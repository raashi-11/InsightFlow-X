from app.llm.gemini_service import ask_gemini


def analyze_trends(previous_data, current_data):

    prompt = f"""
You are a senior business intelligence analyst.

Compare the two datasets.

Identify:

1. Emerging Problems
2. Improving Areas
3. New Risks
4. Strategic Opportunities

Previous Data:
{previous_data}

Current Data:
{current_data}

Provide an executive summary.
"""

    return ask_gemini(prompt)