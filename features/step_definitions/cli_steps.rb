# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') { }

When('I run {string}') do |cmd|
  cmd.gsub!(/printf\s+"([^"]+)"/, 'echo -e "\1"')
   run_command_and_stop(cmd, exit_timeout: 15)
end

# ↓ новый шаг для обработки "with input:"
When('I run {string} with input:') do |cmd, doc_string|
  write_file('stdin.txt', doc_string)
  # оборачиваем вызов в shell, где < действительно работает
  run_command_and_stop("sh -c \"#{cmd} < stdin.txt\"", exit_timeout: 15)
end