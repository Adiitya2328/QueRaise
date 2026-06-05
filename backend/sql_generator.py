# Generate SQL using Gemini AI

from google import genai
from backend.config import settings


# Create Gemini client using API key from .env
client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_sql(system_prompt, user_question):
    """
    Convert natural language question into SQL using Gemini.
    """

    prompt = f"""
{system_prompt}

User Question:
{user_question}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text.strip()