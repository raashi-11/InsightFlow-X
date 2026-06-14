from app.processors.document_processor import (
    DocumentProcessor
)

from app.analytics.theme_counter import (
    ThemeCounter
)

from app.analytics.sentiment_analyzer import (
    SentimentAnalyzer
)

from app.analytics.risk_scorer import (
    RiskScorer
)

from app.analytics.ai_theme_extractor import (
    AIThemeExtractor
)

processor = DocumentProcessor()

document = processor.process(
    "data/raw/customer_feedback.txt"
)

text = document["content"]

theme_counts = (
    ThemeCounter.count_themes(
        text
    )
)

print("\nTHEMES\n")
print(theme_counts)

sentiment = (
    SentimentAnalyzer.analyze(
        text
    )
)

print("\nSENTIMENT\n")
print(sentiment)

risk_score = (
    RiskScorer.calculate(
        sentiment,
        theme_counts
    )
)

print("\nRISK SCORE\n")
print(risk_score)

print("\nAI THEMES\n")

print(

    AIThemeExtractor.extract(
        text
    )

)