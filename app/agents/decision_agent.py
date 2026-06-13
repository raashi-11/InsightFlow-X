from app.llm.gemini_service import ask_gemini


def generate_recommendations(analysis):

    prompt = f"""
You are a Chief Product Officer.

Based on the analysis below:

{analysis}

Generate:

1. Top 3 Actions
2. Expected Business Impact
3. Priority Level
4. Effort Level
5. Success Metrics

Format clearly.
"""

    return ask_gemini(prompt)