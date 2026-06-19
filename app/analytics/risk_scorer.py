class RiskScorer:

    @staticmethod
    def calculate(

        sentiment,

        theme_counts

    ):

        issue_count = sum(
            theme_counts.values()
        )

        issue_risk = min(
            issue_count / 20,
            5
        )

        sentiment_risk = 0

        if sentiment["label"] == "NEGATIVE":

            sentiment_risk = (

                sentiment["score"]

                * 3

            )

        elif sentiment["label"] == "POSITIVE":

            sentiment_risk = 1

        total_score = (

            issue_risk

            + sentiment_risk

        )

        return round(

            min(total_score, 10),

            2

        )