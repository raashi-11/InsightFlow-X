class RiskScorer:

    @staticmethod
    def calculate(

        sentiment,

        theme_counts

    ):

        score = 0

        negative_weight = 0

        if sentiment["label"] == "NEGATIVE":

            negative_weight = (

                sentiment["score"]
                * 5

            )

        issue_count = sum(

            theme_counts.values()

        )

        score = (

            negative_weight

            + issue_count / 10

        )

        score = min(
            score,
            10
        )

        return round(
            score,
            2
        )