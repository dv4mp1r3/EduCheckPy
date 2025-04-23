Feature: CLI app behavior
  Проверяем базовое поведение командной строки

  Background:
    Given a blank slate

  Scenario: No arguments shows help
    When I run `python src/app.py`
    Then the output should contain "usage:"

  Scenario: Greet command
    When I run `python src/app.py greet --name Alice`
    Then the output should contain "Hello, Alice"
