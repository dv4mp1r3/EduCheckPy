import subprocess
import sys
import pytest
from hypothesis import given, strategies as st
import os

os.environ["PYTHONIOENCODING"] = "utf-8"

@pytest.mark.parametrize("numbers, expected", [
    (["1", "2", "3.5"], 6.5),
    (["0"], 0.0),
    (["-1", "1"], 0.0),
    (["100.5", "-50.25", "0.75"], 51.0),
    (["1e2", "2e2"], 300.0),
])
def test_sum_param(numbers, expected):
    """Явные кейсы: целые, дробные, отрицательные, экспоненциальные."""
    result = subprocess.run(
        ["python", "src/app.py", "sum", "--"] + numbers,
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert float(result.stdout.strip()) == pytest.approx(expected)

# Генерируем списки float длиной 1–10, значения в диапазоне ±1e6
@given(st.lists(st.floats(-1e6, 1e6, allow_nan=False, allow_infinity=False),
                 min_size=1, max_size=10))
def test_sum_hypothesis(numbers):
    """Property-based: случайные полож./отриц./дробные числа."""
    # Преобразуем числа в строки для CLI
    str_nums = [str(x) for x in numbers]
    expected = sum(numbers)
    result = subprocess.run(
        ["python", "src/app.py", "sum", "--"] + str_nums,
        capture_output=True, text=True
    )
    assert result.returncode == 0
    # сравниваем с допуском по относительной погрешности
    assert float(result.stdout.strip()) == pytest.approx(expected, rel=1e-6)



@pytest.mark.parametrize("input_text", [
    "",                             # пустая строка
    "simple line",                  # без переноса строки
    "Line1\nLine2\nLine3",          # несколько строк
    "12345",                        # цифры
    "!@#$%^&*()",                   # спецсимволы
    "Привет\nмир",                  # кириллица
    "Emoji 😊🚀\nTest",              # эмодзи и Unicode
])
def test_echo_param(input_text):
    """Echo uppercase для набора заранее выбранных строк."""
    result = subprocess.run(
        ["python", "src/app.py", "echo"],
        input=input_text, capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0
    assert result.stdout == input_text.upper()
    expected = input_text.upper().replace('\r', '\n')
    assert result.stdout == expected

# Генерируем произвольный текст длины 0–100, включая Unicode (кроме суррогатных пар)
text_strat = st.text(
    alphabet=st.characters(blacklist_categories=('Cs',)),
    min_size=0,
    max_size=100
)

@given(text_strat)
def test_echo_hypothesis(input_text):
    """Property-based: echo для случайных Unicode-строк."""
    result = subprocess.run(
        ["python", "src/app.py", "echo"],
        input=input_text, capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0
    expected = input_text.upper().replace('\r', '\n')
    assert result.stdout == expected





@pytest.mark.parametrize("name", [
    "Alice",
    "bob",
    "Ольга",         # кириллица
    "Émile",         # буквы с акцентом
    "A" * 50,        # очень длинное имя
    "Name With Space",
])
def test_greet_param(name):
    """Greet для разных имён, включая Unicode и пробелы."""
    result = subprocess.run(
        ["python", "src/app.py", "greet", "--name", name],
        capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0
    assert result.stdout.strip() == f"Hello, {name}"


def test_greet_missing_name():
    """Без --name argparse должен вернуть код 2 и показать help."""
    result = subprocess.run(
        ["python", "src/app.py", "greet"],
        capture_output=True, text=True, encoding="utf-8"
    )
    # argparse по умолчанию exit code 2 на ошибку парсинга
    assert result.returncode == 2
    assert "usage: app.py greet" in result.stderr