from pathlib import Path
from datetime import datetime


class MetadataProcessor:

    @staticmethod
    def extract(
        file_path: str
    ):

        path = Path(
            file_path
        )

        metadata = {

            "filename":
            path.name,

            "extension":
            path.suffix,

            "size_kb":
            round(
                path.stat().st_size
                / 1024,
                2
            ),

            "processed_at":
            datetime.now().isoformat()
        }

        return metadata