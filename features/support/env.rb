# features/support/env.rb
require 'aruba/cucumber'

Aruba.configure do |config|
  config.working_directory = 'working_dir'  # Изолированная директория для тестов
  config.exit_timeout = 15
end

Before do
  # Копируем исходники в рабочую директорию Aruba
  FileUtils.cp_r('src/', File.join(aruba.config.working_directory, 'src'))
end

After do
  # Очистка временных файлов после каждого сценария
  all_commands.each(&:stop)
  FileUtils.rm_rf(aruba.config.working_directory)
end