![CodexCLI Banner](../assets/CodexCLI.png)

# CodexCLI — README EN

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=pull%20requests)](https://github.com/sepiol026-wq/GoyModules/pulls)
[![Commits](https://img.shields.io/github/commit-activity/t/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=commits)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![Last commit](https://img.shields.io/github/last-commit/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=last%20commit)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

[Home](../README.md) · [Catalog](./readme_en.md) · [Русский](./readme_codexcli_ru.md)

## What this module is
CodexCLI is an AI module for Hikka and Heroku focused on CLI automation, practical DevOps workflows, and in-chat control directly from Telegram.

## Origin and collaboration
- The module is a **fork of QwenCLI** adapted for Codex/OpenAI flows.
- It is developed collaboratively, with fork support and maintenance noted via Telegram: **[@justidev](https://t.me/justidev)**.

## How it works
The module exposes an internal command suite, supports Codex CLI authentication, and enables AI tasks, patch workflows, and utility actions through userbot commands.

## Module file
- `heroku/CodexCLI.py` (Heroku archive)

## Installation
```text
.dlm https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/heroku/CodexCLI.py
```

## First run (important)
To install dependencies and bootstrap runtime, run:
```text
.cdxinstall
```
If you use a custom prefix, replace `.` with your own (for example `!cdxinstall`).

## Core commands
- `.cdxinstall` — install/reinstall dependencies.
- `.cdxauth` — configure Codex authentication.
- `.cdxhelp` — show the command map.
- `.cdx*` — CodexCLI command family (see in-module help for exact commands).

## Typical workflow
1. Install with `.dlm`.
2. Run `.cdxinstall`.
3. Complete auth via `.cdxauth`.
4. Review features with `.cdxhelp` and use `.cdx*` commands.

## Navigation
- [Root](../README.md)
- [Back to English index](./readme_en.md)
- [Русская версия](./readme_codexcli_ru.md)

## License
This README and module are protected under **GNU AGPLv3**. Details: [LICENSE](../LICENSE).
