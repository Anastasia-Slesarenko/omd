# Homework 4
## issue-01
Для запуска тестирования функции `encode()` с использованием `doctest` выполните в консоли следующую команду:

```
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```

По умолчанию пробелы в ожидаемом и фактическом выводе должны точно совпадать. Флаг `NORMALIZE_WHITESPACE` позволяет игнорировать разное количество пробелов. Это полезно, когда строка ожидаемого результата длинная, и вы хотите перенести ее на другую строчку.

Пример команд и результатов тестирования представлен в файле `results_issue_01.txt`.

## issue-02
Тесты на функцию `decode()` с использованием `pytest` написаны в файле `test_decode.py`. Для запуска тестирования функции выполните в консоли следующую команду:

```
python -m pytest -v test_decode.py
```

Требуется предварительная установка, если пакет `pytest` не был установлен ранее: ` python -m pip install pytest`

Пример команд и результатов тестирования представлен в файле `results_issue_02.txt`.

## issue-03
Тесты на функцию `fit_transform()` с использованием `unittest` написаны в файле `test_fit_transform_unit.py`. Для запуска тестирования выполните в консоли следующую команду:

```
python -m unittest test_fit_transform_unit.py
```

Пример команд и результатов тестирования представлен в файле `results_issue_03.txt`.

## issue-04
Тесты на функцию `fit_transform()` с использованием `pytest` написаны в файле `test_fit_transform_pytest.py`. Для запуска тестирования выполните в консоли следующую команду:

```
python -m pytest -v test_fit_transform_pytest.py
```

Требуется предварительная установка, если пакет `pytest` не был установлен ранее: ` python -m pip install pytest`

Пример команд и результатов тестирования представлен в файле `results_issue_04.txt`.

## issue-05
Тесты на функцию `what_is_year_now()` с использованием `unittest` написаны в файле `test_what_is_year_now.py`. Для запуска тестирования выполните в консоли следующую команду:

```
python -m unittest test_what_is_year_now.py
```

Если хотите проверить покрытие кода тестами, предворительно установите `coverage` с помощью команды `python -m pip install coverage` и выполните в консоли следующие команды:
```
python -m coverage run -m unittest test_what_is_year_now.py
python -m coverage report
```
Чтобы сгенерировать отчет о покрытии в формате HTML, выполните следующую команду:

```
python -m coverage html
```

Пример отчета можно посмотреть в html файлах в папке htmlcov.
Пример команд и результатов тестирования представлен в файле `results_issue_05.txt`.