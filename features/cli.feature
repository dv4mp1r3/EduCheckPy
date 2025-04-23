# language: ru
Feature: CLI app behavior
  Проверяем базовое поведение командной строки

  Scenario: No arguments shows help
    When I run `python src/app.py`
    Then the output should contain "usage:"

  Scenario: Greet command
    When I run `python src/app.py greet --name Alice`
    Then the output should contain "Hello, Alice"
