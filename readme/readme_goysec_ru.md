![GoySecurity Banner](../assets/goysec.png)

> Архив Heroku. Версия для Hotaru не портируется.

# GoySecurity — README RU

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=pull%20requests)](https://github.com/sepiol026-wq/GoyModules/pulls)
[![Commits](https://img.shields.io/github/commit-activity/t/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=commits)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![Last commit](https://img.shields.io/github/last-commit/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=last%20commit)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

[Главная](../README.md) · [Каталог](./readme_ru.md) · [English](./readme_goysec_en.md)

## Что это за модуль
GoySecurity — модуль предварительной проверки кода перед установкой сторонних модулей. Он снижает риск запуска подозрительных скриптов и помогает контролировать доверенные источники.

## Как это работает
- Выполняет скан кода по правилам риска.
- Поддерживает режимы строгости.
- Ведёт историю проверок.
- Даёт объяснение «почему риск» и поддерживает whitelist.

## Файл модуля
- `heroku/goysec.py`

## Установка
Скачай файл модуля и отправь его Hotaru, затем загрузи командой:
```text
.ld
```

## Основные команды
- `.gscan` — скан текущего модуля/ссылки.
- `.gautoscan` — автоскан перед установкой.
- `.gmode` — уровень строгости.
- `.gwl` / `.gunwl` — управление whitelist.
- `.ghist` / `.gwhy` — история и причины срабатывания.
- `.gai` / `.gaicustom` — AI-пояснения.

## Навигация
- [Root](../README.md)
- [Назад в русский индекс](./readme_ru.md)
- [English version](./readme_goysec_en.md)

## Лицензия
Этот README и модуль защищены лицензией **GNU AGPLv3**. Подробности: [LICENSE](../LICENSE).