from app.llm.gemini_service import (
    generate_response
)

from app.prompts.decision_prompt import (
    build_decision_prompt
)


class DecisionAgent:

    @staticmethod
    def analyze(

        research_results,

        trend_results,

        risk_score

    ):

        prompt = (

            build_decision_prompt(

                research_results,

                trend_results,

                risk_score

            )

        )

        return generate_response(
            prompt
        )