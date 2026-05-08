# Akatai-Nurdaulet — Анализ CSV данных

Проект содержит 6 задач для анализа данных в CSV-файле. Каждая задача в отдельном файле с собственным классом.

---

## Общая структура

Все файлы используют похожую структуру:
1. **Импорт библиотек** — загружаем инструменты для работы
2. **Создание класса** — у каждой задачи свой класс
3. **Конструктор `__init__`** — инициализация и загрузка данных
4. **Метод `load_data()`** — чтение CSV-файла
5. **Вспомогательные методы** — обработка данных
6. **Метод `run()`** — запуск основной логики
7. **Блок `if __name__ == "__main__"`** — автоматический запуск

---

## Task 9: Число строк и числовые колонки

**Цель**: подсчитать строки, найти числовые колонки и вычислить суммы.

### Построчное объяснение (`task9.py`)

```python
import csv
```
Импортируем модуль `csv` — это встроенная библиотека Python для чтения CSV-файлов.

```python
class Task9:
```
Создаём класс `Task9`. Класс — это шаблон для создания объектов, который объединяет данные и методы вместе.

```python
def __init__(self, file_name="data.csv"):
    self.file_name = file_name  # имя CSV-файла
```
Метод `__init__` — конструктор, вызывается при создании объекта. Сохраняем имя файла в переменную `self.file_name`.

```python
    self.rows = []  # список строк из файла
```
Создаём пустой список `self.rows`, где будем хранить все строки из CSV.

```python
    self.cols = []  # список названий колонок
```
Создаём пустой список `self.cols` для названий колонок (заголовков).

```python
    self.load_data()  # читаем данные сразу при создании
```
Вызываем метод `load_data()` прямо в конструкторе, чтобы данные загрузились автоматически.

```python
def load_data(self):
    with open(self.file_name, newline="", encoding="utf-8") as f:
```
Открываем файл в режиме чтения. `with` — специальная конструкция, которая автоматически закроет файл даже при ошибке. `newline=""` нужна для правильной работы с CSV. `encoding="utf-8"` — кодировка для русских букв.

```python
        reader = csv.DictReader(f)
```
`DictReader` читает CSV и преобразует каждую строку в словарь (как таблица, где ключи — это имена колонок).

```python
        self.cols = reader.fieldnames or []
```
Сохраняем имена колонок. `or []` — если их нет, используем пустой список.

```python
        for row in reader:
            self.rows.append(row)
```
Цикл по всем строкам. Каждую строку добавляем в список `self.rows`. `append()` — метод для добавления элемента в список.

```python
def is_number(self, text):
    try:
        float(text)
        return True
    except:
        return False
```
Проверяем, можно ли текст преобразовать в число. `try/except` — пробуем выполнить операцию, если ошибка — возвращаем `False`. `float()` преобразует строку в число.

```python
def numeric_columns(self):
    numeric = []
```
Начинаем собирать список числовых колонок.

```python
    for col in self.cols:
        is_num = True
```
Для каждой колонки предположим, что она числовая.

```python
        for row in self.rows:
            value = row[col].strip()
```
Для каждой строки берём значение колонки. `.strip()` удаляет пробелы по краям.

```python
            if value == "":
                continue
```
Если ячейка пуста, пропускаем её (пустые ячейки допустимы).

```python
            if not self.is_number(value):
                is_num = False
                break
```
Если значение не число, помечаем колонку как не-числовую и выходим из внутреннего цикла.

```python
        if is_num:
            numeric.append(col)
```
Если колонка оказалась числовой, добавляем её в список.

```python
    return numeric
```
Возвращаем список числовых колонок.

```python
def run(self):
    numeric = self.numeric_columns()
```
Получаем список числовых колонок.

```python
    print("9. Число строк и числовые колонки")
    print("Строк:", len(self.rows))
```
`len()` — функция для подсчёта длины (количества элементов в списке).

```python
    print("Числовые колонки:", numeric)
```
Выводим найденные числовые колонки.

```python
    print("Суммы:")
    for col in numeric:
        total = 0.0
```
Для каждой числовой колонки инициализируем переменную для суммы.

```python
        for row in self.rows:
            value = row[col].strip()
            if value != "":
                total += float(value)
```
Проходим по всем строкам, берём значение, преобразуем в число и добавляем к сумме.

