import pandas as pd


class Task12:
    def __init__(self, file_name="data.csv"):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def numeric_columns(self):
        return self.df.select_dtypes(include="number").columns.tolist()

    def category_columns(self):
        return self.df.select_dtypes(exclude="number").columns.tolist()

    def run(self):
        numeric = self.numeric_columns()
        category = self.category_columns()
        if not numeric or not category:
            return {"error": "обезательно должен быть хотябы одно"}
        
        cat_col = category[0]
        num_col = numeric[0]

        top = self.df[cat_col].fillna("(empty)").value_counts().head(5)
        quartiles = self.df[num_col].quantile([0.25, 0.5, 0.75])

        return {
            "category_column": cat_col,
            "numeric_column": num_col,
            "top_categories": [[str(index), int(value)] for index, value in top.items()],
            "quartiles": {
                "25%": float(quartiles.loc[0.25]),
                "50%": float(quartiles.loc[0.5]),
                "75%": float(quartiles.loc[0.75]),
            },
        }
