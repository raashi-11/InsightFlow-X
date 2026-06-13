from app.ingestion.text_loader import load_text

text = load_text(
    "data/raw/customer_feedback.txt"
)

print(text)