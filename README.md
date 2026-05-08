# Мини-отчёт по таблице

Проект читает файл `data.csv`, анализирует таблицу и показывает результат через FastAPI.

## Запуск

```bash
python "22. Мини-отчёт по таблице.py"
```

Документация FastAPI:

```text
http://127.0.0.1:8001/docs
```

Главный отчёт:

```text
http://127.0.0.1:8001/mini-report?file=data.csv&col1=age&col2=score&cat=city
```

---

## Общая структура

В проекте есть отдельные файлы для заданий:

1. `task9.py` — числовые колонки и суммы.
2. `task10.py` — `min`, `max`, `mean`.
3. `task11.py` — `describe()` и пропуски.
4. `task12.py` — топ-5 категорий и квартильные границы.
5. `task13.py` — PNG-графики.
6. `task14.py` — JSON-отчёт.
7. `22. Мини-отчёт по таблице.py` — FastAPI-сервер.

Главная идея простая:

```python
Task14("data.csv").run("age", "score", "city")
```

Мы создаём объект задания, передаём файл и получаем готовый словарь с результатом.

---

## Task 9: числовые колонки и суммы

```python
import numpy as np
import pandas as pd
```

Подключаются библиотеки.
`pandas` читает таблицу, а `numpy` помогает считать суммы.

```python
self.df = pd.read_csv(file_name)
```

Эта строка читает CSV-файл и превращает его в таблицу.

```python
self.df[col].astype(float)
```

Программа пробует превратить колонку в числа.
Если получилось — колонка числовая.

```python
values = self.df[col].astype(float).to_numpy()
sums[col] = float(np.nansum(values))
```

Колонка превращается в массив NumPy.
Потом считается сумма всех чисел.

---

## Task 10: min, max, mean

```python
numeric = self.numeric_columns()
```

Сначала программа находит числовые колонки.

```python
for col in numeric[:2]:
```

Берутся только первые две числовые колонки.

```python
values = self.df[col].astype(float).dropna().to_numpy()
```

Колонка превращается в числа.
`dropna()` убирает пустые значения.
`to_numpy()` делает массив.

```python
"min": float(np.min(values)),
"max": float(np.max(values)),
"mean": round(float(np.mean(values)), 2),
```

Здесь считаются минимум, максимум и среднее значение.

---

## Task 11: describe и пропуски

```python
self.df = pd.read_csv(file_name)
```

Файл полностью читается через `pandas`.

```python
describe = self.df.describe().round(2).to_dict()
```

`describe()` сразу считает основную статистику:

- `count` — сколько значений
- `mean` — среднее
- `std` — разброс
- `min` — минимум
- `25%`, `50%`, `75%` — квартильные границы
- `max` — максимум

```python
missing = self.df.isna().sum().astype(int).to_dict()
```

Эта строка считает пропуски по каждой колонке.

Простой аналог:

```python
missing = {}
for col in columns:
    missing[col] = 0
```

Только `pandas` делает это быстрее и короче.

---

## Task 12: топ-5 и квартильные границы

```python
category = self.category_columns()
numeric = self.numeric_columns()
```

Программа отдельно ищет текстовые и числовые колонки.

```python
top = self.df[cat_col].fillna("(empty)").value_counts().head(5)
```

Эта строка делает топ-5 значений.
Например, какие города встречаются чаще всего.

```python
quartiles = self.df[num_col].quantile([0.25, 0.5, 0.75])
```

Здесь считаются границы квартилей:

- `25%`
- `50%`
- `75%`

---

## Task 13: графики

```python
import matplotlib.pyplot as plt
```

Подключается библиотека для рисования графиков.

```python
plt.hist(values, bins=8, color="orange", edgecolor="black", alpha=0.7)
```

Создаётся гистограмма числовой колонки.

```python
plt.barh(labels, values, color="teal")
```

Создаётся горизонтальный bar-график для топ-5 категорий.

```python
plt.savefig(self.chart_path("histogram.png"))
```

График сохраняется в PNG-файл.

После запуска `task13.py` появляются:

- `histogram.png`
- `top_categories.png`

---

## Task 14: JSON-отчёт

`task14.py` не запускает FastAPI.
Он только готовит данные для отчёта.

```python
import pandas as pd
```

Подключается `pandas`.
Он нужен, чтобы читать CSV и считать статистику.

```python
class Task14:
```

Создаётся класс задания 14.
Класс нужен, чтобы весь код задания был в одном месте.

```python
def __init__(self, file_name="data.csv"):
    self.file_name = file_name
    self.df = pd.read_csv(file_name)
```

Когда создаётся `Task14`, программа:

1. запоминает имя файла
2. читает CSV
3. сохраняет таблицу в `self.df`

```python
def numeric_columns(self):
    return self.df.select_dtypes(include="number").columns.tolist()
```

Метод возвращает список числовых колонок.

```python
def category_columns(self):
    return self.df.select_dtypes(exclude="number").columns.tolist()
```

Метод возвращает список текстовых колонок.

```python
selected = [col for col in columns if col in self.df.columns]
```

Здесь программа оставляет только те колонки, которые реально есть в таблице.
Это защита от неправильного имени колонки.

```python
describe = self.df[selected].describe().round(2).to_dict()
```

Считается статистика для выбранных колонок.
Потом результат округляется и превращается в словарь.

```python
top = self.df[col].fillna("(empty)").value_counts().head(5)
```

Считается топ-5 значений в категориальной колонке.

```python
def run(self, col1="", col2="", cat=""):
```

Это главный метод задания 14.
Он собирает весь отчёт.

```python
return {
    "file": self.file_name,
    "n_rows": int(len(self.df)),
    "describe": self.describe_columns(selected_numeric[:2]),
    "top_categories": self.top_categories(selected_cat),
}
```

Метод возвращает словарь.
FastAPI потом показывает этот словарь как JSON.

---

## FastAPI-файл

Файл называется:

```text
22. Мини-отчёт по таблице.py
```

В нём находится сервер.

```python
from fastapi import FastAPI, Query
```

`FastAPI` создаёт сервер.
`Query` помогает получать параметры из URL.

```python
from task14 import Task14
```

Так FastAPI получает доступ к заданию 14.

```python
app = FastAPI(title="Mini table report")
```

Создаётся приложение FastAPI.

```python
@app.get("/task14")
```

Эта строка создаёт адрес:

```text
/task14
```

```python
def task14(file: str = Query("data.csv"), col1: str = Query(""), col2: str = Query(""), cat: str = Query("")):
```

Функция получает параметры из URL:

- `file` — имя CSV-файла
- `col1` — первая числовая колонка
- `col2` — вторая числовая колонка
- `cat` — категориальная колонка

```python
return Task14(file).run(col1, col2, cat)
```

Создаётся объект `Task14`.
Потом запускается метод `run()`.
Результат возвращается в браузер как JSON.

```python
@app.get("/mini-report")
```

Это общий отчёт.
Он запускает задания 9-14 вместе.

```python
uvicorn.run(app, host="127.0.0.1", port=8001)
```

Эта строка запускает сервер.
После неё можно открыть:

```text
http://127.0.0.1:8001/docs
```

---

## Общий принцип работы

1. Пользователь открывает адрес в браузере.
2. FastAPI получает параметры из URL.
3. Нужный класс читает `data.csv`.
4. Программа считает статистику.
5. FastAPI возвращает результат как JSON.

