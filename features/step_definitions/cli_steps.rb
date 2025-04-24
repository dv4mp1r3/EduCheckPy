# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') { }

When('I run {string}') do |cmd|
  # Заменяем printf на встроенный метод Aruba для ввода
  cmd.gsub!(/printf\s+"([^"]+)"/, 'echo -e "\1"')
  run_command_and_stop(cmd, exit_timeout: 15)
end

When('I run {string} with input:') do |cmd, input|
  run_command_and_stop(cmd.gsub('src/', ''), exit_timeout: 15) do |process|
    process.write(input)
  end
end