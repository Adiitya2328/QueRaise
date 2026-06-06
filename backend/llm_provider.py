from google import genai
from backend.config import settings

# Create Gemini client
client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_response(prompt):
    """
    Generate response from the configured LLM.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()