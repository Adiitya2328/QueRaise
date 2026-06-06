from backend.langchain_pipeline import run_nl_to_sql

response = run_nl_to_sql(
    "Show first 5 artists"
)

print(response)