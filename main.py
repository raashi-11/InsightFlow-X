from app.retrieval.retriever import (
    retrieve_context
)

from app.llm.gemini_service import (
    ask_with_context
)

query = "Why are users abandoning onboarding?"

context = retrieve_context(
    query
)

answer = ask_with_context(
    query,
    context
)

print("\nCONTEXT:\n")
print(context)

print("\nANSWER:\n")
print(answer)