# features/support/env.rb
require 'aruba/cucumber'
Aruba.configure do |config|
  config.exit_timeout = 10
end
Before { rebase(['src']) }
