# meta developer: @username
# FILENAME: vector.py

__version__ = (2, 0, 0)

import asyncio
import time
from typing import Any, Dict, List, Optional
from urllib.parse import quote_plus

import aiohttp
from herokutl.types import Message

from .. import loader, utils
from ..inline.types import InlineQueryResultArticle, InputTextMessageContent


API_ORIGIN = "https://vector-three-sooty.vercel.app"


class _VectorBackend:
    def __init__(self, module: "Vector") -> None:
        self._module = module
        self._http: Optional[aiohttp.ClientSession] = None
        self._token: str = ""
        self._token_expire: float = 0
        self._search_cache = module._db.pointer("vector", "search_cache", {})

    async def _session(self) -> aiohttp.ClientSession:
        if self._http is None or self._http.closed:
            self._http = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15))
        return self._http

    async def close(self) -> None:
        if self._http is not None and not self._http.closed:
            await self._http.close()

    async def _json(self, method: str, path: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        session = await self._session()
        async with session.request(method, f"{API_ORIGIN}{path}", headers=headers or {}) as response:
            if response.status != 200:
                return {}
            data = await response.json(content_type=None)
            return data if isinstance(data, dict) else {}

    async def token(self) -> str:
        now = time.time()
        if self._token and now < self._token_expire:
            return self._token

        payload = await self._json("GET", "/api/token")
        token = payload.get("token") if isinstance(payload.get("token"), str) else ""
        ttl = int(payload.get("ttl") or 1200)
        if token:
            self._token = token
            self._token_expire = now + max(60, min(ttl, 3600))
        return self._token

    async def search(self, query: str, limit: int) -> List[Dict[str, Any]]:
        query = (query or "").strip()
        if not query:
            return []

        cache_key = f"{query.lower()}:{limit}"
        cached = self._search_cache.get(cache_key)
        if isinstance(cached, dict) and (time.time() - cached.get("stamp", 0) < 300):
            rows = cached.get("rows")
            if isinstance(rows, list):
                return rows

        auth = await self.token()
        headers = {"Authorization": f"Bearer {auth}"} if auth else {}
        data = await self._json("GET", f"/api/search?q={quote_plus(query)}&limit={limit}", headers=headers)
        rows = data.get("results") if isinstance(data.get("results"), list) else []

        normalized: List[Dict[str, Any]] = []
        for item in rows:
            if not isinstance(item, dict):
                continue
            normalized.append(
                {
                    "name": str(item.get("name") or "Unknown"),
                    "author": str(item.get("author") or "@Unknown"),
                    "description": str(item.get("description") or "No description"),
                    "commands": list(item.get("commands") or []),
                    "dependencies": list(item.get("dependencies") or []),
                    "link": str(item.get("link") or item.get("url") or ""),
                }
            )

        self._search_cache[cache_key] = {"stamp": int(time.time()), "rows": normalized}
        return normalized


@loader.tds
class Vector(loader.Module):
    strings = {
        "name": "Vector",
        "prompt": "Enter a query to search.",
        "hint": "Name, command, description, author.",
        "noquery": "You didn't enter a search query, example: {prefix}vector your query",
        "toolong": "Your query is too big, please try reducing it to 120 characters.",
        "notfound": "Nothing found for query {query}.",
        "counter": "{idx}/{total}",
        "install": "Install",
        "author": "by",
        "description": "Description",
        "commands": "Commands",
        "dependencies": "Dependencies",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(loader.ConfigValue("limit", 10, validator=loader.validators.Integer(minimum=1, maximum=30)))
        self._db = None
        self._engine: Optional[_VectorBackend] = None
        self._boot_done = False

    async def client_ready(self, client, db):
        self._db = db
        self._engine = _VectorBackend(self)
        if not self._db.get("vector", "boot_notice_done", False):
            self._db.set("vector", "boot_notice_done", True)
            self._boot_done = True

    async def on_unload(self):
        if self._engine:
            await self._engine.close()

    async def _card(self, mod: Dict[str, Any], index: int, total: int) -> str:
        commands = mod["commands"][:6]
        deps = mod["dependencies"][:6]
        cmd_render = "\n".join(f"• <code>{c}</code>" for c in commands) if commands else "• <code>—</code>"
        dep_render = "\n".join(f"• <code>{d}</code>" for d in deps) if deps else "• <code>—</code>"
        return (
            f"<b>{mod['name']}</b> {self.strings['author']} <code>{mod['author']}</code>\n"
            f"<i>{self.strings['counter'].format(idx=index + 1, total=total)}</i>\n\n"
            f"<b>{self.strings['description']}:</b>\n{mod['description']}\n\n"
            f"<b>{self.strings['commands']}:</b>\n{cmd_render}\n\n"
            f"<b>{self.strings['dependencies']}:</b>\n{dep_render}"
        )

    async def _render_inline_results(self, query: str) -> List[InlineQueryResultArticle]:
        assert self._engine is not None
        modules = await self._engine.search(query, int(self.config["limit"]))
        results: List[InlineQueryResultArticle] = []
        for idx, mod in enumerate(modules):
            text = await self._card(mod, idx, len(modules))
            results.append(
                InlineQueryResultArticle(
                    id=f"vec_{idx}_{abs(hash(mod['name']))}",
                    title=f"{mod['name']} by {mod['author']}",
                    description=mod["description"][:100],
                    input_message_content=InputTextMessageContent(text, "HTML", disable_web_page_preview=True),
                )
            )
        return results

    @loader.inline_handler()
    async def vector_inline_handler(self, event):
        query = (event.inline_query.query or "").strip()
        if not query:
            await event.inline_query.answer(
                [InlineQueryResultArticle(id="empty", title="Vector", description=self.strings["prompt"], input_message_content=InputTextMessageContent(self.strings["hint"], "HTML"))],
                cache_time=0,
            )
            return
        if len(query) > 120:
            await event.inline_query.answer(
                [InlineQueryResultArticle(id="long", title="Vector", description=self.strings["toolong"], input_message_content=InputTextMessageContent(self.strings["toolong"], "HTML"))],
                cache_time=0,
            )
            return
        rows = await self._render_inline_results(query)
        if not rows:
            rows = [InlineQueryResultArticle(id="nf", title="Vector", description=self.strings["notfound"].format(query=query), input_message_content=InputTextMessageContent(self.strings["notfound"].format(query=query), "HTML"))]
        await event.inline_query.answer(rows, cache_time=0)

    async def vectorcmd(self, message: Message):
        query = utils.get_args_raw(message).strip()
        if not query:
            prefix = self.get_prefix()
            await utils.answer(message, f"<b>{self.strings['noquery'].format(prefix=f'<code>{prefix}</code>')}</b>")
            return
        if len(query) > 120:
            await utils.answer(message, f"<b>{self.strings['toolong']}</b>")
            return

        status = await utils.answer(message, "<b>Vector</b>\n<i>Boot sequence initialized...</i>")
        await asyncio.sleep(0.35)
        await utils.answer(status, "<b>Vector</b>\n<i>Syncing remote index...</i>")

        assert self._engine is not None
        modules = await self._engine.search(query, int(self.config["limit"]))
        if not modules:
            await utils.answer(status, f"<b>{self.strings['notfound'].format(query=query)}</b>")
            return

        card = await self._card(modules[0], 0, len(modules))
        await utils.answer(status, card)
