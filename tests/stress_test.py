import subprocess

def test_sum_direct():
    # прямой вызов subprocess
    result = subprocess.run(
        ["python", "src/app.py", "sum", "4", "5", "1"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "10.0"
