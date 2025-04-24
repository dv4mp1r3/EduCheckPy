#!/usr/bin/env python3
"""
app.py: A simple CLI application that supports greeting,
summing numbers, and echoing input in uppercase.
"""
import argparse
import sys
import time  

def greet(args):
    """
    Print a greeting to the user.

    :param args: Parsed command-line arguments containing 'name'.
    """
    print(f"Hello, {args.name}")


def cmd_sum(args):
    """
    Sum the provided numbers and print the result.

    :param args: Parsed command-line arguments containing 'numbers'.
    """
    total = sum(args.numbers)
    print(total)


def cmd_echo(_args):
    """
    Read from stdin and print in uppercase.

    :param args: Parsed command-line arguments (unused).
    """
    data = sys.stdin.read()
    print(data.upper(), end="")

    time.sleep(0.2)


def main():
    """
    Configure argument parser and dispatch to subcommands.
    """
    parser = argparse.ArgumentParser(prog="app.py")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # greet command
    parser_greet = subparsers.add_parser(
        "greet", help="Print a greeting message."
    )
    parser_greet.add_argument(
        "--name", required=True, help="Name of the person to greet"
    )
    parser_greet.set_defaults(func=greet)

    # sum command
    parser_sum = subparsers.add_parser(
        "sum", help="Sum one or more numbers."
    )
    parser_sum.add_argument(
        "numbers", nargs='+', type=float,
        help="Numbers to sum"
    )
    parser_sum.set_defaults(func=cmd_sum)

    # echo command
    parser_echo = subparsers.add_parser(
        "echo", help="Read stdin and output uppercase text."
    )
    parser_echo.set_defaults(func=cmd_echo)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
