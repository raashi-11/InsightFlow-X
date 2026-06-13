from app.ingestion.text_loader import load_text
from app.embeddings.embedding_service import generate_embedding

text = load_text(
    "data/raw/customer_feedback.txt"
)

embedding = generate_embedding(text)

print(
    f"Embedding dimension: {len(embedding)}"
)