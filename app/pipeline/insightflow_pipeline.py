from pathlib import Path

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

from app.agents.decision_agent import (
    DecisionAgent
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

    def run_folder(
        self,
        folder_path
    ):

        all_text = ""

        processed_files = 0

        supported_extensions = [

            ".txt",
            ".csv",
            ".pdf",
            ".mp3",
            ".wav",
            ".m4a"
        ]

        folder = Path(
            folder_path
        )

        for file_path in folder.rglob("*"):

            if (

                file_path.is_file()

                and

                file_path.suffix.lower()

                in supported_extensions

            ):

                try:

                    print(
                        f"Processing: {file_path.name}"
                    )

                    document = (

                        self.processor.process(
                            str(file_path)
                        )
                    )

                    self.memory.ingest_document(
                        document
                    )

                    all_text += (

                        "\n\n"

                        + document[
                            "content"
                        ]
                    )

                    processed_files += 1

                except Exception as e:

                    print(
                        f"Error processing {file_path.name}: {e}"
                    )

        print(
            f"\nProcessed {processed_files} files"
        )

        print(
            "\nRunning analytics..."
        )

        theme_counts = (

            ThemeCounter.count_themes(
                all_text
            )
        )

        sentiment = (

            SentimentAnalyzer.analyze(
                all_text[:5000]
            )
        )

        risk_score = (

            RiskScorer.calculate(

                sentiment,

                theme_counts

            )
        )

        #
        # IMPORTANT
        # Limit text sent to Gemini
        # so organization-wide analysis scales.
        #

        organizational_summary = (

            all_text[:10000]

        )

        print(
            "\nRunning AI theme extraction..."
        )

        ai_themes = (

            AIThemeExtractor.extract(
                organizational_summary
            )
        )

        print(
            "\nRunning research agent..."
        )

        research_results = (

            ResearchAgent.analyze(

                organizational_summary,

                theme_counts,

                sentiment

            )
        )

        print(
            "\nRunning decision agent..."
        )

        decision_results = (

            DecisionAgent.analyze(

                research_results,

                ai_themes,

                risk_score

            )
        )

        print(
            "\nGenerating executive report..."
        )

        report = (

            ExecutiveReportGenerator.generate(

                research_results,

                ai_themes,

                decision_results,

                risk_score

            )
        )

        return {

            "processed_files":
            processed_files,

            "theme_counts":
            theme_counts,

            "sentiment":
            sentiment,

            "risk_score":
            risk_score,

            "ai_themes":
            ai_themes,

            "research_results":
            research_results,

            "decision_results":
            decision_results,

            "report":
            report
        }