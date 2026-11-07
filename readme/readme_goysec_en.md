![GoySecurity Banner](../assets/goysec.png)

> Heroku archive. This module is not being ported to Hotaru.

# GoySecurity — README EN

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=pull%20requests)](https://github.com/sepiol026-wq/GoyModules/pulls)
[![Commits](https://img.shields.io/github/commit-activity/t/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=commits)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![Last commit](https://img.shields.io/github/last-commit/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=last%20commit)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

[Home](../README.md) · [Catalog](./readme_en.md) · [Русский](./readme_goysec_ru.md)

## What this module is
GoySecurity is a pre-install code scanner for third-party userbot modules. It helps reduce risk before execution and gives operators visibility into potential threats.

## How it works
- Runs static checks against risk signatures.
- Supports strictness modes.
- Stores scan history for review.
- Explains why a rule was triggered and supports whitelist management.

## Module file
- `heroku/goysec.py`

## Installation
Download the module file, send it to Hotaru, then load it with:
```text
.ld
```

## Core commands
- `.gscan` — scan a module/link.
- `.gautoscan` — enable autoscan before install.
- `.gmode` — set strictness mode.
- `.gwl` / `.gunwl` — whitelist management.
- `.ghist` / `.gwhy` — history and trigger reasons.
- `.gai` / `.gaicustom` — AI-assisted explanations.

## Navigation
- [Root](../README.md)
- [Back to English index](./readme_en.md)
- [Русская версия](./readme_goysec_ru.md)

## License
This README and module are protected under **GNU AGPLv3**. Details: [LICENSE](../LICENSE).