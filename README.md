# GoyModules

[![DOCS RU](https://img.shields.io/badge/DOCS-RU-2CA5E0?style=for-the-badge&logo=readthedocs&logoColor=white)](./readme/readme_ru.md)
[![DOCS EN](https://img.shields.io/badge/DOCS-EN-6f42c1?style=for-the-badge&logo=readthedocs&logoColor=white)](./readme/readme_en.md)
[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

<p align="center">
  <img src="./banner.png" alt="GoyModules Banner">
</p>

Модули для [Hotaru](https://github.com/HotaruProject/Hotaru) (`.hmod` в корне репозитория). Старые версии для Heroku лежат в [`heroku/`](./heroku/) и больше не обновляются.

## Структура

```text
.
├── *.hmod          модули Hotaru (актуальные)
├── heroku/         legacy-модули Heroku (архив)
├── readme/         документация RU/EN по каждому модулю
├── assets/         баннеры модулей
└── PORTING.md      правила портирования Heroku -> Hotaru
```

## Установка (Hotaru)

Скачай `.hmod` и отправь его своему юзерботу, затем загрузи:

```text
.ld
```

или укажи файл напрямую в команде загрузки. Управление модулями: `.mods`, `.ul <id>`, `.ex <id>`, `.config <id>`.

## Модули

| Модуль | Файл | Описание | Docs |
|---|---|---|---|
| OmniLoad | [`omni.hmod`](./omni.hmod) | Универсальный загрузчик медиа | [RU](./readme/readme_omniload_ru.md) · [EN](./readme/readme_omniload_en.md) |
| YTMusic | [`yt.hmod`](./yt.hmod) | YouTube Music: поиск, скачивание | [RU](./readme/readme_ytmusic_ru.md) · [EN](./readme/readme_ytmusic_en.md) |
| SoundCloud Music | [`sc.hmod`](./sc.hmod) | SoundCloud: поиск, скачивание | [RU](./readme/readme_soundcloudmusic_ru.md) · [EN](./readme/readme_soundcloudmusic_en.md) |
| GoyPulse | [`goypulse.hmod`](./goypulse.hmod) | Автоответчик на цепях Маркова | [RU](./readme/readme_goypulse_ru.md) · [EN](./readme/readme_goypulse_en.md) |
| GoySecurity | [`goysec.hmod`](./goysec.hmod) | Проверка модулей перед установкой | [RU](./readme/readme_goysec_ru.md) · [EN](./readme/readme_goysec_en.md) |
| KeyScanner | [`keyscanner.hmod`](./keyscanner.hmod) | Сканер ключей | [RU](./readme/readme_keyscanner_ru.md) · [EN](./readme/readme_keyscanner_en.md) |
| Recon | [`recon.hmod`](./recon.hmod) | Разведка по цели | [RU](./readme/readme_recon_ru.md) · [EN](./readme/readme_recon_en.md) |
| Iris | [`iris.hmod`](./iris.hmod) | Iris | |
| Vector | [`vector.hmod`](./vector.hmod) | Vector | |
| Doom | [`doom.hmod`](./doom.hmod) | DOOM в Telegram | [RU](./readme/readme_doom_ru.md) · [EN](./readme/readme_doom_en.md) |

### Только Heroku (архив)

| Модуль | Файл | Описание | Docs |
|---|---|---|---|
| RusRoul | [`heroku/rusroul.py`](./heroku/rusroul.py) | Русская рулетка | |
| GoyVirus | [`heroku/goyv.py`](./heroku/goyv.py) | GoyVirus | [RU](./readme/readme_goyvirus_ru.md) · [EN](./readme/readme_goyvirus_en.md) |
| CodexCLI | [`heroku/CodexCLI.py`](./heroku/CodexCLI.py) | Codex CLI | [RU](./readme/readme_codexcli_ru.md) · [EN](./readme/readme_codexcli_en.md) |
| QwenCLI | [`heroku/QwenCLI.py`](./heroku/QwenCLI.py) | Qwen CLI | [RU](./readme/readme_qwencli_ru.md) · [EN](./readme/readme_qwencli_en.md) |
| RedConstructor | [`heroku/RedConstructor.py`](./heroku/RedConstructor.py) | RedConstructor | |

## Лицензия

GNU AGPLv3. Автор: [@samsepi0l_ovf](https://t.me/samsepi0l_ovf). Канал: [@goymodules](https://t.me/goymodules).
