from backend.sql_generator import generate_sql
from backend.query_executor import execute_query

# Read system prompt
with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()

question = "Show first 5 artists"

# Generate SQL
sql_query = generate_sql(system_prompt, question)

print("Generated SQL:")
print(sql_query)

# Execute SQL
results = execute_query(sql_query)

print("\nResults:")

for row in results:
    print(row)