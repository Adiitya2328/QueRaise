from backend.llm_provider import generate_response
from backend.sql_cleaner import clean_sql


def generate_sql(system_prompt, user_question):
    """
    Convert natural language into SQL.
    """

    prompt = f"""
{system_prompt}

User Question:
{user_question}
"""

    response = generate_response(prompt)

    return clean_sql(response)