from app.ingestion.text_loader import load_text

from app.agents.research_agent import (
    analyze_feedback
)

text = load_text(
    "data/raw/customer_feedback.txt"
)

analysis = analyze_feedback(
    text
)

print(analysis)