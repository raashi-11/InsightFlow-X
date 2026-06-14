from datetime import datetime


class ExecutiveReportGenerator:

    @staticmethod
    def generate(

        research_results,

        trend_results,

        decision_results,

        risk_score

    ):

        report = f"""

# EXECUTIVE INTELLIGENCE REPORT

Generated On:
{datetime.now()}

==================================================

RISK SCORE

{risk_score}/10

==================================================

RESEARCH INSIGHTS

{research_results}

==================================================

TREND ANALYSIS

{trend_results}

==================================================

STRATEGIC RECOMMENDATIONS

{decision_results}

==================================================

END OF REPORT

"""

        return report