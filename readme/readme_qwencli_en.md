![QwenCLI Banner](../assets/QwenCLI.png)

# QwenCLI — README EN

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=pull%20requests)](https://github.com/sepiol026-wq/GoyModules/pulls)
[![Commits](https://img.shields.io/github/commit-activity/t/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=commits)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![Last commit](https://img.shields.io/github/last-commit/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=last%20commit)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

[Home](../README.md) · [Catalog](./readme_en.md) · [Русский](./readme_qwencli_ru.md)

## What this module is
QwenCLI is a multifunctional AI module for Hikka and Heroku. It provides a unified command layer for productivity tasks, chat-side automation, and assistant-style workflows.

## How it works
The module exposes an internal command suite and relies on dependencies that should be bootstrapped once. After bootstrap, you manage everything from your userbot prefix.

## Module file
- `heroku/QwenCLI.py` (Heroku archive)

## Installation
```text
.dlm https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/heroku/QwenCLI.py
```

## First run (important)
To initialize runtime dependencies, run:
```text
.qwinstall
```
If you use a custom prefix, replace `.` with your own (for example `!qwinstall`). This command installs the required packages into your environment and prepares the module for full operation.

## Core commands
- `.qwinstall` — install/reinstall dependencies.
- `.qwhelp` — show the command map.
- `.qw*` — QwenCLI working command group (see in-module help for the exact set).

## Typical workflow
1. Install with `.dlm`.
2. Execute `.qwinstall`.
3. Review features via `.qwhelp`.
4. Use the `.qw*` command family in your target chat.

## Navigation
- [Root](../README.md)
- [Back to English index](./readme_en.md)
- [Русская версия](./readme_qwencli_ru.md)

## License
This README and module are protected under **GNU AGPLv3**. Details: [LICENSE](../LICENSE).
