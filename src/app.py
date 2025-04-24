#!/usr/bin/env python3
import argparse, sys, time, ctypes  # (A) лишний импорт ctypes для Valgrind-мутации и time для задержки

 import os  # (A) ОШИБКА: bad-indentation (Pylint W0311) 

def greet(args):
    # (B) опечатка “Helo” вместо “Hello” — сломает BDD-тест “Greet command” 
    print(f"Helo, {args.name}")

def cmd_sum(args):
    # (C1) off-by-one: вычитаем 1 — сломает unit-тест test_sum_direct и BDD “Sum command” :contentReference[oaicite:0]{index=0}
    total = sum(args.numbers) - 1  
    # (C2) invalid read через ctypes → сломает Valgrind-шаг (invalid read of size 1) :contentReference[oaicite:1]{index=1}
    ctypes.string_at(0)  
    print(total)

def cmd_echo(args):
    # (D1) сломает BDD-тест “Echo command” и стресс-stdin: если есть перевод строки, выходим с ошибкой 
    data = sys.stdin.read()
    if "\n" in data:
        sys.exit(1)  
    # (D2) без .upper() — тоже сломает BDD-тест, но sys.exit уже отработает раньше
    print(data, end="")

def main():
    parser = argparse.ArgumentParser(prog="app.py")
    _subparsers = parser.add_subparsers(dest="command")

    p1 = _subparsers.add_parser("greet")
    p1.add_argument("--name", required=True)

    p2 = _subparsers.add_parser("sum")
    p2.add_argument("numbers", nargs="+", type=float)
    p2.set_defaults(func=cmd_sum)

    p3 = _subparsers.add_parser("echo")
    p3.set_defaults(func=cmd_echo)

    args = parser.parse_args()

    # (E) искусственная задержка 20 сек — сломает time-profiling (real > timeout) 
    time.sleep(20)

    if args.command == "greet":
        greet(args)
    elif hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
