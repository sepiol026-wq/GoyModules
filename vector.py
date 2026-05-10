# ====================================================================================================================
#   ██████╗  ██████╗ ██╗   ██╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
#  ██╔════╝ ██╔═══██╗╚██╗ ██╔╝████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
#  ██║  ███╗██║   ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ███████╗
#  ██║   ██║██║   ██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║
#  ╚██████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗███████║
#   ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
#
#   OFFICIAL USERNAMES: @goymodules | @samsepi0l_ovf
#   MODULE: vector
#
#   THIS MODULE IS LICENSED UNDER GNU AGPLv3, PROTECTED AGAINST UNAUTHORIZED COPYING/RESALE,
#   AND ITS ORIGINAL AUTHORSHIP BELONGS TO @samsepi0l_ovf.
#   ALL OFFICIAL UPDATES, RELEASE NOTES, AND PATCHES ARE PUBLISHED IN THE TELEGRAM CHANNEL @goymodules.
# ====================================================================================================================
# meta banner: https://raw.githubusercontent.com/sepiol026-wq/GoyModules/refs/heads/main/assets/vector.png
# meta developer: @GoyModules

__version__ = (2, 0, 0)

import asyncio
import hashlib
import json
import logging
import re
import time
from typing import Any, Dict, List, Optional
from urllib.parse import quote

import aiohttp
from herokutl.types import Message

from .. import loader, utils

API_BASE = "https://vector-three-sooty.vercel.app"
TOKEN_KEY = "vector_token"
CACHE_KEY = "vector_cache"
USER_KEY = "vector_user"
LOG = logging.getLogger(__name__)

E_LOADING = "<tg-emoji emoji-id=5253952855185829086>⚙️</tg-emoji>"
E_OK = "<tg-emoji emoji-id=5255813619702049821>✅</tg-emoji>"
E_ERR = "<tg-emoji emoji-id=5253864872780769235>❗️</tg-emoji>"
E_FIRE = "<tg-emoji emoji-id=5253877736207821121>🔥</tg-emoji>"
E_CARD = "<tg-emoji emoji-id=5255713220546538619>💳</tg-emoji>"
E_LIST = "<tg-emoji emoji-id=5256230583717079814>📝</tg-emoji>"
E_LINK = "<tg-emoji emoji-id=5253490441826870592>🔗</tg-emoji>"
E_TAG = "<tg-emoji emoji-id=5256054975389247793>📛</tg-emoji>"

JWT_LIKE = re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")


