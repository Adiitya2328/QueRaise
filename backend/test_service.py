from backend.service import process_question

response = process_question(
    "Show first 5 artists"
)

print(response)