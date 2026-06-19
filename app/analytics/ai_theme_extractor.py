class AIThemeExtractor:

    @staticmethod
    def extract(
        text
    ):

        themes = {

            "Onboarding":
            text.lower().count(
                "onboarding"
            ),

            "Verification":
            text.lower().count(
                "verification"
            ),

            "KYC":
            text.lower().count(
                "kyc"
            ),

            "Support":
            text.lower().count(
                "support"
            ),

            "Investment":
            text.lower().count(
                "investment"
            ),

            "Dashboard":
            text.lower().count(
                "dashboard"
            ),

            "Education":
            text.lower().count(
                "education"
            ),

            "Compliance":
            text.lower().count(
                "compliance"
            )
        }

        sorted_themes = sorted(

            themes.items(),

            key=lambda x: x[1],

            reverse=True

        )

        summary = []

        for theme, count in sorted_themes:

            if count > 0:

                summary.append(

                    f"{theme}: {count} mentions"

                )

        return "\n".join(
            summary
        )