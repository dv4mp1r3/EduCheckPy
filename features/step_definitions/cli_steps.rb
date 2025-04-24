# features/step_definitions/cli_steps.rb
require 'aruba/cucumber'

Given('a blank slate') do
  # ничего не делаем — aruba автоматически чистит рабочую директорию
end

When('I run {string}') do |cmd|
  # запускаем команду и ждём её завершения
  run_command_and_stop(cmd, exit_timeout: 10)
end

Then('the exit status should be {int}') do |status|
  # проверяем код выхода последней команды
  expect(last_command_started.exit_status).to eq(status)
end

Then('the output should contain {string}') do |expected|
  # проверяем, что stdout содержит нужную подстроку
  expect(last_command_started.output).to include(expected)
end
