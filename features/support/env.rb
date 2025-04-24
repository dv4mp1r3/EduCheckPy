require 'aruba/cucumber'

Aruba.configure do |config|
  # вместо tmp/aruba — current directory (где лежит src/)
  config.working_directory = '.'
  config.exit_timeout = 10
end

Before do
  setup_aruba
end
