from collections import Counter
import re


class ThemeCounter:

    DEFAULT_THEMES = [

        "onboarding",
        "verification",
        "kyc",
        "support",
        "dashboard",
        "pricing",
        "payment",
        "investment",
        "documentation",
        "security",
        "performance",
        "usability",
        "education",
        "compliance"
    ]

    @classmethod
    def count_themes(
        cls,
        text: str
    ):

        text = text.lower()

        counts = {}

        for theme in cls.DEFAULT_THEMES:

            matches = re.findall(
                rf"\b{theme}\b",
                text
            )

            counts[theme] = len(
                matches
            )

        return dict(

            sorted(
                counts.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )