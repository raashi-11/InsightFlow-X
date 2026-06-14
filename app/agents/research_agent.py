from app.llm.gemini_service import (
    generate_response
)

from app.prompts.research_prompt import (
    build_research_prompt
)


class ResearchAgent:

    @staticmethod
    def analyze(

        context,

        theme_counts,

        sentiment

    ):

        prompt = (

            build_research_prompt(

                context,

                theme_counts,

                sentiment

            )

        )

        return generate_response(
            prompt
        )