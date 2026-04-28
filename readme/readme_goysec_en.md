# GoySecurity — README EN

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-2CA5E0?logo=telegram&logoColor=white)](https://t.me/goymodules)

<p align='center'>[![Docs RU](https://img.shields.io/badge/RU-blue?logo=book)](./readme_ru.md) [![Docs EN](https://img.shields.io/badge/EN-blue?logo=book)](./readme_en.md) [![Src](https://img.shields.io/badge/SRC-blue?logo=book)](https://github.com/sepiol026-wq/GoyModules/blob/main/goysec.py) [![Raw](https://img.shields.io/badge/RAW-blue?logo=book)](https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/goysec.py)</p>


![GoySecurity Banner](../assets/goysec.png)

## What this module is
GoySecurity is a pre-install code scanner for third-party userbot modules. It helps reduce risk before execution and gives operators visibility into potential threats.

## How it works
- Runs static checks against risk signatures.
- Supports strictness modes.
- Stores scan history for review.
- Explains why a rule was triggered and supports whitelist management.

## Module file
- `goysec.py`

## Installation
```text
.dlm https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/goysec.py
```

## Core commands
- `.gscan` — scan a module/link.
- `.gautoscan` — enable autoscan before install.
- `.gmode` — set strictness mode.
- `.gwl` / `.gunwl` — whitelist management.
- `.ghist` / `.gwhy` — history and trigger reasons.
- `.gai` / `.gaicustom` — AI-assisted explanations.

## Navigation
- [Back to English index](./readme_en.md)
- [Русская версия](./readme_goysec_ru.md)

## License
This README and module are protected under **GNU AGPLv3**. Details: [LICENSE](../LICENSE).