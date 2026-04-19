# OmniCLI — README RU

![OmniCLI Banner](../assets/omnicli.png)

OmniCLI — мульти-провайдерный AI-модуль на базе архитектуры QwenCLI, с новой группой команд `om*` и оркестрацией внешних CLI.

## Файл
- `OmniCLI.py`

## Установка
```bash
.dlm https://raw.githubusercontent.com/sepiol026-wq/GoyModules/main/OmniCLI.py
```

## Основные команды
- `.om` — основной запрос к ассистенту.
- `.ominstall [all|qwen|codex|gemini|claude]` — установка локального runtime и CLI-провайдеров.
- `.omauth [status|qwen|codex|gemini|claude|all]` — статус авторизации и гайды по входу.
- `.om*` — полный набор команд, зеркалирующий QwenCLI (`.omclear`, `.ommem*`, `.omauto`, `.omprod` и др.).

## Примечания
- Runtime-пайплайн Qwen сохранен полностью и перенесен в Omni namespace.
- В OmniCLI добавлены установщики/гайды авторизации внешних CLI для all-in-one сценария.
