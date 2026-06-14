from app.agents.research_agent import (
    ResearchAgent
)

from app.analytics.theme_counter import (
    ThemeCounter
)

from app.analytics.sentiment_analyzer import (
    SentimentAnalyzer
)


sample_text = """

Users are confused during KYC verification.

Many users abandon onboarding.

Verification takes more than 48 hours.

Users want onboarding videos.

Customers repeatedly contact support.

The dashboard is appreciated.

"""

theme_counts = (

    ThemeCounter.count_themes(
        sample_text
    )

)

sentiment = (

    SentimentAnalyzer.analyze(
        sample_text
    )

)

result = ResearchAgent.analyze(

    sample_text,

    theme_counts,

    sentiment

)

print(result)