import pandas as pd


class Task11:
    def __init__(self, file_name="data.csv"):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def run(self):
        describe = self.df.describe().round(2).to_dict()
        missing = self.df.isna().sum().astype(int).to_dict()

        clean_describe = {}
        for col, stats in describe.items():
            clean_describe[col] = {}
            for key, value in stats.items():
                clean_describe[col][key] = float(value)

        return {
            "describe": clean_describe,
            "missing": missing,
        }
