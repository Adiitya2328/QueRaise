from backend.langchain_pipeline import run_nl_to_sql

response = run_nl_to_sql(
    "Show first 5 artists"
)

print("\nSuccess:")
print(response["success"])

print("\nSQL:")
print(response["sql"])

print("\nResults:")

for row in response["results"]:
    print(row)