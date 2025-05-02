import sys


def foo(n: int) -> int:
    return n * n


def main():
    sys.stdout.write("main function test message")
    assert foo(2) == 4, "correct assert"
    assert foo(3) == 6, "wrong assert"


if __name__ == "__main__":
    main()
