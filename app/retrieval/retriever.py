from app.embeddings.embedding_service import (
    EmbeddingService
)

from app.vectordb.chroma_manager import (
    ChromaManager
)


class Retriever:

    def __init__(self):

        self.db = ChromaManager()

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = (

            EmbeddingService
            .generate_embedding(
                query
            )
        )

        results = (

            self.db.search(
                query_embedding,
                top_k
            )
        )

        return results