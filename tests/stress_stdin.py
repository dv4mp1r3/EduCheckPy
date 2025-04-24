import subprocess, random, string

def random_input(n=50):
    return ''.join(random.choices(string.ascii_letters + "\\n", k=n))

def test_random_stdin():
    for _ in range(50):
        inp = random_input()
        p = subprocess.Popen(
            ["python", "src/app.py", "echo"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )
        out, err = p.communicate(inp)
        assert p.returncode == 0

if __name__ == "__main__":
    test_random_stdin()
    print("Stdin stress tests passed")
