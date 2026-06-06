from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from backend.config import settings


def create_sql_chain():

    prompt = PromptTemplate(
        input_variables=["schema", "question"],
        template="""
You are a PostgreSQL SQL expert.

Database Schema:
{schema}

User Question:
{question}

Return only SQL query.
"""
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=settings.GEMINI_API_KEY,
        temperature=0
    )

    chain = prompt | llm

    return chain