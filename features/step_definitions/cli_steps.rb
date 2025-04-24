# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') { }

When('I run {string}') do |cmd|
  # Убираем обработку конвейера через shell
  cmd, input = cmd.split(' | ', 2)
  
  run_command_and_stop(cmd, exit_timeout: 15) do |process|
    process.write(input) if input
  end
end

Then('the output should contain {string}') do |expected|
  # Нормализуем вывод: удаляем ANSI-коды и лишние пробелы
  cleaned_output = last_command_started.output.gsub(/\e\[\d+m/, '').strip
  expect(cleaned_output).to include(expected)
end