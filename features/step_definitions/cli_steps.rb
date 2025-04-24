# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') do
  # пусто — арена чиста, а src уже rebased
end

When('I run {string}') do |cmd|
  run_command_and_stop(cmd, exit_timeout: 10)
end

Then('the output should contain {string}') do |expected|
  expect(last_command_started.output).to include(expected)
end