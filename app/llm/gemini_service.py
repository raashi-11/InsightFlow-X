import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(prompt: str):
    response = model.generate_content(prompt)
    return response.text

def ask_with_context(
    query,
    context
):

    prompt = f"""
You are an organizational intelligence analyst.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}
"""

    response = model.generate_content(
        prompt
    )

    return response.text