from backend.langchain_pipeline import run_nl_to_sql

questions = [
    "Show first 5 artists",
    "Show all superheroes",
    "Delete all artists"
]

for question in questions:

    print("\n" + "=" * 50)
    print("Question:", question)

    response = run_nl_to_sql(question)

    print("\nSuccess:")
    print(response["success"])

    print("\nMessage:")
    print(response["message"])

    print("\nSQL:")
    print(response["sql"])

    print("\nResults:")
    print(response["results"])