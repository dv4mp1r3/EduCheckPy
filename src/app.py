#!/usr/bin/env python3
import argparse
import sys
import statistics

def greet(args):
    print(f"Hello, {args.name}")

def cmd_sum(args):
    # суммирует переданные числа
    total = sum(args.numbers)
    print(total)

def cmd_echo(args):
    # читает stdin и выводит в upper-case
    data = sys.stdin.read()
    print(data.upper(), end="")

def main():
    parser = argparse.ArgumentParser(prog="app.py")
    sub = parser.add_subparsers(dest="command")

    # greet
    p1 = sub.add_parser("greet")
    p1.add_argument("--name", required=True)

    # sum
    p2 = sub.add_parser("sum")
    p2.add_argument("numbers", nargs="+", type=float,
                    help="Numbers to sum")
    p2.set_defaults(func=cmd_sum)

    # echo
    p3 = sub.add_parser("echo", help="Echo stdin uppercase")
    p3.set_defaults(func=cmd_echo)

    args = parser.parse_args()
    if args.command == "greet":
        greet(args)
    elif hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
