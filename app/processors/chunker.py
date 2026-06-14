class Chunker:

    def __init__(
        self,
        chunk_size=500,
        overlap=100
    ):

        self.chunk_size = chunk_size

        self.overlap = overlap

    def chunk_text(
        self,
        text: str
    ):

        chunks = []

        start = 0

        while start < len(text):

            end = (
                start
                + self.chunk_size
            )

            chunk = text[
                start:end
            ]

            chunks.append(
                chunk
            )

            start += (
                self.chunk_size
                - self.overlap
            )

        return chunks