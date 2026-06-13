import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="organizational_memory"
)


def add_document(doc_id, text, embedding):

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )


def search_documents(query_embedding, n_results=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results