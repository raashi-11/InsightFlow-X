from app.processors.document_processor import (
    DocumentProcessor
)

from app.memory.organizational_memory import (
    OrganizationalMemory
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

from app.agents.research_agent import (
    ResearchAgent
)

from app.evaluation.executive_report_generator import (
    ExecutiveReportGenerator
)


class InsightFlowPipeline:

    def __init__(self):

        self.processor = (
            DocumentProcessor()
        )

        self.memory = (
            OrganizationalMemory()
        )

    def run(
        self,
        file_path
    ):

        print(
            "\n[1] Processing document..."
        )

        document = (
            self.processor.process(
                file_path
            )
        )

        print(
            "[2] Storing in organizational memory..."
        )

        self.memory.ingest_document(
            document
        )

        text = document[
            "content"
        ]

        print(
            "[3] Running analytics..."
        )

        theme_counts = (
            ThemeCounter.count_themes(
                text
            )
        )

        sentiment = (
            SentimentAnalyzer.analyze(
                text
            )
        )

        risk_score = (
            RiskScorer.calculate(
                sentiment,
                theme_counts
            )
        )

        ai_themes = (
            AIThemeExtractor.extract(
                text
            )
        )

        print(
            "[4] Running research agent..."
        )

        research_results = (
            ResearchAgent.analyze(
                text,
                theme_counts,
                sentiment
            )
        )

        print(
            "[5] Generating executive report..."
        )

        report = (
            ExecutiveReportGenerator.generate(

                research_results,

                ai_themes,

                "Decision Agent Placeholder",

                risk_score
            )
        )

        return {

            "metadata":
            document["metadata"],

            "theme_counts":
            theme_counts,

            "sentiment":
            sentiment,

            "risk_score":
            risk_score,

            "research_results":
            research_results,

            "report":
            report
        }