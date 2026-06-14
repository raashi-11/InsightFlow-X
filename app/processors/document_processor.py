from pathlib import Path

from app.ingestion.text_loader import (
    TextLoader
)

from app.ingestion.csv_loader import (
    CSVLoader
)

from app.ingestion.pdf_loader import (
    PDFLoader
)

from app.processors.audio_processor import (
    AudioProcessor
)

from app.processors.metadata_processor import (
    MetadataProcessor
)

from app.processors.chunker import (
    Chunker
)


class DocumentProcessor:

    def __init__(self):

        self.audio_processor = None

        self.chunker = Chunker()

    def process(
        self,
        file_path: str
    ):

        path = Path(
            file_path
        )

        extension = (
            path.suffix.lower()
        )

        if extension == ".txt":

            content = (
                TextLoader.load(
                    file_path
                )
            )

        elif extension == ".csv":

            content = (
                CSVLoader.load(
                    file_path
                )
            )

        elif extension == ".pdf":

            content = (
                PDFLoader.load(
                    file_path
                )
            )

        elif extension in [
            ".mp3",
            ".wav",
            ".m4a"
        ]:

            if self.audio_processor is None:

                self.audio_processor = (
                    AudioProcessor()
                )

            content = (
                self.audio_processor
                .transcribe(
                    file_path
                )
            )

        else:

            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        metadata = (
            MetadataProcessor.extract(
                file_path
            )
        )

        chunks = (
            self.chunker
            .chunk_text(
                content
            )
        )

        return {

            "content":
            content,

            "metadata":
            metadata,

            "chunks":
            chunks
        }