```python
        print(col, total)
```
Выводим название колонки и её сумму.

---

## Task 10: Статистика для двух числовых колонок

**Цель**: найти минимум, максимум и среднее значение для первых двух числовых колонок.

### Ключевые функции

```python
def run(self):
    numeric = self.numeric_columns()
    if len(numeric) < 2:
        print("Нужно как минимум две числовые колонки")
        return
```
Сначала проверяем, есть ли две числовые колонки. Если нет — выходим.

```python
    for col in numeric[:2]:
```
`[:2]` — это срез списка. Берём первые 2 элемента.

```python
        values = []
        for row in self.rows:
            value = row[col].strip()
            if value != "":
                values.append(float(value))
```
Собираем все числовые значения из текущей колонки.

```python
        mmin = min(values)
        mmax = max(values)
        mean = sum(values) / len(values)
```
`min()` — минимальное значение, `max()` — максимальное, `sum()` — сумма, `len()` — количество.

```python
        print(col, "min=", mmin, "max=", mmax, "mean=", round(mean, 2))
```
`round(mean, 2)` — округляем среднее значение до 2 десятичных знаков.

---

## Task 11: Полное описание данных

**Цель**: вывести первые 5 строк, статистику (среднее и стандартное отклонение) и подсчитать пропуски.

### Ключевые части

```python
for row in self.rows[:5]:
    print(" | ".join(row[col] for col in self.cols))
```
Выводим первые 5 строк. `join()` — объединяет элементы в одну строку через разделитель.

```python
mean = sum(values) / count
s2 = 0.0
for v in values:
    s2 += (v - mean) ** 2
std = (s2 / count) ** 0.5
```
Вычисляем стандартное отклонение. `** 2` — возведение в квадрат, `** 0.5` — извлечение квадратного корня.

```python
for col in self.cols:
    miss = 0
    for row in self.rows:
        if row[col].strip() == "":
            miss += 1
    print(col, miss)
```
Подсчитываем пустые ячейки для каждой колонки.

---

## Task 12: Топ-5 категорий и квартили

**Цель**: найти 5 самых частых значений в категориальной колонке и границы квартилей.

### Ключевые функции

```python
def top_categories(self, col):
    counts = {}
    for row in self.rows:
        value = row[col].strip()
        if value == "":
            value = "(пусто)"
        counts[value] = counts.get(value, 0) + 1
```
Создаём словарь `counts`. Для каждого уникального значения считаем, сколько раз оно встречается. `get(value, 0)` — если ключа нет, возвращаем 0.

```python
    pairs = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return pairs[:5]
```
`sorted()` сортирует пары (значение, количество) по количеству в обратном порядке. `lambda` — безымянная функция для сортировки. `[:5]` — берём первые 5.

```python
def quartiles(self, col):
    values = []
    for row in self.rows:
        value = row[col].strip()
        if value != "":
            values.append(float(value))
    values.sort()
```
Собираем числовые значения и сортируем их по возрастанию.

```python
    q25 = values[int(n * 0.25)]
    q50 = values[int(n * 0.5)]
    q75 = values[int(n * 0.75)]
```
Берём элементы на 25%, 50% и 75% позициях отсортированного списка. `int()` — преобразует в целое число (индекс).

---

## Task 13: Генерация графиков

**Цель**: создать три типа графиков: гистограмму, линейный график и диаграмму топ-5 категорий.

### Ключевые функции

```python
import matplotlib.pyplot as plt
```
Импортируем библиотеку для рисования графиков.

```python
def save_histogram(self, col):
    values = []
    for row in self.rows:
        value = row[col].strip()
        if value != "":
            values.append(float(value))
    plt.figure(figsize=(10, 5))
```
`figsize=(10, 5)` — размер графика (ширина 10, высота 5).

```python
    plt.hist(values, bins=8, color="orange", edgecolor="black", alpha=0.7)
```
`hist()` — рисует гистограмму. `bins=8` — делим данные на 8 групп. `color` — цвет, `alpha=0.7` — прозрачность 70%.

```python
    plt.title("Гистограмма " + col)
    plt.xlabel(col)
    plt.ylabel("Число строк")
```
Заголовок графика, подписи осей.

```python
    plt.savefig("histogram.png")
    plt.close()
```
`savefig()` — сохраняет график в файл. `close()` — закрывает объект графика, освобождая память.

