# Heroku → Hotaru porting rules (GoyModules)

Source: heroku/<Name>.py (Heroku loader.Module). Output: <id>.hmod in repo root.
Full API reference: /tmp/fresh_skill.md (read sections 4, 6, 8, 9 + capability table).
Live example of a correct .hmod: /root/Hotaru/indusblock.hmod (read it fully first).

## Hard rules
1. `HOTARU = {...}` MUST be the first executable statement (line 1). No comments, no imports before it. Meta comments (# meta banner:, # meta developer:) and license header go AFTER the HOTARU dict... actually no: put them at the very bottom or drop them; the AST parser rejects anything before HOTARU. Keep license text as a lexicon-free trailing comment block or module docstring AFTER HOTARU.
2. Do NOT add any new comments to ported code. Preserve existing comments from the source where the corresponding code survives.
3. No type annotations (project style for user-facing .hmod).
4. All user strings → HOTARU["lexicon"] with supported languages: en, ru, uk (from strings_ua), ja (from strings_jp), kz, zh if present in source. Fun locales (de/leet/neofit/tiktok/uwu) are dropped — Hotaru lexicon supports only the six codes above; custom-language files are not portable. Access via ctx.t("<id>.key", "<fallback>", **params) — ALWAYS pass the English string as default fallback (indusblock `_t` helper pattern; copy that helper).
5. Handlers are module-level functions, not class methods:
   - command "cdx" → `async def command_cdx(ctx, invocation)` or `async def command_cdx(ctx)` (both signatures supported; pick per need for invocation.raw_args/args/message).
   - watcher → `async def watcher_<name>(ctx)` listed in HOTARU["watchers"].
   - task → `async def task_<name>(ctx)` + HOTARU["tasks"] {name: {"interval": N, "autostart": bool}}.
   - rise/fade hooks: `"rise": "on_startup"` → `async def on_startup(ctx)`; same for "fade".
6. HOTARU["commands"] maps command name → handler function name string, e.g. {"cdx": "command_cdx"}.

## API translation table
| Heroku | Hotaru |
|---|---|
| self.strings["k"] / self._t | ctx.t("<id>.k", "<english default>", **fmt) |
| utils.answer(message, text) | await ctx.respond(text, parse_mode="HTML") (edits own msg automatically) |
| message.edit(text) | await ctx.edit(text, parse_mode="HTML") |
| message.delete() | await ctx.delete() |
| utils.get_args_raw(message) | invocation.raw_args (str) |
| utils.get_args(message) | invocation.args (list) |
| message.chat_id / message.peer_id | ctx.chat_id / ctx.peer_id |
| message.sender_id | ctx.sender_id |
| message.out | ctx.message.out |
| self.db.get(key, default) | ctx.state.get(key, default)  — SYNC in indusblock, but skill says await; follow indusblock: `ctx.state.get(...)` returns JSON-roundtrip value, normalize bools (`is True or == "true"`) |
| self.db.set(key, value) | ctx.state.set(key, value) |
| self.client(SomeRequest(**kw)) | await ctx.tg.call("namespace.someMethod", {kwargs}) + capability "mt" |
| message.client / self._client | await ctx.tg.call(...) + "mt" |
| download_media / download_file | await ctx.download(ctx.reply_attachment or ctx.attachment) |
| aiohttp/requests/urllib HTTP | await ctx.net(url, method=..., headers=..., json=..., data=..., timeout=...) + capability "net". Sandbox has NO raw network (CLONE_NEWNET) — every direct socket/aiohttp/urllib call MUST become ctx.net. |
| subprocess / asyncio.create_subprocess_* | capability "shell"; shell runs in workspace jail — keep logic, use ctx.shell where available, note honestly in final report if a CLI binary (codex/qwen/ffmpeg) cannot exist in the sandbox |
| sqlite3 direct | ctx.state (per-module SQLite is provided); large structured data → JSON values in ctx.state |
| self.inline.form(text, reply_markup=...) / InlineCall | await ctx.respond(text, buttons=[[...]], parse_mode="HTML"); buttons via ctx.ui.danger/success/primary closures `async def cb(call, payload)` → call.edit(...); or ctx.screens.show(title, body, buttons) |
| loader.ConfigValue(name, default, doc, validator) | HOTARU["config_schema"] {name: {"type": "str/int/bool/float/choice", "default": d, "description": doc, ...}}; read via ctx.config.get(name, default) (dict, sync) |
| @loader.watcher(...) | HOTARU["watchers"] + async def watcher_<name>(ctx) |
| client_ready / on_unload | "rise" / "fade" hooks |
| self.lookup("other") | HOTARU["requires"] / cross-module: drop or reimplement via state — report honestly |
| utils.escape_html | ctx.html.escape(...) (no capability needed) |
| __version__ = (1,0,1) | HOTARU["version"] = "1.0.1" |
| @loader.command / *cmd suffix | HOTARU["commands"] key = command name without cmd suffix; lexicon "commands": {name: {"description": ...}} per locale from *_doc kwargs |
| banner (# meta banner:) | HOTARU["banner"] = url |

## Capabilities: declare ONLY what is used
- [] : messaging, 292 ctx.* MTProto helpers, screens/ui, html, t, logs
- "state" : ctx.state (almost every module needs it)
- "net" : ctx.net/ctx.stream
- "shell" : subprocess
- "mt" : ONLY raw ctx.tg.call
- "files" : ctx.files workspace IO
- "inline" : external inline-bot gateway

## Destructive RPCs (account.deleteAccount etc.) are firewalled by Hotaru relay — port the call as ctx.tg.call anyway ONLY if the module's purpose survives; if the whole module is destructive-by-design, skip it (rusroul already excluded by owner).

## Version/ids
- id = snake_case module name matching output filename <id>.hmod (e.g. CodexCLI.py → codexcli.hmod, keyscanner.py → keyscanner.hmod, goysec.py → goysec.hmod, RedConstructor.py → redconstructor.hmod).
- Keep source version if present, else "1.0.0".

## Verification (mandatory before done)
For each output .hmod run:
```
python3 - <<'EOF'
import ast
src = open("<file>.hmod").read()
tree = ast.parse(src)
first = next(n for n in tree.body if not isinstance(n, (ast.Expr,)) or True)
assert isinstance(tree.body[0], ast.Assign) and getattr(tree.body[0].targets[0], "id", "") == "HOTARU", "HOTARU not first statement"
print("OK")
EOF
python3 -c "import ast; ast.parse(open('<file>.hmod').read())" && echo SYNTAX_OK
```
Both must pass for every ported module.
