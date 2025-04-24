import subprocess, random, string, time

def random_input():
    # случайная длина от 0 до 500
    length = random.randint(0, 500)
    # буквы, цифры, пробел, перевод строки, спецсимволы
    chars = string.ascii_letters + string.digits + " \n!@#€"
    return ''.join(random.choices(chars, k=length))

def test_random_stdin():
    times = []
    for i in range(200):
        inp = random_input()
        start = time.time()
        p = subprocess.Popen(
            ["python", "src/app.py", "echo"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = p.communicate(inp, timeout=5)
        duration = time.time() - start
        times.append(duration)

        # 1) программа не упала
        assert p.returncode == 0, f"Non-zero exit on iteration {i}"
        # 2) вывод корректный (uppercase)
        assert out == inp.upper(), f"Output mismatch on iteration {i}"
        # 3) не слишком медленно
        assert duration < 0.1, f"Slow response ({duration}s) on iteration {i}"

    # опционально: проверьте, что 95-й процентиль времени < 0.05s
    times.sort()
    p95 = times[int(0.95 * len(times))]
    assert p95 < 0.05, f"95th percentile too slow: {p95}s"

if __name__ == "__main__":
    test_random_stdin()
    print("Stdin stress tests passed")
