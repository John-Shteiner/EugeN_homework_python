# Проект автоматизации тестирования с Allure

## Структура проекта

lesson_10/
├── pages/ # Page Object классы
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── conftest.py # Фикстуры для браузеров
├── calculator_page.py # Страница калькулятора
├── test_calculator.py # Тесты калькулятора
├── test_saucedemo.py # Тесты интернет-магазина
├── requirements.txt # Зависимости
├── allure-results/ # Результаты тестов (НЕ пушить!)
└── allure-report/ # HTML отчёт (НЕ пушить!)

## Установка зависимостей

```bash
pip install -r requirements.txt