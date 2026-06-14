class TrendDetector:

    @staticmethod
    def compare(
        previous_text: str,
        current_text: str,
        themes
    ):

        results = {}

        previous_text = (
            previous_text.lower()
        )

        current_text = (
            current_text.lower()
        )

        for theme in themes:

            prev_count = (
                previous_text.count(
                    theme.lower()
                )
            )

            curr_count = (
                current_text.count(
                    theme.lower()
                )
            )

            change = (
                curr_count
                - prev_count
            )

            results[theme] = {

                "previous":
                prev_count,

                "current":
                curr_count,

                "change":
                change
            }

        return results