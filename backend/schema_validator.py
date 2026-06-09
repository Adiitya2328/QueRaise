from backend.query_executor import execute_query


def get_valid_tables(
    host,
    port,
    database,
    user,
    password
):
    """
    Get all table names from PostgreSQL.
    """

    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """

    results = execute_query(
        query,
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    return [row[0] for row in results]


def validate_tables(
    sql_query,
    host,
    port,
    database,
    user,
    password
):
    """
    Check whether SQL uses valid tables.
    """

    valid_tables = get_valid_tables(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    query = sql_query.lower()

    found_tables = []

    for table in valid_tables:
        if table in query:
            found_tables.append(table)

    if found_tables:
        return True

    return False