import subprocess, random, string

def random_input(length=100):
    return ''.join(random.choices(string.printable, k=length))

def test_random_stdin():
    for _ in range(50):
        inp = random_input()
        p = subprocess.Popen(
            ["python", "src/app.py", "greet", "--name", "Test"],
            stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True
        )
        p.communicate(inp)
        assert p.returncode == 0

if __name__ == "__main__":
    test_random_stdin()
    print("Stdin stress tests passed")
