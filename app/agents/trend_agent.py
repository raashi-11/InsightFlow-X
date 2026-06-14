from app.llm.gemini_service import (
    generate_response
)

from app.prompts.trend_prompt import (
    build_trend_prompt
)


class TrendAgent:

    @staticmethod
    def analyze(

        previous_data,

        current_data,

        trend_results

    ):

        prompt = (

            build_trend_prompt(

                previous_data,

                current_data,

                trend_results

            )

        )

        return generate_response(
            prompt
        )