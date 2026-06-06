from backend.sql_validator import classify_query

queries = [
    "SELECT * FROM artist;",
    "INSERT INTO artist VALUES (1, 'Test');",
    "UPDATE artist SET name='ABC';",
    "DELETE FROM artist;",
    "DROP TABLE artist;"
]

for query in queries:
    result = classify_query(query)

    print(f"{query} --> {result}")