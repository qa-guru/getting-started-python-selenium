# Автотесты: Python + Pytest + Selenium + Selene

Практический старт для новичков: установим инструменты, запустим первый тест, разберём полезные ключи `pytest` и предложим базовую структуру проекта (с папкой `pages/` для Page Object).

> Требования: **Python 3.11+**. ОС: Windows 10/11, macOS 12+, Ubuntu 22.04+.

---

## Содержание

- [Установка Python](#установка-python)
- [Установка PyCharm](#установка-pycharm)
- [Создание проекта и venv](#создание-проекта-и-venv)
- [Установка Git](#установка-git)
- [Установка всех пакетов](#установка-всех-пакетов)
- [Запуск первого теста](#запуск-первого-теста)
- [Запуск первого теста с разными ключами](#запуск-первого-теста-с-разными-ключами)

---

## Установка Python

**Проверка наличия:**

```bash
python --version
# или
python3 --version
```

**Windows**

1. Скачайте Python 3.11+ с официального сайта.
2. В инсталляторе поставьте галочку **“Add Python to PATH”**.
3. Проверьте:

```powershell
python --version
pip --version
```

**macOS / Linux**
Часто Python уже есть. Если нет — установите из менеджера пакетов или с сайта Python.

```bash
python3 --version
python3 -m pip --version
```

---

## Установка PyCharm

1. Скачайте **PyCharm Community**.
2. В настройках выберите интерпретатор Python (из установленного Python или из виртуального окружения проекта).
3. Опционально включите предпросмотр Markdown и автосохранение.

---

## Создание проекта и venv

```bash
# macOS/Linux
mkdir qa-project && cd qa-project
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

# Windows PowerShell
mkdir qa-project; cd qa-project
python -m venv .venv
. .\.venv\Scripts\activate
python -m pip install --upgrade pip
```
---

## Установка Git

**Проверка:**

```bash
git --version
```

**Установка:**

* Windows: установите Git for Windows (Git Bash или PowerShell).
* macOS: `xcode-select --install` или установщик Git.
* Linux (Ubuntu): `sudo apt-get install git`.

**Быстрая настройка:**

```bash
git config --global user.name "Ваше Имя"
git config --global user.email "you@example.com"
```

---

## Установка всех пакетов

Создайте `requirements.txt` в корне проекта:

```
pytest
selenium
webdriver-manager
```

Установите всё разом:

```bash
pip install -r requirements.txt
```

---

## Запуск первого теста

Структура проекта (минимум):

```
qa-project/
  .venv/
  tests/
    test_python_org_wait.py
  requirements.txt
  README.md
```

Запуск тестов:

```bash
pytest -q
```

## Запуск первого теста с разными ключами

**Базовые:**

```bash
pytest          # стандартный вывод
pytest -v       # подробные имена тестов
pytest -q       # тихий режим
```

**Отбор тестов:**

```bash
pytest tests/test_python_org_wait.py   # один файл
pytest tests -k search                 # по подстроке в имени
pytest -k "not e2e"                    # исключить
```

**Маркеры:**

```python
import pytest

@pytest.mark.e2e
def test_something():
    ...
```

Запуск по маркеру:

```bash
pytest -m e2e
```

**Поведение при падениях и отчёты:**

```bash
pytest -x            # стоп на первом фейле
pytest --maxfail=1   # то же
pytest -ra           # причины skip/xfail
pytest -s            # показать print()/stdout
```

**Параллельный запуск (опционально):**

```bash
pip install pytest-xdist
pytest -n auto
```
