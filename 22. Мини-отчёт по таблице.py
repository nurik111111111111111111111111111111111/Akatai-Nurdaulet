from fastapi import FastAPI, Query

from task9 import Task9
from task10 import Task10
from task11 import Task11
from task12 import Task12
from task13 import Task13
from task14 import Task14


app = FastAPI(title="Mini table report")


@app.get("/")
def root():
    return {
        "message": "Mini table report",
        "endpoints": [
            "/task9?file=data.csv",
            "/task10?file=data.csv",
            "/task11?file=data.csv",
            "/task12?file=data.csv",
            "/task13?file=data.csv",
            "/task14?file=data.csv&col1=age&col2=score&cat=city",
            "/mini-report?file=data.csv&col1=age&col2=score&cat=city",
        ],
    }


@app.get("/task9")
def task9(file: str = Query("data.csv")):
    return Task9(file).run()


@app.get("/task10")
def task10(file: str = Query("data.csv")):
    return Task10(file).run()


@app.get("/task11")
def task11(file: str = Query("data.csv")):
    return Task11(file).run()


@app.get("/task12")
def task12(file: str = Query("data.csv")):
    return Task12(file).run()


@app.get("/task13")
def task13(file: str = Query("data.csv")):
    return Task13(file).run()


@app.get("/task14")
def task14(
    file: str = Query("data.csv"),
    col1: str = Query(""),
    col2: str = Query(""),
    cat: str = Query(""),
):
    return Task14(file).run(col1, col2, cat)


@app.get("/mini-report")
def mini_report(
    file: str = Query("data.csv"),
    col1: str = Query(""),
    col2: str = Query(""),
    cat: str = Query(""),
):
    return {
        "task9": Task9(file).run(),
        "task10": Task10(file).run(),
        "task11": Task11(file).run(),
        "task12": Task12(file).run(),
        "task13": Task13(file).run(),
        "task14": Task14(file).run(col1, col2, cat),
    }


if __name__ == "__main__":
    import uvicorn

    print("Mini report: http://127.0.0.1:8001/mini-report?file=data.csv&col1=age&col2=score&cat=city")
    print("Task 14: http://127.0.0.1:8001/task14?file=data.csv&col1=age&col2=score&cat=city")
    uvicorn.run(app, host="127.0.0.1", port=8001)
