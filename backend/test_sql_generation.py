from backend.sql_generator import generate_sql

# Read system prompt
with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()

question = "Show first 5 artists"

sql_query = generate_sql(system_prompt, question)

print(sql_query)