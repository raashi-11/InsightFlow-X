from pathlib import Path


class TextLoader:

    @staticmethod
    def load(file_path: str) -> str:

        path = Path(file_path)

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()