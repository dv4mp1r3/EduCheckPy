import sys
# comment


def do_something_with_int_var(int_value: int) -> int:
    return int_value * int_value


def main():
    sys.stdout.write("main function test message")
    assert do_something_with_int_var(2) == 4, "correct assert"
    assert do_something_with_int_var(3) == 6, "wrong assert"


if __name__ == "__main__":
    main()
