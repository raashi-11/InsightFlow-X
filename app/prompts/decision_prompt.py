def build_decision_prompt(

    research_results,

    trend_results,

    risk_score

):

    return f"""

You are a Chief Strategy Officer.

RESEARCH FINDINGS:
{research_results}

TREND ANALYSIS:
{trend_results}

RISK SCORE:
{risk_score}

Provide:

1. Executive Summary
2. Top Priorities
3. Recommended Actions
4. Expected Business Impact
5. Success Metrics

Rank recommendations by priority.

Return results in professional report format.

"""