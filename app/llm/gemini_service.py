import os

from dotenv import load_dotenv

from google import genai


load_dotenv()


class GeminiService:

    _client = None

    @classmethod
    def get_client(cls):

        if cls._client is None:

            api_key = os.getenv(
                "GOOGLE_API_KEY"
            )

            cls._client = genai.Client(
                api_key=api_key
            )

        return cls._client

    @classmethod
    def generate(
        cls,
        prompt: str
    ):

        client = cls.get_client()

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt
        )

        return response.text


def generate_response(
    prompt: str
):

    return GeminiService.generate(
        prompt
    )