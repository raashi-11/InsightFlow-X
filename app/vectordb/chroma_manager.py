import chromadb

from app.embeddings.embedding_service import (
    EmbeddingService
)


class ChromaManager:

    def __init__(self):

        self.client = (
            chromadb.PersistentClient(
                path="data/chroma_db"
            )
        )

        self.collection = (
            self.client
            .get_or_create_collection(
                name="organizational_memory"
            )
        )

    def store_chunks(
        self,
        chunks,
        metadata
    ):

        for idx, chunk in enumerate(chunks):

            embedding = (
                EmbeddingService
                .generate_embedding(
                    chunk
                )
            )

            chunk_id = (
                f"{metadata['filename']}"
                f"_{idx}"
            )

            self.collection.add(

                ids=[chunk_id],

                documents=[chunk],

                embeddings=[embedding],

                metadatas=[
                    {
                        "filename":
                        metadata[
                            "filename"
                        ],

                        "chunk_id":
                        idx
                    }
                ]
            )

    def search(
        self,
        query_embedding,
        n_results=5
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=n_results
        )