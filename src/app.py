# src/app.py
#!/usr/bin/env python3
import argparse

def greet(args):
    """Печатает приветствие."""
    print(f"Hello, {args.name}")

def main():
    parser = argparse.ArgumentParser(prog="app.py")
    # Добавлено подчеркивание, чтобы избежать предупреждения W0612
    _subparsers = parser.add_subparsers(dest="command")

    # Команда greet
    _greet_parser = _subparsers.add_parser("greet", help="Greet someone")
    _greet_parser.add_argument(
        "--name", required=True, help="Name to greet"
    )

    args = parser.parse_args()
    if args.command == "greet":
        greet(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()