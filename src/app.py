#!/usr/bin/env python3
import argparse

def greet(args):
    """Печатает приветствие."""
    print(f"Hello, {args.name}")


def main():
    parser = argparse.ArgumentParser(prog="app.py")
    subparsers = parser.add_subparsers(dest="command")

    # Команда greet
    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument(
        "--name", required=True, help="Name to greet"
    )

    args = parser.parse_args()
    if args.command == "greet":
        greet(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()