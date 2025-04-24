# features/support/env.rb
require 'aruba/cucumber'

Aruba.configure do |config|
  config.working_directory = 'working_dir'  # Изолированная директория для тестов
  config.exit_timeout = 15
  config.activate_announcer = :always      # Включить отладку
end

Before do
  # Копируем исходники в рабочую директорию Aruba
  FileUtils.cp_r('src/', File.join(aruba.config.working_directory, 'src'))
end