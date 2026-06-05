from backend.query_executor import execute_query


def get_schema_context():
    """
    Get table and column information from PostgreSQL.
    """

    query = """
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position;
    """

    results = execute_query(query)

    schema_text = "Database Schema:\n"

    current_table = None

    for table_name, column_name in results:
        if table_name != current_table:
            current_table = table_name
            schema_text += f"\nTable: {table_name}\n"

        schema_text += f"- {column_name}\n"

    return schema_text