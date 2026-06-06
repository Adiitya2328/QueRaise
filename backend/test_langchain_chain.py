from backend.langchain_sql_generator import create_sql_chain
from backend.schema_context import get_schema_context
from backend.sql_cleaner import clean_sql

chain = create_sql_chain()

schema = get_schema_context()

response = chain.invoke(
    {
        "schema": schema,
        "question": "Show first 5 artists"
    }
)

sql_query = clean_sql(response.content)

print(sql_query)