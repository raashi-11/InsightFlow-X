from transformers import pipeline


class SentimentAnalyzer:

    _classifier = None

    @classmethod
    def get_classifier(cls):

        if cls._classifier is None:

            cls._classifier = pipeline(

                "sentiment-analysis",

                model=(
                    "distilbert-base-uncased-finetuned-sst-2-english"
                )
            )

        return cls._classifier

    @classmethod
    def analyze(
        cls,
        text: str
    ):

        classifier = (
            cls.get_classifier()
        )

        result = classifier(

            text[:512]
        )[0]

        return {

            "label":
            result["label"],

            "score":
            round(
                result["score"],
                4
            )
        }