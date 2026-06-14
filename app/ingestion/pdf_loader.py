from pypdf import PdfReader


class PDFLoader:

    @staticmethod
    def load(file_path: str) -> str:

        reader = PdfReader(
            file_path
        )

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:

                pages.append(text)

        return "\n".join(
            pages
        )