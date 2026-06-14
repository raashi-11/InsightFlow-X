from app.retrieval.retriever import (
    Retriever
)

retriever = Retriever()

results = retriever.retrieve(
    "What projects has Raashi built?"
)

print(
    results["documents"]
)