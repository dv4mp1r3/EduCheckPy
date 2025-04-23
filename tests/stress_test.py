import subprocess, random, string

def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def test_random_args():
    for _ in range(100):
        name = random_name()
        result = subprocess.run(
            ["python", "src/app.py", "greet", "--name", name],
            capture_output=True, text=True
        )
        assert result.returncode == 0

if __name__ == "__main__":
    test_random_args()
    print("Stress tests passed")
