from backend.sql_generator import generate_sql
from backend.schema_context import get_schema_context
from backend.sql_validator import validate_query
from backend.query_executor import execute_query

# Read system prompt
with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()

# Load schema
schema_context = get_schema_context()

full_prompt = system_prompt + "\n\n" + schema_context

question = "Show first 5 artists"

# Generate SQL
sql_query = generate_sql(full_prompt, question)

print("\nGenerated SQL:")
print(sql_query)

# Validate SQL
is_valid, message = validate_query(sql_query)

print("\nValidation Result:")
print(message)

if is_valid:

    results = execute_query(sql_query)

    print("\nResults:")

    for row in results[:5]:
        print(row)

else:
    print("\nExecution Blocked.")