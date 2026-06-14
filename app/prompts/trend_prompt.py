def build_trend_prompt(

    previous_data,

    current_data,

    trend_results

):

    return f"""

You are a Strategic Insights Analyst.

PREVIOUS DATA:
{previous_data}

CURRENT DATA:
{current_data}

TREND METRICS:
{trend_results}

Identify:

1. Emerging Problems
2. Improving Areas
3. New Risks
4. Strategic Opportunities

Explain what is changing over time.

Return results in structured markdown.

"""