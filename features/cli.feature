Scenario: No arguments shows help
    When I run "python src/app.py"
    Then the exit status should be 0
    And the output should contain "usage:"

Scenario: Greet command
    When I run "python src/app.py greet --name Alice"
    Then the exit status should be 0
    And the output should contain "Hello, Alice"
