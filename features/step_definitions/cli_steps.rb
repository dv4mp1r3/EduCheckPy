# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') { }

When('I run {string}') do |cmd|
  run_command_and_stop(cmd, exit_timeout: 10)  # встроенный запуск команды
end