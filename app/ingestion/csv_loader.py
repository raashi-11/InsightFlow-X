import pandas as pd


class CSVLoader:

    @staticmethod
    def load(file_path: str) -> str:

        df = pd.read_csv(file_path)

        return df.to_string(
            index=False
        )