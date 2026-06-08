from backend.sql_validator import validate_query

queries = [
    "SELECT * FROM artist;",
    "SELECT * FROM superman;",
    "DROP TABLE artist;"
]

for query in queries:

    is_valid, message = validate_query(query)

    print(f"\nQuery: {query}")
    print("Valid:", is_valid)
    print("Message:", message)