from backend.schema_validator import validate_tables

queries = [
    "SELECT * FROM artist;",
    "SELECT * FROM album;",
    "SELECT * FROM superman;"
]

for query in queries:

    result = validate_tables(query)

    print(f"{query} --> {result}")