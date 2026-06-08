from backend.langchain_sql_generator import create_prompt_template

prompt = create_prompt_template()

result = prompt.invoke(
    {
        "schema": "artist(artist_id, name)",
        "question": "Show first 5 artists"
    }
)

print(result.text)