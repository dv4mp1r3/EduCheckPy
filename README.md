# Автоматическая проверка CLI-приложения на Python

В этом репозитории реализован CI для проверки учебных работ на языке Python в командной строке.

## Структура

- `src/app.py` — пример CLI‑приложения с командой `greet`.
- `features/` — BDD‑тесты (Cucumber + Aruba).
- `tests/stress_test.py` — скрипт стресс‑тестирования.
- `requirements.txt` — зависимости Python.
- `.pylintrc` — конфиг для Pylint.
- `.github/workflows/ci.yml` — GitHub Actions pipeline.

## Локальный запуск

```bash
# Установить Python‑зависимости
pip install -r requirements.txt

# Запустить линтинг
pylint src

# Запустить BDD‑тесты
gem install cucumber aruba
cucumber

# Запустить стресс‑тесты
python tests/stress_test.py