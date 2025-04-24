Given('a blank slate') do
    # Здесь можно добавить очистку или инициализацию окружения, если необходимо
  end
  
  When('I run {string}') do |command|
    run_command(command)
  end
  
  Then('the exit status should be {int}') do |status|
    expect(last_command_started).to have_exit_status(status)
  end
  
  Then('the output should contain {string}') do |expected_output|
    expect(last_command_started).to have_output(/#{Regexp.escape(expected_output)}/)
  end
  