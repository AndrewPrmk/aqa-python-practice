# AQA Python Practice

Учебный проект по автоматизированному тестированию на Python.

## Стек

- Python
- pytest

## Что реализовано

- функция валидации логина `validate_login`
- базовые автотесты
- тесты в стиле AAA
- параметризованные тесты
- тесты с pytest fixtures
- общие фикстуры в `conftest.py`
- маркировка тестов через pytest markers

## Структура проекта

```text
.
├── app/
│   ├── __init__.py
│   └── validators.py
├── tests/
│   ├── conftest.py
│   ├── test_login_validator.py
│   ├── test_login_validator_AAA.py
│   ├── test_login_validator_fixtures.py
│   └── test_login_validator_parametrize.py
├── pytest.ini
├── .gitignore
└── README.md
```

## Запуск тестов

Установить pytest:

```bash
pip install pytest
```

Запустить все тесты:

```bash
pytest
```

Запустить конкретный файл:

```bash
pytest tests/test_login_validator_fixtures.py
```

Запустить smoke-тесты:

```bash
pytest -m smoke
```

Запустить negative-тесты:

```bash
pytest -m negative
```

## Учебная цель

Проект создан для практики базовых навыков AQA:

- написание автотестов;
- использование `assert`;
- параметризация через `pytest.mark.parametrize`;
- работа с фикстурами;
- работа с `conftest.py`;
- запуск тестов по маркерам;
- структура теста AAA;
- чтение результатов запуска тестов.
