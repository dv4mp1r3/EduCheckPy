import subprocess
import sys

def test_stress_sum():
    for i in range(1000):
        numbers = [str(j) for j in range(i % 10 + 1)]
        expected_sum = sum(map(float, numbers))
        result = subprocess.run(
            ["python", "src/app.py", "sum"] + numbers,
            capture_output=True, text=True
        )
        assert result.returncode == 0
        assert float(result.stdout.strip()) == expected_sum


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
