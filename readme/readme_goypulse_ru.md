![GoyPulse Banner](../assets/goypulse.png)

# GoyPulse — README RU

[![Telegram](https://img.shields.io/badge/Telegram-@goymodules-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/goymodules)
[![Stars](https://img.shields.io/github/stars/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=stars)](https://github.com/sepiol026-wq/GoyModules/stargazers)
[![Forks](https://img.shields.io/github/forks/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=forks)](https://github.com/sepiol026-wq/GoyModules/forks)
[![Issues](https://img.shields.io/github/issues/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=issues)](https://github.com/sepiol026-wq/GoyModules/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/sepiol026-wq/GoyModules?style=for-the-badge&logo=github&label=pull%20requests)](https://github.com/sepiol026-wq/GoyModules/pulls)
[![Commits](https://img.shields.io/github/commit-activity/t/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=commits)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![Last commit](https://img.shields.io/github/last-commit/sepiol026-wq/GoyModules?style=for-the-badge&logo=git&label=last%20commit)](https://github.com/sepiol026-wq/GoyModules/commits/main)
[![License](https://img.shields.io/github/license/sepiol026-wq/GoyModules?style=for-the-badge&label=license)](https://github.com/sepiol026-wq/GoyModules/blob/main/LICENSE)

[Главная](../README.md) · [Каталог](./readme_ru.md) · [English](./readme_goypulse_en.md)

## Что это за модуль
GoyPulse — продвинутый нейро-автоответчик на основе цепей Маркова. Модуль учится на сообщениях, учитывает контекст чата, поддерживает скрытый режим и гибкую настройку ответов.

## Как это работает
1. Считывает историю и новые сообщения в чатах.
2. Обновляет языковую модель по локальной памяти.
3. Генерирует ответ с учётом настроек, ограничений и режима работы.
4. Работает как единый автоответчик без подсистем обновлений/бэкапов.

## Файл модуля
- `heroku/goypulse.py`

## Установка
Только архив Heroku. Модуль не портируется в Hotaru.
```text
.dlm https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/heroku/goypulse.py
```

## Основные команды
- `.gpulse on/off` — включение и отключение.
- `.gpref` — обновить память/рефреш.
- `.gpstat` — статус и статистика.
- `.gpinfo` — диагностика текущего чата.

## Рекомендованный старт
1. Загрузите модуль.
2. Включите `.gpulse on` в нужном чате.
3. Через время выполните `.gpref` для улучшения ответов.
4. При необходимости докрутите параметры через `.gpset`.

## Навигация
- [Root](../README.md)
- [Назад в русский индекс](./readme_ru.md)
- [English version](./readme_goypulse_en.md)

## Лицензия
Этот README и модуль защищены лицензией **GNU AGPLv3**. Подробности: [LICENSE](../LICENSE).
