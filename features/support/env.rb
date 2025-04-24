# features/support/env.rb
require 'aruba/cucumber'

Aruba.configure do |config|
  # timeout для команд, сек.
  config.exit_timeout = 10
end

Before do
  # Подготовить aruba: очистить tmp, перейти в корень проекта
  setup_aruba
end
