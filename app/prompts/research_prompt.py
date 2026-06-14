def build_research_prompt(

    context,

    theme_counts,

    sentiment

):

    return f"""

You are a Senior Business Intelligence Analyst.

Analyze the organizational data below.

CONTEXT:
{context}

THEME COUNTS:
{theme_counts}

SENTIMENT:
{sentiment}

Identify:

1. Top Pain Points
2. Feature Requests
3. Positive Signals
4. Risks
5. Opportunities

Return results in structured markdown format.

"""