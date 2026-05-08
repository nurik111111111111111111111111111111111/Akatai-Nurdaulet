import csv
import os

import matplotlib.pyplot as plt


class Task13:
    def __init__(self, file_name="data.csv"):
        self.file_name = file_name
        self.rows = []
        self.cols = []
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.load_data()

    def chart_path(self, file_name):
        return os.path.join(self.base_dir, file_name)

    def load_data(self):
        with open(self.file_name, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.cols = reader.fieldnames or []
            for row in reader:
                self.rows.append(row)

    def is_number(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False

    def numeric_columns(self):
        numeric = []
        for col in self.cols:
            is_num = True
            for row in self.rows:
                value = row[col].strip()
                if value == "":
                    continue
                if not self.is_number(value):
                    is_num = False
                    break
            if is_num:
                numeric.append(col)
        return numeric

    def category_columns(self):
        cat = []
        for col in self.cols:
            is_num = True
            for row in self.rows:
                value = row[col].strip()
                if value == "":
                    continue
                if not self.is_number(value):
                    is_num = False
                    break
            if not is_num:
                cat.append(col)
        return cat

    def save_histogram(self, col):
        values = []
        for row in self.rows:
            value = row[col].strip()
            if value != "":
                values.append(float(value))

        plt.figure(figsize=(10, 5))
        plt.hist(values, bins=8, color="orange", edgecolor="black", alpha=0.7)
        plt.title("Histogram: " + col)
        plt.xlabel(col)
        plt.ylabel("Rows")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.savefig(self.chart_path("histogram.png"))
        plt.close()

    def save_top_categories(self, col):
        counts = {}
        for row in self.rows:
            value = row[col].strip()
            if value == "":
                value = "(empty)"
            counts[value] = counts.get(value, 0) + 1

        pairs = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]
        labels = [item[0] for item in pairs]
        values = [item[1] for item in pairs]

        plt.figure(figsize=(10, 5))
        plt.barh(labels, values, color="teal")
        plt.title("Top 5 categories: " + col)
        plt.xlabel("Count")
        plt.ylabel(col)
        for index, value in enumerate(values):
            plt.text(value + 0.1, index, str(value), va="center")
        plt.tight_layout()
        plt.savefig(self.chart_path("top_categories.png"))
        plt.close()

    def run(self):
        numeric = self.numeric_columns()
        cat = self.category_columns()
        if not numeric or not cat:
            return {"error": "Need numeric and categorical columns"}

        num_col = numeric[0]
        cat_col = cat[0]
        self.save_histogram(num_col)
        self.save_top_categories(cat_col)
        return {
            "message": "Charts saved",
            "files": ["histogram.png", "top_categories.png"],
        }


if __name__ == "__main__":
    print(Task13().run())
