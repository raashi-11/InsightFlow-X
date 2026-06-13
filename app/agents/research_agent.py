from app.llm.gemini_service import (
    ask_gemini
)


def analyze_feedback(context):

    prompt = f"""
You are a senior research analyst.

Analyze the feedback and identify:

1. Top Pain Points
2. Feature Requests
3. Positive Feedback
4. Risks
5. Opportunities

Feedback:
{context}

Return results in clear bullet points.
"""

    return ask_gemini(prompt)