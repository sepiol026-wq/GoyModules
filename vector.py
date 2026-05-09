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

__version__ = (1, 1, 1)

import asyncio
import ast
import base64
import hashlib
import json
import logging
import re
import time
import uuid
from contextlib import suppress
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import quote, unquote, urljoin

import aiohttp
from herokutl.tl.functions.contacts import UnblockRequest
from herokutl.types import Message

from .. import loader, utils
from ..inline.types import InlineQueryResultArticle, InputTextMessageContent
from ..types import CoreOverwriteError


VECTOR_API_BASE = "https://vector-three-sooty.vercel.app"
VECTOR_TOKEN_PREFIX = "vector-token-v1"
VECTOR_TOKEN_SALT = "vektor_heroku_searchmodulesModbySepiol026-wqGithub"
JWT_RE = re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")
logger = logging.getLogger(__name__)


class VectorAPI:
    def __init__(self, owner: "Vector") -> None:
        self.owner = owner
        self.session: Optional[aiohttp.ClientSession] = None

    @property
    def base(self) -> str:
        return str(self.owner.config["api_base"]).rstrip("/")

    async def connect(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    async def request(
        self,
        method: str,
        path: str,
        *,
        token: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        json_payload: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        with_status: bool = False,
        timeout: int = 15,
    ) -> Union[Dict[str, Any], bytes, None]:
        session = await self.connect()
        url = urljoin(f"{self.base}/", path.lstrip("/"))
        headers = {"User-Agent": "VectorHerokuModule/1.0"}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        try:
            async with session.request(
                method,
                url,
                params=params,
                json=json_payload,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=timeout),
            ) as response:
                if response.status < 200 or response.status >= 300:
                    return {"_status": response.status} if with_status else None
                if raw:
                    return await response.read()
                data = await response.json(content_type=None)
                if with_status and isinstance(data, dict):
                    data.setdefault("_status", response.status)
                return data
        except Exception:
            logger.debug("Vector API request failed: %s %s", method, path, exc_info=True)
            return None

    async def bot_username(self) -> Optional[str]:
        data = await self.request("GET", "/api/tg-bot")
        username = data.get("username") if isinstance(data, dict) else None
        if isinstance(username, str) and username.strip():
            return username.strip().lstrip("@")
        return None

    async def search(self, query: str, limit: int, token: str) -> List[Dict[str, Any]]:
        data = await self.request("GET", "/api/search", token=token, params={"q": query, "limit": str(limit)})
        if not isinstance(data, dict):
            return []
        results = data.get("results", [])
        return [self.normalize(item) for item in results if isinstance(item, dict)]

    async def rate(self, user_id: str, module_name: str, action: str, token: str) -> Optional[Dict[str, Any]]:
        return await self.request(
            "POST",
            f"/api/rate/{quote(user_id, safe='')}/{quote(module_name, safe='')}/{action}",
            token=token,
        )

    async def comments_get(self, module_name: str, token: Optional[str] = None) -> List[Dict[str, Any]]:
        data = await self.request("GET", f"/api/modules/{quote(module_name, safe='')}/comments", token=token)
        if not isinstance(data, dict):
            return []
        return [c for c in data.get("comments", []) if isinstance(c, dict)]

    async def comments_post(self, module_name: str, body: str, token: str, parent_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        payload: Dict[str, Any] = {"body": body}
        if parent_id:
            payload["parent_id"] = parent_id
        return await self.request("POST", f"/api/modules/{quote(module_name, safe='')}/comments", token=token, json_payload=payload)

    async def comment_edit(self, module_name: str, comment_id: str, body: str, token: str) -> Optional[Dict[str, Any]]:
        return await self.request(
            "PATCH",
            f"/api/modules/{quote(module_name, safe='')}/comments/{quote(comment_id, safe='')}",
            token=token,
            json_payload={"body": body},
        )

    async def comment_delete(self, module_name: str, comment_id: str, token: str) -> Optional[Dict[str, Any]]:
        return await self.request(
            "DELETE",
            f"/api/modules/{quote(module_name, safe='')}/comments/{quote(comment_id, safe='')}",
            token=token,
        )

    async def ratings_get(self, module_name: str, token: Optional[str] = None) -> Dict[str, Any]:
        data = await self.request("GET", f"/api/modules/{quote(module_name, safe='')}/ratings", token=token)
        return data if isinstance(data, dict) else {}

    async def security_status(self, module_name: str, token: str) -> Dict[str, Any]:
        data = await self.request(
            "GET",
            f"/api/modules/{quote(module_name, safe='')}/security-check",
            token=token,
            with_status=True,
        )
        return data if isinstance(data, dict) else {}

    async def security_run(self, module_name: str, token: str) -> Dict[str, Any]:
        data = await self.request(
            "POST",
            f"/api/modules/{quote(module_name, safe='')}/security-check",
            token=token,
            with_status=True,
            timeout=120,
        )
        return data if isinstance(data, dict) else {}

    async def download(self, module_name: str, token: str) -> Optional[str]:
        data = await self.request("GET", f"/api/modules/{quote(module_name, safe='')}/download", token=token, raw=True)
        if not isinstance(data, (bytes, bytearray)):
            return None
        return bytes(data).decode("utf-8", errors="replace")

    def download_url(self, module_name: str) -> str:
        return f"{self.base}/api/modules/{quote(module_name, safe='')}/download"

    def source_url(self, module_name: str, given: str = "") -> str:
        return given or f"{self.base}/modules/{quote(module_name, safe='')}/source"

    def normalize(self, data: Dict[str, Any]) -> Dict[str, Any]:
        commands = data.get("commands") if isinstance(data.get("commands"), list) else []
        normalized_commands = []
        for item in commands:
            if not isinstance(item, dict):
                continue
            normalized_commands.append({
                "name": item.get("name") or item.get("cmd") or "",
                "description": item.get("description") or item.get("desc") or "",
            })

        dependencies = data.get("dependencies") if isinstance(data.get("dependencies"), list) else []
        name = str(data.get("name") or data.get("class_name") or "Unknown")
        return {
            "name": name,
            "class_name": data.get("class_name") or name,
            "version": data.get("version") or "?.?.?",
            "author": data.get("developer") or data.get("author") or "@Unknown",
            "description": data.get("description") or "",
            "commands": normalized_commands,
            "dependencies": [str(item) for item in dependencies],
            "likes": int(data.get("likes") or 0),
            "dislikes": int(data.get("dislikes") or 0),
            "banner": data.get("banner"),
            "source_url": self.source_url(name, str(data.get("source_url") or "")),
            "download_url": self.download_url(name),
        }


class VectorAuth:
    def __init__(self, owner: "Vector") -> None:
        self.owner = owner

    def payload_command(self, telegram_id: str, username: str, nickname: str, bucket: Optional[int] = None) -> str:
        bucket = int(time.time() // 10) if bucket is None else bucket
        payload = f"{VECTOR_TOKEN_PREFIX}|{telegram_id}|{bucket}|{username}|{nickname}|{VECTOR_TOKEN_SALT}"
        return "/" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:32]

    def decode_payload(self, token: str) -> Dict[str, Any]:
        try:
            payload = token.split(".")[1]
            payload += "=" * (-len(payload) % 4)
            return json.loads(base64.urlsafe_b64decode(payload.encode()).decode())
        except Exception:
            return {}

    def token_alive(self, token: Optional[str]) -> bool:
        if not token:
            return False
        payload = self.decode_payload(token)
        exp = payload.get("exp")
        if not isinstance(exp, (int, float)):
            return False
        return exp - time.time() > 60

    def user_id(self, token: str) -> Optional[str]:
        sub = self.decode_payload(token).get("sub")
        return str(sub) if sub else None

    async def ensure(self, force: bool = False) -> Optional[str]:
        cached = self.owner.get("auth_token", None)
        if not force and self.token_alive(cached):
            return cached

        token = await self.obtain()
        if token:
            self.owner.set("auth_token", token)
        return token

    async def obtain(self) -> Optional[str]:
        bot_username = await self.owner.api.bot_username()
        if not bot_username:
            return None

        client = self.owner.client
        me = await client.get_me()
        telegram_id = str(getattr(me, "id", ""))
        username = getattr(me, "username", None) or ""
        first_name = getattr(me, "first_name", None) or ""
        last_name = getattr(me, "last_name", None) or ""
        nickname = " ".join(part for part in (first_name, last_name) if part).strip() or username or telegram_id

        with suppress(Exception):
            await client(UnblockRequest(bot_username))

        for attempt in range(2):
            bucket = int(time.time() // 10) - attempt
            cmd = self.payload_command(telegram_id, username, nickname, bucket=bucket)
            try:
                async with client.conversation(bot_username, timeout=15, exclusive=False) as conv:
                    outgoing = await conv.send_message(cmd)
                    try:
                        response = await asyncio.wait_for(conv.get_response(), timeout=14)
                        token = self.extract_token(getattr(response, "raw_text", "") or getattr(response, "text", ""))
                        with suppress(Exception):
                            await outgoing.delete()
                        if token:
                            return token
                    except asyncio.TimeoutError:
                        with suppress(Exception):
                            await outgoing.delete()
            except Exception:
                pass

        for attempt in range(2):
            bucket = int(time.time() // 10) - attempt
            cmd = self.payload_command(telegram_id, username, nickname, bucket=bucket)
            try:
                outgoing = await client.send_message(bot_username, cmd)
            except Exception:
                continue

            deadline = time.time() + 20
            token = None
            while time.time() < deadline:
                await asyncio.sleep(1.5)
                try:
                    async for msg in client.iter_messages(bot_username, limit=3):
                        if msg.out:
                            continue
                        candidate = self.extract_token(getattr(msg, "raw_text", "") or getattr(msg, "text", ""))
                        if candidate:
                            token = candidate
                            break
                except Exception:
                    pass
                if token:
                    break

            with suppress(Exception):
                await outgoing.delete()
            if token:
                return token

        return None

    def extract_token(self, text: str) -> Optional[str]:
        match = JWT_RE.search(text or "")
        return match.group(0) if match else None


class VectorInstaller:
    def _loader_module(self, plugin: "Vector") -> Optional[loader.Module]:
        lookup = getattr(plugin, "lookup", None) or getattr(plugin.allmodules, "lookup", None)
        if not callable(lookup):
            return None

        module = lookup("loader")
        return module if module and callable(getattr(module, "load_module", None)) else None

    def _class_name(self, code: str) -> Optional[str]:
        try:
            tree = ast.parse(code)
            for node in tree.body:
                if not isinstance(node, ast.ClassDef):
                    continue

                for base in node.bases:
                    if (
                        isinstance(base, ast.Attribute)
                        and getattr(base.value, "id", None) == "loader"
                        and base.attr == "Module"
                    ) or (isinstance(base, ast.Name) and base.id == "Module"):
                        return node.name
        except Exception:
            logger.debug("Unable to parse Vector module class name", exc_info=True)

        return None

    def _module_loaded(self, plugin: "Vector", class_name: Optional[str], code: str) -> bool:
        lookup = getattr(plugin, "lookup", None) or getattr(plugin.allmodules, "lookup", None)
        if class_name and callable(lookup):
            module = lookup(class_name)
            if module:
                return True

        with suppress(Exception):
            for module in getattr(plugin.allmodules, "modules", []):
                if class_name and module.__class__.__name__ == class_name:
                    return True

                source = getattr(module, "__source__", None)
                if isinstance(source, str) and source.strip() == code.strip():
                    return True

        return False

    async def execute(self, plugin: "Vector", module_name: str, token: str) -> Tuple[str, List[str]]:
        code = await plugin.api.download(module_name, token)
        if not code:
            return "error", []

        loader_module = self._loader_module(plugin)
        if loader_module is None:
            logger.error("Heroku built-in loader module is unavailable; Vector cannot install %s", module_name)
            return "error", []

        class_name = self._class_name(code)
        origin = plugin.api.download_url(module_name)

        try:
            await loader_module.load_module(code, None, origin=origin, save_fs=True)
        except CoreOverwriteError:
            return "overwrite", []
        except Exception:
            logger.exception("Heroku built-in loader failed to install %s", module_name)
            return "error", []

        if self._module_loaded(plugin, class_name, code):
            if getattr(plugin, "fully_loaded", True):
                with suppress(Exception):
                    plugin.update_modules_in_db()
            return "success", []

        logger.error("Heroku built-in loader finished without loading %s", module_name)
        return "error", []


class VectorUI:
    def __init__(self, owner: "Vector") -> None:
        self.owner = owner

    def emoji(self, key: str) -> str:
        return self.owner.THEMES[self.owner.config["theme"]][key]

    def plain_len(self, text: str) -> int:
        return len(re.sub(r"<[^>]+>", "", text))

    def format(self, data: Dict[str, Any], index: int = 1, total: int = 1) -> str:
        name = utils.escape_html(str(data.get("name", "Unknown")))
        author = utils.escape_html(str(data.get("author", "@Unknown")))
        version = str(data.get("version") or "?.?.?")
        text = f"{self.emoji('module')} <code>{name}</code> <b>{self.owner.strings['author']}</b> <code>{author}</code>"
        if version != "?.?.?":
            text += f" (<code>v{utils.escape_html(version)}</code>)"
        if total > 1:
            text += f"\n{self.emoji('modules_list')} <i>{self.owner.strings['counter'].format(idx=index, total=total)}</i>"

        description = data.get("description")
        if description:
            text += f"\n\n{self.emoji('description')} <b>{self.owner.strings['description']}:</b>\n<blockquote expandable>{utils.escape_html(str(description))}</blockquote>"

        text += self.render_commands(data.get("commands", []), 3700 - self.plain_len(text))
        text += self.render_dependencies(data.get("dependencies", []), 3700 - self.plain_len(text))
        return text

    def render_commands(self, commands: List[Dict[str, Any]], limit: int) -> str:
        if not commands:
            return ""
        rows = []
        for index, item in enumerate(commands):
            name = utils.escape_html(str(item.get("name") or ""))
            description = utils.escape_html(str(item.get("description") or "")).split("\n")[0]
            row = f"<code>{self.owner.get_prefix()}{name}</code> {description}".strip()
            extra = f"<i>{self.owner.strings['morecommands'].format(remaining=len(commands) - index)}</i>"
            if self.plain_len("\n".join(rows + [row, extra])) > limit and index > 0:
                rows.append(extra)
                break
            rows.append(row)
        return f"\n\n{self.emoji('command')} <b>{self.owner.strings['commands']}:</b>\n<blockquote expandable>{chr(10).join(rows)}</blockquote>"

    def render_dependencies(self, dependencies: List[str], limit: int) -> str:
        if not dependencies:
            return ""
        rows = []
        for index, dependency in enumerate(dependencies):
            row = f"<code>{utils.escape_html(dependency)}</code>"
            extra = f"<i>{self.owner.strings['moredeps'].format(remaining=len(dependencies) - index)}</i>"
            if self.plain_len("\n".join(rows + [row, extra])) > limit and index > 0:
                rows.append(extra)
                break
            rows.append(row)
        return f"\n\n{self.emoji('dependency')} <b>{self.owner.strings['dependencies']}:</b>\n<blockquote expandable>{chr(10).join(rows)}</blockquote>"

    def security_icon(self, verdict: str) -> str:
        if verdict == "safe":
            return self.emoji("safe")
        if verdict == "unsafe":
            return self.emoji("unsafe")
        return self.emoji("shield")

    def security_verdict_label(self, verdict: str) -> str:
        try:
            labels = self.owner.strings["security_verdicts"]
        except Exception:
            labels = {}
        if isinstance(labels, dict):
            return str(labels.get(verdict) or labels.get("unknown") or verdict)
        return verdict or "unknown"

    def format_security(self, module_name: str, data: Dict[str, Any]) -> str:
        check = data.get("check") if isinstance(data.get("check"), dict) else None
        if isinstance(data.get("quota"), dict):
            quota = data.get("quota")
        elif check and isinstance(check.get("quota"), dict):
            quota = check.get("quota")
        else:
            quota = None
        if not check:
            left = quota.get("remaining") if isinstance(quota, dict) else "?"
            limit = quota.get("limit") if isinstance(quota, dict) else "?"
            return (
                f"{self.emoji('shield')} <b>{self.owner.strings['security_title'].format(name=utils.escape_html(module_name))}</b>\n\n"
                f"{self.emoji('warn')} {self.owner.strings['security_unchecked']}\n"
                f"{self.emoji('quota')} <i>{self.owner.strings['security_quota'].format(remaining=left, limit=limit)}</i>"
            )

        verdict = str(check.get("verdict") or "unknown")
        label = utils.escape_html(str(check.get("label") or self.security_verdict_label(verdict)))
        confidence = int(check.get("confidence") or 0)
        summary = utils.escape_html(str(check.get("summary") or self.owner.strings["security_no_summary"]))
        details = check.get("details") if isinstance(check.get("details"), dict) else {}
        static = details.get("static") if isinstance(details.get("static"), dict) else {}
        findings = static.get("findings") if isinstance(static.get("findings"), dict) else {}
        critical = findings.get("critical") if isinstance(findings.get("critical"), list) else []
        warning = findings.get("warning") if isinstance(findings.get("warning"), list) else []
        info = findings.get("info") if isinstance(findings.get("info"), list) else []
        risk = utils.escape_html(str(static.get("risk") or "unknown"))
        score = utils.escape_html(str(static.get("score") if static.get("score") is not None else "?"))

        lines = [
            f"{self.security_icon(verdict)} <b>{self.owner.strings['security_title'].format(name=utils.escape_html(module_name))}</b>",
            "",
            f"{self.emoji('shield')} <b>{self.owner.strings['security_verdict']}:</b> <code>{label}</code> (<code>{confidence}%</code>)",
            f"{self.emoji('stats')} <b>{self.owner.strings['security_static']}:</b> risk <code>{risk}</code>, score <code>{score}</code>",
            f"{self.emoji('description')} <b>{self.owner.strings['security_summary']}:</b>\n<blockquote expandable>{summary}</blockquote>",
        ]

        compact = []
        for title, values in ((self.owner.strings["security_critical"], critical), (self.owner.strings["security_warning"], warning), (self.owner.strings["security_info"], info)):
            if values:
                compact.append(f"<b>{title}</b>: " + ", ".join(utils.escape_html(str(item.get("title") or "?")) for item in values[:3] if isinstance(item, dict)))
        if compact:
            lines.append(f"{self.emoji('search')} <b>{self.owner.strings['security_findings']}:</b>\n<blockquote expandable>{chr(10).join(compact)}</blockquote>")

        if isinstance(quota, dict):
            lines.append(f"{self.emoji('quota')} <i>{self.owner.strings['security_quota'].format(remaining=quota.get('remaining', '?'), limit=quota.get('limit', '?'))}</i>")
        return "\n".join(lines)

    def buttons(self, data: Dict[str, Any], index: int, modules: Optional[List[Dict[str, Any]]], query: str) -> List[List[Dict[str, Any]]]:
        name = str(data.get("name") or "")
        buttons = [
            [
                {"text": self.owner.strings["query"], "copy": query},
                {"text": self.owner.strings["install"], "callback": self.owner.install, "args": (name, index, modules, query)},
                {"text": self.owner.strings["page"], "url": data.get("source_url")},
            ],
            [
                {"text": f"👍 {data.get('likes', 0)}", "callback": self.owner.rate, "args": (name, "like", index, modules, query)},
                {"text": f"👎 {data.get('dislikes', 0)}", "callback": self.owner.rate, "args": (name, "dislike", index, modules, query)},
                {"text": self.owner.strings["comments_btn"], "callback": self.owner.comments, "args": (name, index, modules, query)},
            ],
            [
                {"text": self.owner.strings["security_check_btn"], "callback": self.owner.security_check, "args": (name, index, modules, query)},
            ],
        ]
        if modules and len(modules) > 1:
            buttons[1].insert(1, {"text": self.owner.strings["counter"].format(idx=index + 1, total=len(modules)), "callback": self.owner.show, "args": (index, modules, query)})
            navigation = []
            if index > 0:
                navigation.append({"text": "◀️", "callback": self.owner.navigate, "args": (index - 1, modules, query)})
            if index < len(modules) - 1:
                navigation.append({"text": "▶️", "callback": self.owner.navigate, "args": (index + 1, modules, query)})
            if navigation:
                buttons.append(navigation)
        return buttons

    def pagination(self, modules: List[Dict[str, Any]], query: str, page: int = 0, current: int = 0) -> List[List[Dict[str, Any]]]:
        buttons = []
        start = page * 8
        end = min(start + 8, len(modules))
        for index in range(start, end):
            module = modules[index]
            buttons.append([{
                "text": f"{index + 1}. {module.get('name', 'Unknown')} by {module.get('author', '@Unknown')}",
                "callback": self.owner.navigate,
                "args": (index, modules, query),
            }])
        navigation = []
        if page > 0:
            navigation.append({"text": "◀️", "callback": self.owner.page, "args": (page - 1, modules, query, current)})
        if page < (len(modules) + 7) // 8 - 1:
            navigation.append({"text": "▶️", "callback": self.owner.page, "args": (page + 1, modules, query, current)})
        if navigation:
            buttons.append(navigation)
        buttons.append([{"text": "✖️", "callback": self.owner.navigate, "args": (current, modules, query)}])
        return buttons


@loader.tds
class Vector(loader.Module):
    """Search modules in Vector: https://vector-three-sooty.vercel.app/"""

    strings = {
        "name": "Vector",
        "_cls_doc": "Vector module search for Heroku Userbot. https://vector-three-sooty.vercel.app",
        "author": "by",
        "description": "Description",
        "commands": "Commands",
        "dependencies": "Dependencies",
        "morecommands": "...and {remaining} more commands.",
        "moredeps": "...and {remaining} more dependencies.",
        "list": "All found modules:",
        "search": "Searching for {query}...",
        "noquery": "You didn't enter a search query, example: {prefix}vector your query",
        "notfound": "Nothing found for query {query}.",
        "toolong": "Your query is too big, please try reducing it to 120 characters.",
        "auth_error": "Vector authorization failed. Try again a little later.",
        "added": "✔ Rating submitted!",
        "changed": "✔ Rating has been changed!",
        "deleted": "✔ Rating deleted!",
        "prompt": "Enter a query to search.",
        "hint": "Name, command, description, author.",
        "retry": "Try another query.",
        "query": "Query",
        "install": "Install",
        "counter": "{idx}/{total}",
        "page": "Page",
        "success": "✔ Module successfully installed!",
        "error": "✘ Error, perhaps the module is broken!",
        "overwrite": "✘ Error, module tried to overwrite built-in module!",
        "dependency": "✘ Dependencies installation error! {deps}",
        "rated_set": "✔ Rating has been set!",
        "rated_removed": "✔ Rating has been removed!",
        "docbase": "Vector API base URL.",
        "doctheme": "Theme for emojis.",
        "doclimit": "Maximum amount of search results.",
        "security_check_btn": "🛡 Security check",
        "security_title": "Module check — {name}",
        "security_checking": "Checking module status via Vector API...",
        "security_running": "Running security check via Vector API...",
        "security_run_btn": "Run check",
        "security_cached": "Using cached security result.",
        "security_verdict": "Verdict",
        "security_static": "Static analysis",
        "security_summary": "Summary",
        "security_findings": "Signals",
        "security_critical": "critical",
        "security_warning": "warnings",
        "security_info": "info",
        "security_unchecked": "Module is not checked yet. You can start a new check; it will spend one daily limit slot.",
        "security_no_summary": "No readable summary.",
        "security_quota": "Checks left today: {remaining}/{limit}",
        "security_limit": "Daily check limit is exhausted.",
        "security_fetch_error": "Failed to get module security status.",
        "edit_error": "Failed to update the inline message.",
        "security_verdicts": {"safe": "safe", "suspicious": "suspicious", "unsafe": "unsafe", "unknown": "unknown"},
        "comments_btn": "💬",
        "comments_title": "💬 <b>Comments — {name}</b>",
        "comments_empty": "No comments yet. Be the first!",
        "comments_fetch_error": "Failed to load comments.",
        "comment_posted": "✔ Comment posted!",
        "comment_post_error": "✘ Failed to post comment.",
        "comments_back": "◀️ Back",
        "comments_write": "🌐 Website",
    }

    strings_ru = {
        "_cls_doc": "Поиск модулей Vector для Heroku Userbot. https://vector-three-sooty.vercel.app",
        "author": "от",
        "description": "Описание",
        "commands": "Команды",
        "dependencies": "Зависимости",
        "morecommands": "...и еще {remaining} команд.",
        "moredeps": "...и еще {remaining} зависимостей.",
        "list": "Все найденные модули:",
        "search": "Поиск по запросу {query}...",
        "noquery": "Вы не ввели запрос для поиска, пример: {prefix}vector ваш запрос",
        "notfound": "Ничего не найдено по запросу {query}.",
        "toolong": "Ваш запрос слишком большой, пожалуйста, сократите его до 120 символов.",
        "auth_error": "Не удалось авторизоваться в Vector. Попробуйте чуть позже.",
        "added": "✔ Оценка добавлена!",
        "changed": "✔ Оценка изменена!",
        "deleted": "✔ Оценка удалена!",
        "prompt": "Введите запрос для поиска.",
        "hint": "Название, команда, описание, автор.",
        "retry": "Попробуйте другой запрос.",
        "query": "Запрос",
        "install": "Установить",
        "counter": "{idx}/{total}",
        "page": "Страница",
        "success": "✔ Модуль успешно установлен!",
        "error": "✘ Ошибка, возможно, модуль сломан!",
        "overwrite": "✘ Ошибка, модуль попытался перезаписать встроенный модуль!",
        "dependency": "✘ Ошибка установки зависимостей! {deps}",
        "rated_set": "✔ Оценка поставлена!",
        "rated_removed": "✔ Оценка убрана!",
        "docbase": "Базовый URL Vector API.",
        "doctheme": "Тема эмодзи.",
        "doclimit": "Максимальное количество результатов поиска.",
        "security_check_btn": "🛡 Проверка безопасности",
        "security_title": "Проверка модуля — {name}",
        "security_checking": "Проверяю статус безопасности через Vector API...",
        "security_running": "Запускаю проверку безопасности через Vector API...",
        "security_run_btn": "Запустить проверку",
        "security_cached": "Показываю кэшированный результат проверки.",
        "security_verdict": "Вердикт",
        "security_static": "Статический анализ",
        "security_summary": "Итог",
        "security_findings": "Сигналы",
        "security_critical": "критичные",
        "security_warning": "предупреждения",
        "security_info": "инфо",
        "security_unchecked": "Модуль ещё не проверен. Можно запустить проверку, она спишет один слот дневного лимита.",
        "security_no_summary": "Нет читаемого описания результата.",
        "security_quota": "Проверок сегодня осталось: {remaining}/{limit}",
        "security_limit": "Лимит проверок на сегодня исчерпан.",
        "security_fetch_error": "Не удалось получить статус проверки модуля.",
        "edit_error": "Не удалось обновить inline-сообщение.",
        "security_verdicts": {"safe": "безопасен", "suspicious": "подозрителен", "unsafe": "небезопасен", "unknown": "неизвестно"},
        "comments_btn": "💬",
        "comments_title": "💬 <b>Комментарии — {name}</b>",
        "comments_empty": "Комментариев пока нет. Будьте первым!",
        "comments_fetch_error": "Не удалось загрузить комментарии.",
        "comment_posted": "✔ Комментарий опубликован!",
        "comment_post_error": "✘ Не удалось опубликовать комментарий.",
        "comments_back": "◀️ Назад",
        "comments_write": "🌐 Сайт",
    }

    THEMES = {
        "default": {
            "search": '<tg-emoji emoji-id="5447459604524971717">🔎</tg-emoji>',
            "error": '<tg-emoji emoji-id="5388785832956016892">❌</tg-emoji>',
            "warn": "⚠️",
            "description": '<tg-emoji emoji-id="6008090211181923982">📝</tg-emoji>',
            "command": '<tg-emoji emoji-id="5877260593903177342">⚙</tg-emoji>',
            "dependency": '<tg-emoji emoji-id="5325732612084351248">📦</tg-emoji>',
            "module": '<tg-emoji emoji-id="5924720918826848520">📦</tg-emoji>',
            "modules_list": '<tg-emoji emoji-id="5883973610606956186">🗂</tg-emoji>',
            "shield": "🛡",
            "safe": "✅",
            "unsafe": "❌",
            "stats": "📊",
            "quota": "⏳",
        },
        "neon": {
            "search": "💠",
            "error": "🟥",
            "warn": "🟨",
            "description": "🧬",
            "command": "🛠",
            "dependency": "🧩",
            "module": "🚀",
            "modules_list": "🗂",
            "shield": "🛡",
            "safe": "✅",
            "unsafe": "❌",
            "stats": "📊",
            "quota": "⏳",
        },
    }

    def __init__(self) -> None:
        self.config = loader.ModuleConfig(
            loader.ConfigValue("api_base", VECTOR_API_BASE, lambda: self.strings("docbase"), validator=loader.validators.Link()),
            loader.ConfigValue("theme", "default", lambda: self.strings("doctheme"), validator=loader.validators.Choice(["default", "neon"])),
            loader.ConfigValue("limit", 10, lambda: self.strings("doclimit"), validator=loader.validators.Integer(minimum=1, maximum=25)),
        )

    async def client_ready(self, client: "herokutl.TelegramClient", database: "loader.Database") -> None:
        self.client = client
        self.database = database
        self.api = VectorAPI(self)
        self.auth = VectorAuth(self)
        self.installer = VectorInstaller()
        self.ui = VectorUI(self)
        self.bot = getattr(getattr(self, "inline", None), "bot", None) or getattr(getattr(self, "inline", None), "_bot", None)
        self._security_cache: Dict[str, Dict[str, Any]] = {}

    async def on_unload(self) -> None:
        if hasattr(self, "api"):
            await self.api.close()

    async def answer(self, target: Any, text: str = "", alert: bool = False) -> None:
        try:
            await target.answer(text, show_alert=alert)
        except Exception:
            logger.debug("Unable to answer inline callback", exc_info=True)

    def _safe_inline_text(self, text: str) -> str:
        safe = text.replace("<blockquote expandable>", "<blockquote>")
        allowed = {"a", "b", "blockquote", "code", "i", "tg-emoji"}

        def keep_supported_tag(match: re.Match) -> str:
            return match.group(0) if match.group(1).lower() in allowed else ""

        safe = re.sub(r"</?([a-zA-Z][\w-]*)(?:\s+[^>]*)?>", keep_supported_tag, safe)
        return safe[:3900]

    def _preview_url(self, url: Optional[str]) -> str:
        url = str(url or "").strip()
        return url if url.startswith(("http://", "https://")) else ""

    def _with_preview_link(self, text: str, url: Optional[str]) -> str:
        preview_url = self._preview_url(url)
        if not preview_url or preview_url in text:
            return text

        escaped = utils.escape_html(preview_url).replace('"', "&quot;")
        return f'<a href="{escaped}">\u200b</a>\n{text}'

    def _preview_options(self, url: Optional[str]) -> Dict[str, Any]:
        preview_url = self._preview_url(url)
        if not preview_url:
            return {}

        return {
            "url": preview_url,
            "prefer_large_media": True,
            "show_above_text": True,
        }

    def _is_inline_target(self, target: Any) -> bool:
        return any(hasattr(target, attr) for attr in ("inline_message_id", "unit_id", "inline_manager"))

    async def _edit_inline_with_preview(
        self,
        target: Any,
        text: str,
        buttons: List[List[Dict[str, Any]]],
        preview_url: str,
    ) -> bool:
        manager = getattr(target, "inline_manager", None)
        if not manager or not preview_url:
            return False

        unit_id = getattr(target, "unit_id", None)
        with suppress(Exception):
            if unit_id in getattr(target, "_units", {}):
                target._units[unit_id]["buttons"] = buttons

        inline_message_id = getattr(target, "inline_message_id", None)
        params: Dict[str, Any] = {"inline_message_id": inline_message_id} if inline_message_id else {}
        chat_id = getattr(target, "chat_id", None)
        message_id = getattr(target, "message_id", None)
        if not params and chat_id and message_id:
            params = {"chat_id": chat_id, "message_id": message_id}
        if not params:
            return False

        try:
            await manager.bot.edit_message_text(
                text,
                **params,
                reply_markup=manager.generate_markup(buttons),
                link_preview_options=self._preview_options(preview_url),
            )
            return True
        except Exception:
            logger.debug("Unable to edit Vector inline preview directly", exc_info=True)
            return False

    async def edit(self, target: Any, text: str, buttons: List[List[Dict[str, Any]]], banner: Optional[str] = None) -> bool:
        preview_url = self._preview_url(banner)
        for candidate in (text, self._safe_inline_text(text)):
            candidate = self._with_preview_link(candidate, preview_url)
            try:
                if self._is_inline_target(target) and await self._edit_inline_with_preview(target, candidate, buttons, preview_url):
                    return True

                if hasattr(target, "edit"):
                    kwargs = {"reply_markup": buttons}
                    if self._is_inline_target(target):
                        kwargs["disable_web_page_preview"] = False
                    else:
                        kwargs["link_preview"] = True
                    ok = await target.edit(candidate, **kwargs)
                    if ok is not False:
                        return True

                answer_kwargs = {"reply_markup": buttons}
                if self._is_inline_target(target):
                    answer_kwargs["disable_web_page_preview"] = False
                else:
                    answer_kwargs["link_preview"] = True
                result = await utils.answer(target, candidate, **answer_kwargs)
                if result is not None:
                    return True
            except Exception:
                logger.warning("Unable to edit Vector inline message; retrying with safe text", exc_info=True)

        with suppress(Exception):
            await self.answer(target, self.strings["edit_error"], True)
        return False

    async def navigate(self, callback: Any, index: int, modules: List[Dict[str, Any]], query: str = "") -> None:
        await self.answer(callback)
        if 0 <= index < len(modules):
            data = modules[index]
            await self.edit(callback, self.ui.format(data, index + 1, len(modules)), self.ui.buttons(data, index, modules, query), data.get("banner"))

    async def show(self, callback: Any, index: int, modules: List[Dict[str, Any]], query: str) -> None:
        await self.answer(callback)
        await self.edit(callback, f"{self.ui.emoji('modules_list')} <b>{self.strings['list']}</b>", self.ui.pagination(modules, query, 0, index))

    async def page(self, callback: Any, current: int, modules: List[Dict[str, Any]], query: str, index: int) -> None:
        await self.answer(callback)
        await self.edit(callback, f"{self.ui.emoji('modules_list')} <b>{self.strings['list']}</b>", self.ui.pagination(modules, query, current, index))

    async def rate(self, callback: Any, module_name: str, action: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str = "") -> None:
        token = await self.auth.ensure()
        user_id = self.auth.user_id(token or "")
        if not token or not user_id:
            return await self.answer(callback, self.strings["auth_error"], True)

        response = await self.api.rate(user_id, module_name, action, token)
        if not response or not response.get("ok"):
            token = await self.auth.ensure(force=True)
            user_id = self.auth.user_id(token or "")
            response = await self.api.rate(user_id, module_name, action, token) if token and user_id else None
        if not response or not response.get("ok"):
            return await self.answer(callback, self.strings["error"], True)

        refreshed = await self.api.search(query or module_name, int(self.config["limit"]), token)
        fresh = next((item for item in refreshed if item.get("name") == module_name), None)
        if modules and index < len(modules) and fresh:
            modules[index].update(fresh)
            data = modules[index]
        else:
            data = fresh or {"name": module_name, "likes": 0, "dislikes": 0, "source_url": self.api.source_url(module_name)}

        await self.edit(callback, self.ui.format(data, index + 1, len(modules or [data])), self.ui.buttons(data, index, modules, query), data.get("banner"))
        state = response.get("rating", {}).get("state")
        await self.answer(callback, self.strings["rated_removed" if state == "removed" else "rated_set"], True)

    async def install(self, callback: Any, module_name: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str = "") -> None:
        token = await self.auth.ensure()
        if not token:
            return await self.answer(callback, self.strings["auth_error"], True)

        state, dependencies = await self.installer.execute(self, module_name, token)
        if state == "success":
            await self.answer(callback, self.strings["success"], True)
        elif state == "dependency":
            formatted = f"({','.join(dependencies[:5])})" if dependencies else ""
            await self.answer(callback, self.strings["dependency"].format(deps=formatted), True)
        elif state == "overwrite":
            await self.answer(callback, self.strings["overwrite"], True)
        else:
            await self.answer(callback, self.strings["error"], True)

    def _cache_security(self, module_name: str, data: Dict[str, Any]) -> None:
        check = data.get("check") if isinstance(data.get("check"), dict) else None
        if check:
            self._security_cache[module_name] = data

    def _security_cached(self, module_name: str) -> Optional[Dict[str, Any]]:
        data = self._security_cache.get(module_name)
        return data if isinstance(data, dict) and isinstance(data.get("check"), dict) else None

    def _security_status_code(self, data: Dict[str, Any]) -> int:
        try:
            return int(data.get("_status") or 0)
        except Exception:
            return 0

    async def security_check(self, callback: Any, module_name: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str = "") -> None:
        checked_buttons = self._security_buttons(module_name, index, modules, query, checked=True)
        cached = self._security_cached(module_name)
        if cached:
            return await self.edit(
                callback,
                f"{self.ui.emoji('safe')} <i>{self.strings['security_cached']}</i>\n\n{self.ui.format_security(module_name, cached)}",
                checked_buttons,
            )

        loading_buttons = self._security_buttons(module_name, index, modules, query, checked=True)
        await self.edit(callback, f"{self.ui.emoji('search')} <b>{self.strings['security_checking']}</b>", loading_buttons)

        token = await self.auth.ensure()
        if not token:
            token = await self.auth.ensure(force=True)
        if not token:
            return await self.edit(callback, f"{self.ui.emoji('error')} <b>{self.strings['auth_error']}</b>", loading_buttons)

        data = await self.api.security_status(module_name, token)
        status = self._security_status_code(data)
        if not data or status >= 400:
            logger.warning("Vector security status failed for %s with status=%s data=%r", module_name, status, data)
            return await self.edit(callback, f"{self.ui.emoji('error')} <b>{self.strings['security_fetch_error']}</b>", loading_buttons)

        self._cache_security(module_name, data)
        checked = bool(data.get("checked") and isinstance(data.get("check"), dict))
        buttons = self._security_buttons(module_name, index, modules, query, checked=checked)
        await self.edit(callback, self.ui.format_security(module_name, data), buttons)

    async def security_run(self, callback: Any, module_name: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str = "") -> None:
        buttons = self._security_buttons(module_name, index, modules, query, checked=False)
        await self.edit(callback, f"{self.ui.emoji('search')} <b>{self.strings['security_running']}</b>", buttons)

        token = await self.auth.ensure()
        if not token:
            token = await self.auth.ensure(force=True)
        if not token:
            return await self.edit(callback, f"{self.ui.emoji('error')} <b>{self.strings['auth_error']}</b>", buttons)

        data = await self.api.security_run(module_name, token)
        status = self._security_status_code(data)
        if status == 429:
            return await self.edit(callback, f"{self.ui.emoji('warn')} <b>{self.strings['security_limit']}</b>", buttons)
        if not data or status >= 400:
            logger.warning("Vector security run failed for %s with status=%s data=%r", module_name, status, data)
            return await self.edit(callback, f"{self.ui.emoji('error')} <b>{self.strings['security_fetch_error']}</b>", buttons)

        self._cache_security(module_name, data)
        await self.edit(callback, self.ui.format_security(module_name, data), self._security_buttons(module_name, index, modules, query, checked=True))

    def _security_buttons(self, module_name: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str, *, checked: bool) -> List[List[Dict[str, Any]]]:
        buttons = [
            [
                {"text": self.strings["comments_back"], "callback": self.navigate, "args": (index, modules or [], query)},
                {"text": self.strings["page"], "url": self.api.source_url(module_name)},
            ],
        ]
        if not checked:
            buttons.append([{"text": self.strings["security_run_btn"], "callback": self.security_run, "args": (module_name, index, modules, query)}])
        return buttons

    def _format_comments(self, comments: List[Dict[str, Any]], module_name: str) -> str:
        """Render comment thread as HTML for Telegram message."""
        if not comments:
            return self.strings["comments_empty"]
        lines = []
        top = [c for c in comments if not c.get("parent_id")]
        replies_map: Dict[str, List[Dict[str, Any]]] = {}
        for c in comments:
            pid = c.get("parent_id")
            if pid:
                replies_map.setdefault(str(pid), []).append(c)

        for c in top[:15]:
            cid = str(c.get("id", ""))
            author = utils.escape_html(str(c.get("author_name") or c.get("author_username") or "Unknown"))
            username = c.get("author_username")
            author_link = f'<a href="https://t.me/{username}">{author}</a>' if username else author
            body = utils.escape_html(str(c.get("body", "")))
            can_edit = c.get("can_edit", False)
            edit_hint = " ✏️" if can_edit else ""
            lines.append(f"👤 <b>{author_link}</b>{edit_hint}\n{body}")
            for r in replies_map.get(cid, [])[:3]:
                r_author = utils.escape_html(str(r.get("author_name") or r.get("author_username") or "Unknown"))
                r_username = r.get("author_username")
                r_link = f'<a href="https://t.me/{r_username}">{r_author}</a>' if r_username else r_author
                r_body = utils.escape_html(str(r.get("body", "")))
                lines.append(f"  ↳ <b>{r_link}</b>: {r_body}")
        total = len(comments)
        if total > 15:
            lines.append(f"<i>...и ещё {total - 15} комментариев на сайте.</i>")
        return "\n\n".join(lines)

    def _comments_buttons(self, module_name: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str) -> List[List[Dict[str, Any]]]:
        source_url = self.api.source_url(module_name)
        return [
            [
                {"text": self.strings["comments_back"], "callback": self.navigate, "args": (index, modules or [], query)},
                {"text": self.strings["comments_write"], "url": source_url},
            ],
        ]

    async def comments(self, callback: Any, module_name: str, index: int, modules: Optional[List[Dict[str, Any]]], query: str = "") -> None:
        await self.answer(callback)
        token = await self.auth.ensure()
        raw = await self.api.comments_get(module_name, token=token)
        if raw is None:
            return await self.answer(callback, self.strings["comments_fetch_error"], True)
        text = f"{self.strings['comments_title'].format(name=utils.escape_html(module_name))}\n\n{self._format_comments(raw, module_name)}"
        await self.edit(callback, text, self._comments_buttons(module_name, index, modules, query))

    @loader.inline_handler(
        ru_doc="(запрос) - поиск модулей в Vector.",
        en_doc="(query) - search modules in Vector.",
    )
    async def vector(self, event: "loader.InlineCall") -> Union[Dict[str, str], None]:
        query = event.args
        if not query:
            return {
                "title": self.strings["prompt"],
                "description": self.strings["hint"],
                "message": f"{self.ui.emoji('error')} <b>{self.strings['noquery'].format(prefix=f'<code>@{self.inline.bot_username} ')}</code></b>",
            }
        if len(query) > 120:
            return {
                "title": self.strings["toolong"],
                "description": self.strings["retry"],
                "message": f"{self.ui.emoji('warn')} <b>{self.strings['toolong']}</b>",
            }

        token = await self.auth.ensure()
        if not token:
            token = await self.auth.ensure(force=True)
        if not token:
            return {"title": self.strings["auth_error"], "description": self.strings["retry"], "message": self.strings["auth_error"]}

        modules = await self.api.search(query, int(self.config["limit"]), token)
        if not modules:
            return {
                "title": self.strings["retry"],
                "description": self.strings["hint"],
                "message": f"{self.ui.emoji('error')} <b>{self.strings['notfound'].format(query=f'<code>{utils.escape_html(query)}</code>')}</b>",
            }

        results = []
        for index, data in enumerate(modules[:50]):
            description = str(data.get("description") or "")
            markup = None
            with suppress(Exception):
                markup = self.inline.generate_markup(self.ui.buttons(data, index, modules, query))
            results.append(InlineQueryResultArticle(
                id=f"vector_{uuid.uuid4().hex[:8]}_{index}",
                title=utils.escape_html(str(data.get("name", ""))),
                description=utils.escape_html(description[:250] + ("..." if len(description) > 250 else "")),
                input_message_content=InputTextMessageContent(
                    message_text=self._with_preview_link(self.ui.format(data, index + 1, len(modules)), data.get("banner")),
                    parse_mode="HTML",
                    link_preview_options=self._preview_options(data.get("banner")) or None,
                ),
                reply_markup=markup,
            ))
        await event.inline_query.answer(results, cache_time=0)

    @loader.command(
        ru_doc="(запрос) - поиск модулей в Vector.",
        en_doc="(query) - search modules in Vector.",
    )
    async def vectorcmd(self, message: Message) -> Any:
        """(query) - search modules in Vector."""
        query = utils.get_args_raw(message)
        if not query:
            return await utils.answer(message, f"{self.ui.emoji('error')} <b>{self.strings['noquery'].format(prefix=f'<code>{self.get_prefix()}')}</code></b>")
        if len(query) > 120:
            return await utils.answer(message, f"{self.ui.emoji('warn')} <b>{self.strings['toolong']}</b>")

        message = await utils.answer(message, f"{self.ui.emoji('search')} <b>{self.strings['search'].format(query=f'<code>{utils.escape_html(query)}</code>')}</b>")
        token = await self.auth.ensure()
        if not token:
            token = await self.auth.ensure(force=True)
        if not token:
            return await utils.answer(message, f"{self.ui.emoji('error')} <b>{self.strings['auth_error']}</b>")

        modules = await self.api.search(query, int(self.config["limit"]), token)
        if not modules:
            return await utils.answer(message, f"{self.ui.emoji('error')} <b>{self.strings['notfound'].format(query=f'<code>{utils.escape_html(query)}</code>')}</b>")

        data = modules[0]
        buttons = self.ui.buttons(data, 0, modules, query)
        form = await self.inline.form("ㅤ", message, reply_markup=buttons, silent=True)
        await self.edit(form, self.ui.format(data, 1, len(modules)), buttons, data.get("banner"))