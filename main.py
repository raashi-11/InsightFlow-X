from app.evaluation.executive_report_generator import (
    ExecutiveReportGenerator
)

research_results = """
Top Pain Points:
- KYC confusion
- Verification delays

Opportunities:
- Video onboarding
"""

trend_results = """
Onboarding complaints increased 40%
Verification complaints increased 25%
"""

decision_results = """
Priority 1:
Improve onboarding flow

Priority 2:
Reduce verification turnaround time
"""

risk_score = 7.2

report = ExecutiveReportGenerator.generate(

    research_results,

    trend_results,

    decision_results,

    risk_score

)

print(report)