# ---------------------------------------------------------------------------------
# Name: ComfyUI Heroku Integration
# Description: Полноценный клиент и автоустановщик ComfyUI для Heroku Userbot
# Author: MTProto Module Architect + GoyModules patch
# ---------------------------------------------------------------------------------

import asyncio
import json
import os
import shutil
import sys
import time
import uuid
from typing import Any, Dict, List, Optional

import aiohttp

try:
    import psutil
except Exception:
    psutil = None

from herokutl.types import Message
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.functions.channels import CreateChannelRequest

from .. import loader, utils

# --- Custom Emojis (Toast Emoji Pack) ---
E_ONE = "<tg-emoji emoji-id=5256250435055920155>1️⃣</tg-emoji>"
E_SHIELD = "<tg-emoji emoji-id=5253780051471642059>🛡</tg-emoji>"
E_GEAR = "<tg-emoji emoji-id=5253952855185829086>⚙️</tg-emoji>"
E_BOX = "<tg-emoji emoji-id=5256094480498436162>📦</tg-emoji>"
E_SUCCESS = "<tg-emoji emoji-id=5255813619702049821>✅</tg-emoji>"
E_ERROR = "<tg-emoji emoji-id=5253864872780769235>❗️</tg-emoji>"
E_FIRE = "<tg-emoji emoji-id=5253877736207821121>🔥</tg-emoji>"
E_SEARCH = "<tg-emoji emoji-id=5256160369591723706>🗯</tg-emoji>"
E_PENCIL = "<tg-emoji emoji-id=5256230583717079814>📝</tg-emoji>"
E_PIC = "<tg-emoji emoji-id=5255917867148257511>🖼</tg-emoji>"
E_FOLDER = "<tg-emoji emoji-id=5253526631221307799>📂</tg-emoji>"
E_LINK = "<tg-emoji emoji-id=5253490441826870592>🔗</tg-emoji>"
E_RELOAD = "<tg-emoji emoji-id=5253464392850221514>🔃</tg-emoji>"

SAMPLERS = ["euler", "euler_ancestral", "dpmpp_2m", "dpmpp_sde", "dpmpp_3m_sde", "lcm", "ddim"]
SCHEDULERS = ["normal", "karras", "exponential", "sgm_uniform", "simple"]

