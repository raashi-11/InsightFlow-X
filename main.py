from app.llm.gemini_service import ask_gemini

response = ask_gemini(
    "Explain what organizational intelligence means in one paragraph."
)

print(response)