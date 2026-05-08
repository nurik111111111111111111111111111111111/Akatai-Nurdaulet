import pandas as pd


class Task14:
    def __init__(self, file_name="data.csv"):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def numeric_columns(self):
        return self.df.select_dtypes(include="number").columns.tolist()

    def category_columns(self):
        return self.df.select_dtypes(exclude="number").columns.tolist()

    def describe_columns(self, columns):
        selected = [col for col in columns if col in self.df.columns]
        if not selected:
            return {}

        describe = self.df[selected].describe().round(2).to_dict()
        result = {}
        for col, stats in describe.items():
            result[col] = {}
            for key, value in stats.items():
                result[col][key] = float(value)
        return result

    def top_categories(self, col):
        if not col or col not in self.df.columns:
            return []

        top = self.df[col].fillna("(empty)").value_counts().head(5)
        return [[str(index), int(value)] for index, value in top.items()]

    def run(self, col1="", col2="", cat=""):
        numeric = self.numeric_columns()
        category = self.category_columns()

        selected_numeric = [col for col in [col1, col2] if col]
        if not selected_numeric:
            selected_numeric = numeric[:2]

        selected_cat = cat
        if not selected_cat and category:
            selected_cat = category[0]

        return {
            "file": self.file_name,
            "n_rows": int(len(self.df)),
            "describe": self.describe_columns(selected_numeric[:2]),
            "top_categories": self.top_categories(selected_cat),
        }


if __name__ == "__main__":
    print(Task14().run())
