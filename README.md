# Sprint_5 - Автотесты для Stellar Burgers

## Описание
Автотесты для сервиса Stellar Burgers (космический фастфуд). Проект написан на Python с использованием Selenium и pytest.

## Технологии
- Python 3.14
- Selenium 4.15.2
- pytest 7.4.3
- Faker 20.1.0

## Установка и запуск
1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать: `source venv/Scripts/activate` (Windows Git Bash) или `venv\Scripts\activate` (Windows CMD)
4. Установить зависимости: `pip install -r requirements.txt`
5. Запустить тесты: `pytest -v`

## Структура проекта
- `pages/` - Page Object Model для страниц
- `tests/` - Тесты по функциональности
- `helpers/` - Вспомогательные функции (генераторы данных)
- `conftest.py` - Фикстуры для браузеров
- `config.py` - Конфигурация (BASE_URL)

## Тестируемый функционал
- Регистрация (успешная и с ошибкой)
- Вход (4 способа)
- Личный кабинет (переходы, выход)
- Конструктор (переключение разделов)