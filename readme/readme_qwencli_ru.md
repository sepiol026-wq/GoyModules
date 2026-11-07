![QwenCLI Banner](../assets/QwenCLI.png)

# QwenCLI — README RU

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=pull%20requests)](https://github.com/sepiol026-wq/GoyModules/pulls)
[![Commits](https://img.shields.io/github/commit-activity/t/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=commits)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![Last commit](https://img.shields.io/github/last-commit/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=last%20commit)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

[Главная](../README.md) · [Каталог](./readme_ru.md) · [English](./readme_qwencli_en.md)

## Что это за модуль
QwenCLI — это многофункциональный AI-модуль для Hikka и Heroku. Он объединяет рабочие чат-команды, автоматизацию и сценарии для повседневных задач: от ответов и генерации текста до утилитарных действий, которые обычно делают через внешний CLI.

## Как это работает
Модуль разворачивает внутренний слой команд и использует локальные/сетевые зависимости, которые устанавливаются один раз. После установки вы получаете единый интерфейс управления через префикс вашего юзербота.

## Файл модуля
- `heroku/QwenCLI.py` (архив Heroku)

## Установка
```text
.dlm https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/heroku/QwenCLI.py
```

## Первый запуск (важно)
Чтобы начать работу, пропишите:
```text
.qwinstall
```
Если у вас другой префикс, используйте его вместо точки (например, `!qwinstall`). Эта команда устанавливает нужные зависимости для Heroku или локального запуска и подготавливает модуль к полноценной работе.

## Базовые команды
- `.qwinstall` — установка/переустановка зависимостей.
- `.qwhelp` — список основных возможностей.
- `.qw*` — рабочая группа команд QwenCLI (конкретный набор смотрите через help внутри модуля).

## Практический сценарий
1. Установите модуль через `.dlm`.
2. Выполните `.qwinstall`.
3. Проверьте доступные команды через `.qwhelp`.
4. Используйте рабочие команды из блока `.qw*` в нужном чате.

## Навигация
- [Root](../README.md)
- [Назад в русский индекс](./readme_ru.md)
- [English version](./readme_qwencli_en.md)

## Лицензия
Этот README и модуль защищены лицензией **GNU AGPLv3**. Подробности: [LICENSE](../LICENSE).
