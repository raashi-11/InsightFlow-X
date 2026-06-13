from app.ingestion.text_loader import load_text

from app.agents.trend_agent import (
    analyze_trends
)

from app.agents.decision_agent import (
    generate_recommendations
)

previous = load_text(
    "data/raw/january_feedback.txt"
)

current = load_text(
    "data/raw/march_feedback.txt"
)

analysis = analyze_trends(
    previous,
    current
)

recommendations = generate_recommendations(
    analysis
)

print("\nANALYSIS\n")
print(analysis)

print("\nRECOMMENDATIONS\n")
print(recommendations)