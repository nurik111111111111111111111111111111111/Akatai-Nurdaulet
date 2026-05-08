import numpy as np
import pandas as pd


class Task10:
    def __init__(self, file_name="data.csv"):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def numeric_columns(self):
        numeric = []
        for col in self.df.columns:
            try:
                self.df[col].astype(float)
                numeric.append(col)
            except ValueError:
                pass
        return numeric

    def run(self):
        numeric = self.numeric_columns()
        if len(numeric) < 2:
            return {"error": "как минимум 2 числовых столбца"}

        result = {}
        for col in numeric[:2]:
            values = self.df[col].astype(float).dropna().to_numpy()
            result[col] = {
                "min": float(np.min(values)),
                "max": float(np.max(values)),
                "mean": round(float(np.mean(values)), 2),
            }

        return result
