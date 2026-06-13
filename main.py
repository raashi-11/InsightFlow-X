from app.embeddings.embedding_service import generate_embedding
from app.vectordb.chroma_manager import search_documents

query = "Why are users leaving onboarding?"

query_embedding = generate_embedding(
    query
)

results = search_documents(
    query_embedding
)

print(results["documents"])