class VectorHTTP:
    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def call(self, method: str, path: str, *, token: Optional[str] = None, params: Optional[dict] = None, data: Optional[dict] = None) -> Optional[Any]:
        sess = await self.session()
        headers = {"User-Agent": "VectorModule/2.0.0"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        url = f"{API_BASE.rstrip('/')}/{path.lstrip('/')}"
        try:
            async with sess.request(method, url, params=params, json=data, headers=headers, timeout=aiohttp.ClientTimeout(total=20)) as resp:
                if resp.status < 200 or resp.status >= 300:
                    return {"_status": resp.status, "_error": await resp.text()}
                ct = (resp.headers.get("content-type") or "").lower()
                if "json" in ct:
                    return await resp.json(content_type=None)
                return await resp.text()
        except Exception as e:
            LOG.exception("Vector request error: %s", e)
            return None


@loader.tds
class Vector(loader.Module):
    strings = {
        "name": "Vector",
        "boot": f"{E_LOADING} <b>Vector запускается...</b>",
        "help": (
            f"{E_TAG} <b>Vector</b>\n"
            f"{E_LIST} <code>.vector &lt;запрос&gt;</code> — поиск модулей\n"
            f"{E_LIST} <code>.vector comments &lt;module&gt;</code> — комментарии\n"
            f"{E_LIST} <code>.vector rate &lt;module&gt; &lt;up/down&gt;</code> — оценка\n"
            f"{E_LIST} <code>.vector open &lt;module&gt;</code> — открыть страницу"
        ),
        "need_query": f"{E_ERR} <b>Укажи запрос.</b>",
        "no_results": f"{E_ERR} <b>Ничего не найдено.</b>",
        "unauth": f"{E_ERR} <b>Ошибка авторизации Vector API.</b>",
        "done": f"{E_OK} <b>Готово.</b>",
    }

    def __init__(self):
        self.http = VectorHTTP()
        self._cache: Dict[str, Any] = {}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self._cache = self.db.get(self.strings["name"], CACHE_KEY, {})

    async def on_unload(self):
        await self.http.close()

    def _mask(self, value: str) -> str:
        if not isinstance(value, str):
            return ""
        value = JWT_LIKE.sub("<jwt-redacted>", value)
        if len(value) <= 64:
            return value
        return value[:32] + "..." + value[-8:]

    def _uid(self) -> str:
        me = self.db.get(self.strings["name"], USER_KEY, "")
        if me:
            return me
        base = f"{time.time()}:{id(self)}"
        uid = hashlib.sha256(base.encode()).hexdigest()[:24]
        self.db.set(self.strings["name"], USER_KEY, uid)
        return uid

    async def _ensure_token(self, force: bool = False) -> Optional[str]:
        token = None if force else self.db.get(self.strings["name"], TOKEN_KEY, "")
        if token:
            return token
        payload = {"user_id": self._uid(), "source": "heroku_vector"}
        out = await self.http.call("POST", "/api/auth/telegram", data=payload)
        if not isinstance(out, dict):
            return None
        token = out.get("token") or out.get("access_token") or ""
        if token:
            self.db.set(self.strings["name"], TOKEN_KEY, token)
            return token
        return None

    def _render_result(self, item: Dict[str, Any], idx: int) -> str:
        name = item.get("name") or "unknown"
        desc = item.get("description") or "—"
        author = item.get("developer") or item.get("author") or "—"
        installs = item.get("installs") or item.get("downloads") or 0
        rating = item.get("rating") or "—"
        link = item.get("url") or item.get("link") or ""
        parts = [
            f"<b>{idx}. {name}</b>",
            f"{E_CARD} Автор: <code>{author}</code>",
            f"{E_FIRE} Рейтинг: <b>{rating}</b> · Установок: <b>{installs}</b>",
            f"{E_LIST} {desc}",
        ]
        if link:
            parts.append(f"{E_LINK} <a href=\"{link}\">Открыть</a>")
        return "\n".join(parts)

    async def _api_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        token = await self._ensure_token()
        if not token:
            return []
        out = await self.http.call("GET", "/api/search", token=token, params={"q": query, "limit": str(limit)})
        if isinstance(out, dict) and out.get("_status") == 401:
            token = await self._ensure_token(force=True)
            if not token:
                return []
            out = await self.http.call("GET", "/api/search", token=token, params={"q": query, "limit": str(limit)})
        if isinstance(out, dict):
            res = out.get("results", [])
            return res if isinstance(res, list) else []
        return out if isinstance(out, list) else []

    async def _api_comments(self, name: str) -> List[Dict[str, Any]]:
        token = await self._ensure_token()
        if not token:
            return []
        out = await self.http.call("GET", f"/api/modules/{quote(name, safe='')}/comments", token=token)
        if isinstance(out, list):
            return out
        if isinstance(out, dict):
            data = out.get("comments", [])
            return data if isinstance(data, list) else []
        return []

    async def _api_rate(self, name: str, action: str) -> bool:
        token = await self._ensure_token()
        if not token:
            return False
        out = await self.http.call("POST", f"/api/rate/{quote(self._uid(), safe='')}/{quote(name, safe='')}/{quote(action, safe='')}", token=token)
        return isinstance(out, dict) and out.get("_status") is None

    @loader.unrestricted
    async def vectorcmd(self, message: Message):
        args = utils.get_args_raw(message).strip()
        if not args:
            await utils.answer(message, self.strings["help"])
            return

        boot = await utils.answer(message, self.strings["boot"])
        parts = args.split(maxsplit=2)
        sub = parts[0].lower()

        if sub == "comments":
            if len(parts) < 2:
                await utils.answer(boot, self.strings["need_query"])
                return
            comments = await self._api_comments(parts[1])
            if not comments:
                await utils.answer(boot, self.strings["no_results"])
                return
            rows = [f"<b>Комментарии к {parts[1]}</b>"]
            for i, c in enumerate(comments[:10], 1):
                user = c.get("user") or c.get("author") or "unknown"
                text = (c.get("text") or c.get("comment") or "").strip()
                text = text[:250] + ("..." if len(text) > 250 else "")
                rows.append(f"\n<b>{i})</b> <code>{user}</code>\n{text or '—'}")
            await utils.answer(boot, "\n".join(rows))
            return

        if sub == "rate":
            if len(parts) < 3 or parts[2].lower() not in {"up", "down"}:
                await utils.answer(boot, f"{E_ERR} <b>Формат:</b> <code>.vector rate module up|down</code>")
                return
            ok = await self._api_rate(parts[1], parts[2].lower())
            await utils.answer(boot, self.strings["done"] if ok else self.strings["unauth"])
            return

        if sub == "open":
            if len(parts) < 2:
                await utils.answer(boot, self.strings["need_query"])
                return
            await utils.answer(boot, f"{E_LINK} https://vector-three-sooty.vercel.app/modules/{quote(parts[1], safe='')}")
            return

        modules = await self._api_search(args, 10)
        if not modules:
            await utils.answer(boot, self.strings["no_results"])
            return

        self._cache["last_query"] = args
        self._cache["last_results"] = modules
        self.db.set(self.strings["name"], CACHE_KEY, self._cache)

        out = [f"{E_OK} <b>Результаты для:</b> <code>{args}</code>"]
        for i, item in enumerate(modules[:10], 1):
            out.append("\n" + self._render_result(item, i))
        await utils.answer(boot, "\n".join(out))
