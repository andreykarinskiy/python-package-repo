# cursor-minipkg

Минималистичный пример Python-библиотеки с современным `src`-layout, автоматическими проверками и сценарием публикации в GitHub Packages.

## Стек и требования

- Python 3.9+
- Hatchling в качестве backend сборки
- Pytest, Ruff, Mypy для локальных проверок (по желанию)

## Установка в editable-режиме

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Запуск тестов и статических проверок

```bash
pytest
ruff check src tests
mypy src
```

## Сборка пакета

```bash
python -m build
```

## Публикация в GitHub Packages

1. Создайте персональный токен (PAT) с правами `write:packages` и `read:packages`.
2. Добавьте в настройках репозитория секрет `GH_PACKAGES_TOKEN`.
3. Создайте релиз в GitHub (`git tag` + `git push --tags` или через UI).
4. GitHub Actions автоматически соберёт и опубликует релизный артефакт в GitHub Packages.

Дополнительно можно установить пакет из GitHub Packages, добавив в `~/.config/pip/pip.conf`:

```ini
[global]
index-url = https://pip.pkg.github.com/OWNER/
extra-index-url = https://pypi.org/simple
```

Замените `OWNER` на имя вашей организации или пользователя. После этого пакет можно установить командой:

```bash
pip install cursor-minipkg
```