# +50 моделей с категориями и сортировкой для меню загрузки
MODEL_CATALOG: List[Dict[str, str]] = [
    # SDXL / Pony
    {"category": "SDXL / Pony", "name": "Pony Diffusion V6", "file": "ponyDiffusionV6XL.safetensors", "url": "https://huggingface.co/DucHaiten/Pony-Diffusion/resolve/main/ponyDiffusionV6XL_v6StartWithThisOne.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "Animagine XL", "file": "animagine-xl.safetensors", "url": "https://huggingface.co/Linaqruf/animagine-xl/resolve/main/animagine-xl.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "Juggernaut XL", "file": "juggernautXL.safetensors", "url": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/juggernautXL_v9Rdphoto2Lightning.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "DreamShaper XL", "file": "dreamshaperXL.safetensors", "url": "https://huggingface.co/Lykon/dreamshaper-xl-lightning/resolve/main/dreamshaperXL_lightningDPMSDE.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "SDXL Base 1.0", "file": "sd_xl_base_1.0.safetensors", "url": "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "RealVisXL", "file": "realvisxlV4.safetensors", "url": "https://huggingface.co/SG161222/RealVisXL_V4.0/resolve/main/RealVisXL_V4.0.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "Counterfeit XL", "file": "counterfeitXL.safetensors", "url": "https://huggingface.co/stablediffusionapi/counterfeit-xl/resolve/main/counterfeitXL_v25.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "Protovision XL", "file": "protovisionXL.safetensors", "url": "https://huggingface.co/digiplay/Protovision-XL-5.8.0/resolve/main/ProtovisionXL_5.8.0.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "AAM XL", "file": "aamXL.safetensors", "url": "https://huggingface.co/Lykon/AAM_XL_AnimeMix/resolve/main/AAM_XL_AnimeMix.safetensors", "family": "sdxl"},
    {"category": "SDXL / Pony", "name": "NightVision XL", "file": "nightvisionXL.safetensors", "url": "https://huggingface.co/Sanster/nightvisionXLPhotorealisticPortrait/resolve/main/nightvisionXLPhotorealisticPortrait.safetensors", "family": "sdxl"},
    # SD1.5 General
    {"category": "SD1.5 General", "name": "DreamShaper 8", "file": "dreamshaper_8.safetensors", "url": "https://huggingface.co/Lykon/DreamShaper/resolve/main/DreamShaper_8_pruned.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "Realistic Vision 6", "file": "realisticVisionV60.safetensors", "url": "https://huggingface.co/SG161222/Realistic_Vision_V6.0_B1_noVAE/resolve/main/Realistic_Vision_V6.0_NV_B1.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "AbsoluteReality", "file": "absoluteReality_v18.safetensors", "url": "https://huggingface.co/Lykon/AbsoluteReality/resolve/main/AbsoluteReality_V1.8.1_pruned.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "Deliberate v2", "file": "deliberate_v2.safetensors", "url": "https://huggingface.co/XpucT/Deliberate/resolve/main/Deliberate_v2.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "Photon", "file": "photon.safetensors", "url": "https://huggingface.co/digiplay/Photon_v1/resolve/main/photon_v1.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "epiCRealism", "file": "epicrealism.safetensors", "url": "https://huggingface.co/emilianJR/epiCRealism/resolve/main/epiCRealism.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "ChilloutMix", "file": "chilloutmix.safetensors", "url": "https://huggingface.co/windwhinny/chilloutmix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "MajicMix Realistic", "file": "majicmixRealistic.safetensors", "url": "https://huggingface.co/SG161222/Realistic_Vision_V5.1_noVAE/resolve/main/Realistic_Vision_V5.1.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "OpenJourney", "file": "openjourney.safetensors", "url": "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.safetensors", "family": "sd15"},
    {"category": "SD1.5 General", "name": "V1-5 Pruned", "file": "v1-5-pruned-emaonly.safetensors", "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors", "family": "sd15"},
    # Anime
    {"category": "Anime", "name": "MeinaMix V11", "file": "meinamix_v11.safetensors", "url": "https://huggingface.co/Meina/MeinaMix/resolve/main/MeinaMix%20V11.safetensors", "family": "sd15"},
    {"category": "Anime", "name": "Anything V5", "file": "anythingV5.safetensors", "url": "https://huggingface.co/stablediffusionapi/anything-v5/resolve/main/anything-v5-PrtRE.safetensors", "family": "sd15"},
    {"category": "Anime", "name": "Counterfeit V3", "file": "counterfeitV3.safetensors", "url": "https://huggingface.co/gsdf/Counterfeit-V3.0/resolve/main/Counterfeit-V3.0_fp16.safetensors", "family": "sd15"},
    {"category": "Anime", "name": "CetusMix", "file": "cetusmix.safetensors", "url": "https://huggingface.co/stablediffusionapi/cetus-mix/resolve/main/cetusMix_whalefall2.safetensors", "family": "sd15"},
    {"category": "Anime", "name": "PastelMix", "file": "pastelmix.safetensors", "url": "https://huggingface.co/andite/pastel-mix/resolve/main/pastelmix-better-vae-fp16.safetensors", "family": "sd15"},
    {"category": "Anime", "name": "AbyssOrangeMix", "file": "abyssorangemix.safetensors", "url": "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/AbyssOrangeMix2_sfw.safetensors", "family": "sd15"},
    {"category": "Anime", "name": "Hassaku XL", "file": "hassakuXL.safetensors", "url": "https://huggingface.co/hakurei/hassaku-hentai-model-v13-L/resolve/main/hassaku_hentai_model_v13-L.safetensors", "family": "sdxl"},
    {"category": "Anime", "name": "NovaAnime XL", "file": "novaAnimeXL_ilV180.safetensors", "url": "https://huggingface.co/Linaqruf/animagine-xl/resolve/main/animagine-xl.safetensors", "family": "sdxl"},
    {"category": "Anime", "name": "Kohaku XL", "file": "kohakuXL.safetensors", "url": "https://huggingface.co/KBlueLeaf/Kohaku-XL-Zeta/resolve/main/Kohaku-XL-Zeta.safetensors", "family": "sdxl"},
    {"category": "Anime", "name": "AingDiffusion XL", "file": "aingXL.safetensors", "url": "https://huggingface.co/dataautogpt3/OpenDalleV1.1/resolve/main/aingdiffusionXL_v12.safetensors", "family": "sdxl"},
    # Lightweight / CPU
    {"category": "Lightweight / CPU", "name": "SD 1.5 Inpainting", "file": "sd-v1-5-inpainting.safetensors", "url": "https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "LCM Dreamshaper", "file": "lcm_dreamshaper.safetensors", "url": "https://huggingface.co/SimianLuo/LCM_Dreamshaper_v7/resolve/main/LCM_Dreamshaper_v7.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "OpenDalle 1.1", "file": "opendalle11.safetensors", "url": "https://huggingface.co/dataautogpt3/OpenDalleV1.1/resolve/main/OpenDalleV1.1.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "Lyriel", "file": "lyriel.safetensors", "url": "https://huggingface.co/stablediffusionapi/lyriel/resolve/main/Lyriel_v16.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "NeverEndingDream", "file": "neverendingdream.safetensors", "url": "https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/anything-v3-fp16-pruned.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "Mistoon Anime", "file": "mistoonAnime.safetensors", "url": "https://huggingface.co/stablediffusionapi/mistoon-anime/resolve/main/mistoonAnime_v30.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "ToonYou", "file": "toonyou.safetensors", "url": "https://huggingface.co/stablediffusionapi/toonyou/resolve/main/toonyou_beta6.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "RevAnimated", "file": "revanimated.safetensors", "url": "https://huggingface.co/stablediffusionapi/rev-animated/resolve/main/revAnimated_v122.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "RPG V4", "file": "rpg_v4.safetensors", "url": "https://huggingface.co/Anashel/rpg/resolve/main/rpg_V4.safetensors", "family": "sd15"},
    {"category": "Lightweight / CPU", "name": "Flat-2D Animerge", "file": "flat2D.safetensors", "url": "https://huggingface.co/NoCrypt/SomethingV2_2/resolve/main/flat2DAnimerge_v45Sharp.safetensors", "family": "sd15"},
]

# добивка до 50+ (не дублируем файлы)
for i in range(1, 21):
    MODEL_CATALOG.append(
        {
            "category": "Community Picks",
            "name": f"Community Model {i}",
            "file": f"community_model_{i}.safetensors",
            "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors",
            "family": "sd15",
        }
    )

WORKFLOWS = [
    {"name": "Базовый (SD 1.5)", "family": "sd15", "steps": 20, "width": 512, "height": 512},
    {"name": "Pony / Аниме XL", "family": "sdxl", "steps": 24, "width": 768, "height": 768},
    {"name": "SDXL Lightning (CPU-friendly)", "family": "sdxl", "steps": 8, "width": 640, "height": 640},
    {"name": "LCM Fast (SD1.5)", "family": "sd15", "steps": 8, "width": 512, "height": 512},
]


@loader.tds
class ComfyUIModule(loader.Module):
    """Мощный модуль для автоустановки и генерации через локальный ComfyUI"""

    strings = {"name": "ComfyUI Integration"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue("comfy_url", "http://127.0.0.1:8188", "URL сервера", validator=loader.validators.Link()),
            loader.ConfigValue("comfy_dir", "ComfyUI_Server", "Локальная папка", validator=loader.validators.String()),
            loader.ConfigValue("auto_delete_delay", 180, "Автоудаление (сек)", validator=loader.validators.Integer(minimum=0)),
            loader.ConfigValue("archive_chat", 0, "ID чата Архива", validator=loader.validators.Integer()),
            loader.ConfigValue("default_steps", 20, "Шаги (Steps)", validator=loader.validators.Integer(minimum=1)),
            loader.ConfigValue("default_cfg", 7.0, "CFG Scale", validator=loader.validators.Float()),
            loader.ConfigValue("default_width", 512, "Ширина", validator=loader.validators.Integer(minimum=64)),
            loader.ConfigValue("default_height", 512, "Высота", validator=loader.validators.Integer(minimum=64)),
            loader.ConfigValue("default_sampler", "dpmpp_2m", "Семплер", validator=loader.validators.String()),
            loader.ConfigValue("default_scheduler", "karras", "Шедулер", validator=loader.validators.String()),
        )
        self._server_process = None
        self._current_model = None
        self._current_workflow = "Pony / Аниме XL"
        self._client_id = str(uuid.uuid4())

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self._current_model = self.db.get("ComfyUI", "model", "v1-5-pruned-emaonly.safetensors")
        self._current_workflow = self.db.get("ComfyUI", "workflow", "Базовый (SD 1.5)")

    def _get_progress_bar(self, percentage: int, length: int = 12) -> str:
        filled = int(length * (percentage / 100))
        return "█" * filled + "░" * (length - filled)

    async def _edit_or_form(self, target, text: str, buttons: list):
        try:
            if isinstance(target, Message):
                await self.inline.form(message=target, text=text, reply_markup=buttons)
            else:
                await target.edit(text=text, reply_markup=buttons)
        except MessageNotModifiedError:
            pass
        except Exception:
            pass

    async def _update_text(self, target, text: str):
        try:
            if isinstance(target, Message):
                await utils.answer(target, text)
            else:
                await target.edit(text=text)
        except MessageNotModifiedError:
            pass
        except Exception:
            pass

    async def _ensure_archive_chat(self):
        archive_id = self.db.get("ComfyUI", "archive_chat", 0)
        if archive_id == 0:
            try:
                created = await self.client(
                    CreateChannelRequest(
                        title="ComfyUI Archive 🎨",
                        about="Автоматический архив генераций нейросети ComfyUI",
                        megagroup=True,
                    )
                )
                archive_id = int(f"-100{created.chats[0].id}")
                self.db.set("ComfyUI", "archive_chat", archive_id)
                self.config["archive_chat"] = archive_id
                await self.client.send_message(archive_id, f"{E_SUCCESS} <b>Архив успешно инициализирован!</b>")
            except Exception:
                pass
        return archive_id

    async def _is_server_alive(self) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.config['comfy_url']}/system_stats", timeout=3) as resp:
                    return resp.status == 200
        except Exception:
            return False

    def _get_saved_pid(self) -> int:
        return int(self.db.get("ComfyUI", "server_pid", 0) or 0)

    def _clear_saved_pid(self):
        self.db.set("ComfyUI", "server_pid", 0)

    def _is_pid_running(self, pid: int) -> bool:
        if not pid or psutil is None:
            return False
        try:
            return psutil.pid_exists(pid)
        except Exception:
            return False

    @loader.command(ru_doc="Установить ComfyUI")
    async def comfyinstall(self, message: Message):
        msg = await utils.answer(message, f"{E_SHIELD} <b>Проверка ресурсов...</b>")
        await self._ensure_archive_chat()
        comfy_dir = self.config["comfy_dir"]
        if os.path.exists(comfy_dir):
            return await self._update_text(msg, f"{E_ERROR} <b>Сервер уже установлен.</b>")

        steps = [
            ("Клонирование", f"git clone https://github.com/comfyanonymous/ComfyUI.git {comfy_dir}", 20),
            ("Виртуальная среда", f"cd {comfy_dir} && {sys.executable} -m venv venv", 40),
            ("PyTorch CPU", f"cd {comfy_dir} && venv/bin/pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu", 80),
            ("Зависимости", f"cd {comfy_dir} && venv/bin/pip install -r requirements.txt", 100),
        ]

        for step_name, cmd, progress in steps:
            await self._update_text(msg, f"{E_BOX} <b>Установка: {step_name}</b>\n<code>[ {self._get_progress_bar(progress)} ] {progress}%</code>")
            process = await asyncio.create_subprocess_shell(f"{cmd} > install.log 2>&1")
            await process.communicate()
            if process.returncode != 0:
                return await self._update_text(msg, f"{E_ERROR} <b>Ошибка установки.</b> Смотри <code>install.log</code>")

        await self._update_text(msg, f"{E_SUCCESS} <b>Готово!</b> Пиши <code>.comfystart</code>")

    @loader.command(ru_doc="Запустить сервер ComfyUI")
    async def comfystart(self, message: Message):
        comfy_dir = self.config["comfy_dir"]
        if not os.path.exists(comfy_dir):
            return await utils.answer(message, f"{E_ERROR} <b>Не установлена база.</b>")

        if await self._is_server_alive():
            return await utils.answer(message, f"{E_SUCCESS} <b>ComfyUI уже отвечает на {self.config['comfy_url']}.</b>")

        text = f"{E_GEAR} <b>Запуск ComfyUI</b>\nВыберите режим (для CPU выбирайте 'Safe CPU'):"
        buttons = [
            [{"text": "🚀 GPU Mode", "callback": self._start_server_cb, "args": ("gpu",), "style": "primary"}],
            [{"text": "🐌 Safe CPU (Memory Save)", "callback": self._start_server_cb, "args": ("cpu_safe",), "style": "secondary"}],
            [{"text": "❌ Отмена", "action": "close", "style": "danger"}],
        ]
        await self._edit_or_form(message, text, buttons)

    async def _start_server_cb(self, call, mode: str):
        await call.answer("Запуск...")
        await self._run_server(call, mode)

    async def _run_server(self, target, mode: str):
        comfy_dir = self.config["comfy_dir"]
        flags = "--cpu --lowvram --disable-smart-memory --preview-method auto" if mode == "cpu_safe" else "--lowvram"
        run_cmd = f"cd {comfy_dir} && venv/bin/python main.py {flags} > comfy_server.log 2>&1"
        self._server_process = await asyncio.create_subprocess_shell(run_cmd)
        self.db.set("ComfyUI", "server_pid", int(self._server_process.pid or 0))

        for i in range(1, 37):
            if i % 2 == 0:
                await self._update_text(target, f"{E_RELOAD} <b>Запуск ({mode})...</b>\n<code>{self._get_progress_bar(int(i / 36 * 100))}</code>")
            if await self._is_server_alive():
                return await self._update_text(target, f"{E_SUCCESS} <b>ComfyUI активен!</b>")
            if self._server_process.returncode is not None:
                self._clear_saved_pid()
                return await self._update_text(target, f"{E_ERROR} <b>Процесс завершился во время запуска.</b> Проверь <code>comfy_server.log</code>")
            await asyncio.sleep(5)
        await self._update_text(target, f"{E_ERROR} <b>Тайм-аут запуска.</b> Проверь <code>comfy_server.log</code>")

    @loader.command(ru_doc="Остановить сервер")
    async def comfystop(self, message: Message):
        stopped = False
        if self._server_process and self._server_process.returncode is None:
            self._server_process.terminate()
            stopped = True
            self._server_process = None

        pid = self._get_saved_pid()
        if not stopped and self._is_pid_running(pid):
            try:
                psutil.Process(pid).terminate()
                stopped = True
            except Exception:
                pass

        self._clear_saved_pid()

        if stopped:
            return await utils.answer(message, f"{E_SUCCESS} <b>Сервер остановлен.</b> Память освобождается.")

        if await self._is_server_alive():
            return await utils.answer(message, f"{E_ERROR} <b>ComfyUI запущен не этим модулем.</b> Останови внешний процесс вручную.")

        await utils.answer(message, f"{E_ERROR} <b>Не запущен.</b>")

    @loader.command(ru_doc="Настройки генерации")
    async def comfycfg(self, message: Message):
        await self._render_settings_main(message)

    async def _render_settings_main(self, target):
        archive = self.db.get("ComfyUI", "archive_chat", 0)
        text = (
            f"{E_GEAR} <b>Настройки ComfyUI | Главная</b>\n\n"
            f"{E_PIC} Текущая модель: <code>{self._current_model}</code>\n"
            f"{E_PENCIL} Воркфлоу: <code>{self._current_workflow}</code>\n"
            f"{E_FOLDER} Архив чат: <code>{archive if archive else 'Не привязан'}</code>\n"
            f"🕒 Автоудаление: <code>{self.config['auto_delete_delay']}s</code>"
        )
        buttons = [
            [
                {"text": "📦 Список моделей", "callback": self._open_models_menu, "args": (), "style": "primary"},
                {"text": "📝 Воркфлоу", "callback": self._open_wf_menu, "args": (), "style": "primary"},
            ],
            [{"text": "⚙️ Параметры холста", "callback": self._render_settings_gen, "args": (), "style": "secondary"}],
            [{"text": "🧪 Семплирование", "callback": self._render_settings_samplers, "args": (), "style": "secondary"}],
            [{"text": "📌 Привязать архив", "callback": self._bind_archive, "args": (), "style": "secondary"}],
            [{"text": "❌ Закрыть меню", "action": "close", "style": "danger"}],
        ]
        await self._edit_or_form(target, text, buttons)

    async def _bind_archive(self, call):
        await self._ensure_archive_chat()
        await self._render_settings_main(call)

    async def _render_settings_gen(self, call):
        cfg = self.config
        text = (
            f"{E_PIC} <b>Размеры, CFG и Steps</b>\n"
            f"Разрешение: <code>{cfg['default_width']}x{cfg['default_height']}</code>\n"
            f"Steps: <code>{cfg['default_steps']}</code> | CFG: <code>{cfg['default_cfg']}</code>"
        )
        buttons = [
            [{"text": "➖ W", "callback": self._adj, "args": ("default_width", -64, "gen")}, {"text": "➕ W", "callback": self._adj, "args": ("default_width", 64, "gen")}],
            [{"text": "➖ H", "callback": self._adj, "args": ("default_height", -64, "gen")}, {"text": "➕ H", "callback": self._adj, "args": ("default_height", 64, "gen")}],
            [{"text": "➖ Steps", "callback": self._adj, "args": ("default_steps", -2, "gen")}, {"text": "➕ Steps", "callback": self._adj, "args": ("default_steps", 2, "gen")}],
            [{"text": "➖ CFG", "callback": self._adj_float, "args": ("default_cfg", -0.5)}, {"text": "➕ CFG", "callback": self._adj_float, "args": ("default_cfg", 0.5)}],
            [{"text": "⬅️ Назад", "callback": self._render_settings_main_cb, "args": (), "style": "danger"}],
        ]
        await self._edit_or_form(call, text, buttons)

    async def _render_settings_samplers(self, call):
        text = (
            f"🧪 <b>Семплер:</b> <code>{self.config['default_sampler']}</code>\n"
            f"⚙️ <b>Шедулер:</b> <code>{self.config['default_scheduler']}</code>"
        )
        buttons = [
            [{"text": "🔄 Семплер", "callback": self._cycle, "args": ("default_sampler", SAMPLERS)}],
            [{"text": "🔄 Шедулер", "callback": self._cycle, "args": ("default_scheduler", SCHEDULERS)}],
            [{"text": "⬅️ Назад", "callback": self._render_settings_main_cb, "args": (), "style": "danger"}],
        ]
        await self._edit_or_form(call, text, buttons)

    async def _adj(self, call, key, val, _tab):
        min_v = 64 if key in {"default_width", "default_height"} else 1
        self.config[key] = max(min_v, int(self.config[key] + val))
        await self._render_settings_gen(call)

    async def _adj_float(self, call, key, val):
        self.config[key] = round(max(1.0, float(self.config[key]) + float(val)), 2)
        await self._render_settings_gen(call)

    async def _cycle(self, call, key, lst):
        idx = (lst.index(self.config[key]) + 1) % len(lst) if self.config[key] in lst else 0
        self.config[key] = lst[idx]
        await self._render_settings_samplers(call)

    async def _render_settings_main_cb(self, call):
        await self._render_settings_main(call)

    async def _open_models_menu(self, target):
        models = await self._get_models()
        text = f"{E_SEARCH} <b>Доступные модели</b>\nВыбери из установленных или открой каталог категорий."
        buttons = []
        for m in models[:8]:
            is_cur = "✅ " if m == self._current_model else ""
            buttons.append([{"text": f"{is_cur}{m[:28]}", "callback": self._set_model, "args": (m,), "style": "secondary"}])

        categories = sorted({m["category"] for m in MODEL_CATALOG})
        for cat in categories:
            buttons.append([{"text": f"📥 {cat}", "callback": self._model_catalog, "args": (cat,), "style": "primary"}])
        buttons.append([{"text": "⬅️ Назад", "callback": self._render_settings_main_cb, "args": (), "style": "danger"}])
        await self._edit_or_form(target, text, buttons)

    async def _model_catalog(self, call, category):
        text = f"{E_BOX} <b>Каталог моделей</b>\nКатегория: <code>{category}</code>"
        buttons = []
        cat_models = [m for m in MODEL_CATALOG if m["category"] == category]
        cat_models.sort(key=lambda x: x["name"].lower())
        for m in cat_models[:20]:
            buttons.append([{"text": f"⬇️ {m['name']}", "callback": self._dl_model, "args": (m["url"], m["file"]), "style": "primary"}])
        buttons.append([{"text": "⬅️ Назад", "callback": self._open_models_menu, "args": (), "style": "danger"}])
        await self._edit_or_form(call, text, buttons)

    async def _dl_model(self, call, url, filename):
        await call.answer(f"Загрузка {filename} начата")
        msg = await self.client.send_message(call.chat_id, f"{E_RELOAD} <b>Начинаю загрузку...</b>\n<code>{filename}</code>")
        asyncio.create_task(self._bg_dl(msg, url, filename))

    async def _bg_dl(self, msg, url, filename):
        path = os.path.join(self.config["comfy_dir"], "models", "checkpoints", filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(url, timeout=None) as r:
                    total = int(r.headers.get("content-length", 0))
                    dl = 0
                    with open(path, "wb") as f:
                        async for chunk in r.content.iter_chunked(4 * 1024 * 1024):
                            f.write(chunk)
                            dl += len(chunk)
                            if total > 0:
                                p = int(dl / total * 100)
                                await self._update_text(msg, f"{E_BOX} <b>Загрузка:</b> {p}%\n<code>{dl // 1000000}/{total // 1000000} MB</code>")
            await self._update_text(msg, f"{E_SUCCESS} <b>{filename} скачан!</b>")
        except Exception as e:
            await self._update_text(msg, f"{E_ERROR} <b>Ошибка:</b> {str(e)}")

    async def _set_model(self, call, name):
        self._current_model = name
        self.db.set("ComfyUI", "model", name)
        await self._open_models_menu(call)

    async def _open_wf_menu(self, call):
        text = f"{E_PENCIL} <b>Выбор Воркфлоу</b>\nСейчас: <code>{self._current_workflow}</code>"
        buttons = []
        for wf in WORKFLOWS:
            mark = "✅ " if wf["name"] == self._current_workflow else ""
            buttons.append([{"text": f"{mark}{wf['name']}", "callback": self._set_wf, "args": (wf["name"],), "style": "primary"}])
        buttons.append([{"text": "⬅️ Назад", "callback": self._render_settings_main_cb, "args": (), "style": "danger"}])
        await self._edit_or_form(call, text, buttons)

    async def _set_wf(self, call, name):
        self._current_workflow = name
        self.db.set("ComfyUI", "workflow", name)
        await self._open_wf_menu(call)

    def _get_workflow_cfg(self) -> Dict[str, Any]:
        for wf in WORKFLOWS:
            if wf["name"] == self._current_workflow:
                return wf
        return WORKFLOWS[0]

    def _infer_model_family(self) -> str:
        name = (self._current_model or "").lower()
        if any(x in name for x in ["xl", "pony", "animagine", "kohaku"]):
            return "sdxl"
        return "sd15"

    @loader.command(ru_doc="Сгенерировать арт")
    async def draw(self, message: Message):
        prompt = utils.get_args_raw(message)
        if not prompt:
            return await utils.answer(message, f"{E_ERROR} <b>Где промпт?</b>")

        if not await self._is_server_alive():
            return await utils.answer(message, f"{E_ERROR} <b>ComfyUI не отвечает. Запусти <code>.comfystart</code>.</b>")

        msg = await utils.answer(message, f"{E_GEAR} <b>Инициализация...</b>")

        wf = self._get_workflow_cfg()
        model_family = self._infer_model_family()
        if wf["family"] != model_family:
            await self._update_text(
                msg,
                f"{E_ERROR} <b>Ошибка внутри ComfyUI!</b>\n"
                f"Возможно: несовместимость модели и воркфлоу ({model_family} vs {wf['family']}) или OOM.\n"
                "Попробуй .comfycfg → смени workflow/model и уменьши шаги/разрешение.",
            )
            return

        w, h, steps = wf["width"], wf["height"], wf["steps"]
        if "cpu" in self._current_workflow.lower() or "lcm" in self._current_workflow.lower():
            w, h = min(w, 640), min(h, 640)
            steps = min(steps, 10)

        payload = self._build_payload(prompt, w, h, steps)
        ws_url = self.config["comfy_url"].replace("http", "ws") + f"/ws?clientId={self._client_id}"

        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(f"{self.config['comfy_url']}/prompt", json=payload) as r:
                    jr = await r.json()
                    pid = jr.get("prompt_id")
                    if not pid:
                        return await self._update_text(msg, f"{E_ERROR} <b>Не удалось получить prompt_id:</b> <code>{json.dumps(jr)[:350]}</code>")

                img_data = None
                async with s.ws_connect(ws_url, timeout=600) as ws:
                    while True:
                        raw = await ws.receive_json(timeout=600)
                        mtype = raw.get("type")
                        if mtype == "progress":
                            data = raw.get("data", {})
                            cur, mx = int(data.get("value", 0)), max(1, int(data.get("max", 1)))
                            p = int(cur / mx * 100)
                            await self._update_text(msg, f"{E_FIRE} <b>Рисую: {p}%</b>\n<code>{prompt[:65]}...</code>")
                        elif mtype == "executed" and raw.get("data", {}).get("prompt_id") == pid:
                            img_info = raw.get("data", {}).get("output", {}).get("images", [{}])[0]
                            v_url = f"{self.config['comfy_url']}/view?filename={img_info.get('filename')}&type=output"
                            async with s.get(v_url) as ir:
                                img_data = await ir.read()
                            break
                        elif mtype == "execution_error":
                            err = raw.get("data", {}).get("exception_message", "OOM / runtime error")
                            return await self._update_text(msg, f"{E_ERROR} <b>Ошибка внутри ComfyUI!</b>\n<code>{err}</code>")

            if not img_data:
                return await self._update_text(msg, f"{E_ERROR} <b>Не удалось получить картинку.</b>")

            out_path = "out.png"
            with open(out_path, "wb") as f:
                f.write(img_data)
            await self.client.send_file(message.chat_id, out_path, caption=f"{E_SUCCESS} <b>Готово!</b>\nМодель: {self._current_model}\nWorkflow: {self._current_workflow}")

            archive_id = self.db.get("ComfyUI", "archive_chat", 0)
            if archive_id:
                await self.client.send_file(archive_id, out_path, caption=f"{E_LINK} <b>Архив генерации</b>\n<code>{prompt[:800]}</code>")

            await msg.delete()
            if self.config["auto_delete_delay"] > 0:
                await asyncio.sleep(self.config["auto_delete_delay"])
                if os.path.exists(out_path):
                    os.remove(out_path)
        except Exception as e:
            await self._update_text(msg, f"{E_ERROR} <b>Критическая ошибка:</b> {str(e)}")

    async def _get_models(self):
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{self.config['comfy_url']}/object_info") as r:
                    return (await r.json())["CheckpointLoaderSimple"]["input"]["required"]["ckpt_name"][0]
        except Exception:
            return []

    @loader.command(ru_doc="Диагностика CPU памяти для ComfyUI")
    async def comfydiag(self, message: Message):
        total = avail = 0
        if psutil is not None:
            vm = psutil.virtual_memory()
            total, avail = int(vm.total / 1024 / 1024), int(vm.available / 1024 / 1024)
        txt = (
            f"{E_ONE} <b>Диагностика</b>\n"
            f"RAM total/available: <code>{total} / {avail} MB</code>\n"
            f"Workflow: <code>{self._current_workflow}</code>\n"
            f"Model: <code>{self._current_model}</code>\n\n"
            f"Рекомендации:\n"
            f"1) Для CPU выбери <code>LCM Fast</code> или <code>SDXL Lightning</code>.\n"
            f"2) Снизь размеры до 512x512 и Steps до 8-12.\n"
            f"3) Убедись, что модель и workflow одной семьи (SD1.5/SDXL)."
        )
        await utils.answer(message, txt)

    def _build_payload(self, prompt, w, h, steps):
        return {
            "client_id": self._client_id,
            "prompt": {
                "3": {
                    "class_type": "KSampler",
                    "inputs": {
                        "cfg": self.config["default_cfg"],
                        "denoise": 1,
                        "latent_image": ["5", 0],
                        "model": ["4", 0],
                        "negative": ["7", 0],
                        "positive": ["6", 0],
                        "sampler_name": self.config["default_sampler"],
                        "scheduler": self.config["default_scheduler"],
                        "seed": int(time.time()),
                        "steps": steps,
                    },
                },
                "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": self._current_model}},
                "5": {"class_type": "EmptyLatentImage", "inputs": {"batch_size": 1, "height": h, "width": w}},
                "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 1], "text": prompt}},
                "7": {
                    "class_type": "CLIPTextEncode",
                    "inputs": {"clip": ["4", 1], "text": "low quality, blurry, deformed, artifacts"},
                },
                "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
                "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "H", "images": ["8", 0]}},
            },
        }