```python
def save_line_plot(self, col):
    plt.plot(values, marker="o", linestyle="-", color="purple")
```
`plot()` — линейный график. `marker="o"` — точки на линии, `linestyle="-"` — полная линия.

```python
def save_top_categories(self, col):
    plt.barh(labels, values, color="teal")
```
`barh()` — горизонтальная столбчатая диаграмма (стоящие столбцы).

```python
    for index, value in enumerate(values):
        plt.text(value + 0.1, index, str(value), va="center")
```
`enumerate()` — даёт индекс и значение одновременно. `text()` — добавляет текстовую подпись к графику.

---

## Task 14: HTTP API для отчёта

**Цель**: запустить простой HTTP-сервер, который на запрос `/report` возвращает JSON с анализом данных.

### Импорты

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
```
Модуль для создания HTTP-сервера.

```python
from urllib.parse import parse_qs, unquote, urlparse
```
Функции для парсинга URL и параметров запроса.

### Класс Task14

```python
def missing_counts(self):
    result = {}
    for col in self.cols:
        miss = 0
        for row in self.rows:
            if row[col].strip() == "":
                miss += 1
        result[col] = miss
    return result
```
Подсчитываем пустые ячейки для каждой колонки.

```python
def describe_columns(self, cols):
    result = {}
    for col in cols:
        values = [...]
        result[col] = {
            "count": len(values),
            "mean": sum(values) / len(values),
            "min": values[0],
            "25%": values[int(len(values) * 0.25)],
            "max": values[-1],
        }
    return result
```
Возвращаем словарь со статистикой по числовым колонкам в виде JSON.

### Класс Handler

```python
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
```
Метод вызывается, когда приходит GET-запрос.

```python
    parsed = urlparse(self.path)
    if parsed.path != "/report":
        self.send_response(404)
        return
```
Проверяем путь в URL. Если не `/report`, отправляем ошибку 404.

```python
    params = parse_qs(parsed.query)
    file_name = params.get("file", [""])[0]
    cols = params.get("cols", [""])[0].split(",")
    cat = params.get("cat", [""])[0]
```
Извлекаем параметры из URL:
- `file` — имя файла
- `cols` — колонки для анализа (через запятую)
- `cat` — категориальная колонка

```python
    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    self.end_headers()
    data = json.dumps(report, ensure_ascii=False)
    self.wfile.write(data.encode("utf-8"))
```
Отправляем успешный ответ (200) с заголовком `Content-Type: application/json` и данными в виде JSON.

### Запуск сервера

```python
def run_server():
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    server.serve_forever()
```
Создаём сервер на localhost порт 8000 и запускаем его.

---

## Как запустить

### Task 9–12 (консольный вывод)
```bash
python task9.py
python task10.py
python task11.py
python task12.py
```

### Task 13 (генерация графиков)
```bash
python task13.py
```
Создаст файлы: `histogram.png`, `line_plot.png`, `top_categories.png`

### Task 14 (HTTP-сервер)

1. Запустите сервер в одном терминале:
```bash
python task14.py
```
Вы увидите: `Запуск сервера http://127.0.0.1:8000/report?...`

2. Откройте другой терминал и сделайте запрос, или откройте в браузере:

**Примеры запросов:**

Анализ колонок `age` и `score` (числовые):
```
http://127.0.0.1:8000/report?file=data.csv&cols=age,score&cat=group
```

Анализ колонок `id` и `age` с категорией `city`:
```
http://127.0.0.1:8000/report?file=data.csv&cols=id,age&cat=city
```

**Параметры URL:**
- `file` — имя CSV-файла (обязательно)
- `cols` — две колонки для анализа через запятую (обязательно)
- `cat` — категориальная колонка (опционально)

**Выход (JSON):**
```json
{
  "n_rows": 100,
  "missing": {"age": 2, "score": 0, ...},
  "describe": {
    "age": {"count": 98, "mean": 35.5, "min": 18, "25%": 25, "50%": 35, "75%": 45, "max": 65},
    "score": {"count": 100, "mean": 75.2, ...}
  },
  "top_categories": [["group_A", 30], ["group_B", 25], ...]
}
```

**Остановить сервер:** нажмите `Ctrl+C` в терминале

---

## Требования

- Python 3.7+
- `matplotlib` (для Task 13)

Установка: `pip install matplotlib`
