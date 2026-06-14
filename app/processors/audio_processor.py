import whisper


class AudioProcessor:

    def __init__(self):

        self.model = whisper.load_model(
            "base"
        )

    def transcribe(
        self,
        file_path: str
    ) -> str:

        result = self.model.transcribe(
            file_path
        )

        return result["text"]