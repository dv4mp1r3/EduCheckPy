# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') { }

When('I run {string}') do |cmd|
  cmd.gsub!('src/', '') # Пути скорректированы после копирования
  run_command_and_stop(cmd, exit_timeout: 15)
end

When('I run {string} with input:') do |cmd, input|
  cmd.gsub!('src/', '')
  run_command_and_stop(cmd, exit_timeout: 15) do |process|
    process.write(input)
  end
end