class DecisionAgent:

    @staticmethod
    def analyze(

        research_results,

        trend_results,

        risk_score

    ):

        recommendations = []

        if risk_score >= 8:

            recommendations.append(

                "Urgently address onboarding and verification bottlenecks."

            )

            recommendations.append(

                "Allocate additional customer support resources."

            )

        elif risk_score >= 5:

            recommendations.append(

                "Improve onboarding experience and customer education."

            )

            recommendations.append(

                "Monitor verification delays closely."

            )

        else:

            recommendations.append(

                "Maintain current operational strategy."

            )

            recommendations.append(

                "Focus on product enhancement and customer retention."

            )

        recommendations.append(

            "Continue investing in dashboard and portfolio analytics capabilities."

        )

        recommendations.append(

            "Expand educational content for first-time investors."

        )

        return "\n".join(
            recommendations
        )