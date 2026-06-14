from app.llm.gemini_service import (
    generate_response
)


class AIThemeExtractor:

    @staticmethod
    def extract(
        text: str
    ):

        prompt = f"""

You are a senior business intelligence analyst.

Analyze the following organizational data.

Identify:

1. Major Themes
2. Emerging Concerns
3. Positive Signals
4. Strategic Opportunities

Return results in structured bullet points.

DATA:

{text[:12000]}

"""

        return generate_response(
            prompt
        )