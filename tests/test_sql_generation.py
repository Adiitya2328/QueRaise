from backend.sql_generator import generate_sql
from backend.schema_context import get_schema_context

# Read system prompt
with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()

# Get schema information
schema_context = get_schema_context()

# Combine prompt + schema
full_prompt = system_prompt + "\n\n" + schema_context

question = "Which customer has spent the most money?"

sql_query = generate_sql(full_prompt, question)

print(sql_query)