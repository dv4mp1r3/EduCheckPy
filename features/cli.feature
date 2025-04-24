Feature: CLI app behavior

  Background:
    Given a blank slate

  Scenario: Greet command
    When I run 'python src/app.py greet --name Alice'
    Then the exit status should be 0
    And the output should contain "Hello, Alice"

  Scenario: Sum command
    When I run 'python src/app.py sum 1 2 3.5'
    Then the exit status should be 0
    And the output should contain "6.5"

  Scenario: Echo command
    When I run 'python app.py echo' with input:
      """
      test
      Line
      """
    Then the output should contain "TEST\nLINE"
