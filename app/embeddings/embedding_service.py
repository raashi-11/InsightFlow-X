from sentence_transformers import (
    SentenceTransformer
)


class EmbeddingService:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = (
                SentenceTransformer(
                    "all-MiniLM-L6-v2"
                )
            )

        return cls._model

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        model = cls.get_model()

        embedding = model.encode(
            text
        )

        return embedding.tolist()