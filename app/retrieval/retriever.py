from app.embeddings.embedding_service import (
    generate_embedding
)

from app.vectordb.chroma_manager import (
    search_documents
)


def retrieve_context(query):

    query_embedding = generate_embedding(
        query
    )

    results = search_documents(
        query_embedding
    )

    documents = results["documents"][0]

    context = "\n".join(documents)

    return context