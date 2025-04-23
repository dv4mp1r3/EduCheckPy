Feature: CLI app behavior

  Scenario: No arguments shows help
    When I run `python src/app.py`
    Then the output should contain "usage:"

  Scenario: Known command works
    When I run `python src/app.py greet --name Alice`
    Then the output should contain "Hello, Alice"
