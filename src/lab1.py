"""
function for n*n calc
"""
import sys


def do_something_with_int_var(int_value: int) -> int:
    """
    result function

    :param: int_value: value
    """
    return int_value * int_value


def main():
    """
    lab EP
    """
    sys.stdout.write("main function test message")
    assert do_something_with_int_var(2) == 4, "correct assert"
    assert do_something_with_int_var(3) == 6, "wrong assert"


if __name__ == "__main__":
    main()
