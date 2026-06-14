from app.vectordb.chroma_manager import (
    ChromaManager
)


class OrganizationalMemory:

    def __init__(self):

        self.db = (
            ChromaManager()
        )

    def ingest_document(
        self,
        document
    ):

        self.db.store_chunks(

            document["chunks"],

            document["metadata"]
        )