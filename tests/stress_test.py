import subprocess
import os
import sys

def test_sum_direct():
    # Абсолютный путь
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'app.py')
    result = subprocess.run(
        [sys.executable, app_path, "sum", "4", "5", "1"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "10.0"

def test_echo_command():
    input_text = "test\nLine"
    result = subprocess.run(
        ["python", "src/app.py", "echo"],
        input=input_text,
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "TEST\nLINE"

def test_greet_command():
    result = subprocess.run(
        ["python", "src/app.py", "greet", "--name", "Alice"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, Alice"
