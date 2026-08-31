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

## Структура проекта

```text
.
├── main.py
├── test_login_validator.py
├── test_login_validator_AAA.py
├── test_login_validator_fixtures.py
├── test_login_validator_parametrize.py
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
pytest test_login_validator_fixtures.py
```

## Учебная цель

Проект создан для практики базовых навыков AQA:

- написание автотестов;
- использование `assert`;
- параметризация через `pytest.mark.parametrize`;
- работа с фикстурами;
- структура теста AAA;
- чтение результатов запуска тестов.