import numpy as np
import pandas as pd


class Task9:
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
        sums = {}
        for col in numeric:
            values = self.df[col].astype(float).to_numpy()#колонкаларды float түріне ауыстырып, numpy массивіне айналдырамыз
            sums[col] = float(np.nansum(values))

        return {
            "n_rows": int(len(self.df)),
            "numeric_columns": numeric,
            "sums": sums,
        }
