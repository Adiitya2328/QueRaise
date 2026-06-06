from backend.langchain_sql_generator import create_sql_chain
from backend.schema_context import get_schema_context
from backend.sql_cleaner import clean_sql
from backend.sql_validator import validate_query
from backend.query_executor import execute_query

chain = create_sql_chain()

schema = get_schema_context()

response = chain.invoke(
    {
        "schema": schema,
        "question": "Show first 5 artists"
    }
)

sql_query = clean_sql(response.content)

print("\nGenerated SQL:")
print(sql_query)

is_valid, message = validate_query(sql_query)

print("\nValidation:")
print(message)

if is_valid:

    results = execute_query(sql_query)

    print("\nResults:")

    for row in results:
        print(row)