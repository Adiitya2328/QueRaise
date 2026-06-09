from backend.schema_validator import validate_tables


def classify_query(sql_query):
    """
    Classify SQL query type.
    """

    query = sql_query.strip().upper()

    if query.startswith("SELECT"):
        return "READ"

    elif query.startswith(("INSERT", "UPDATE", "DELETE")):
        return "WRITE"

    elif query.startswith(("DROP", "TRUNCATE", "ALTER")):
        return "BLOCKED"

    else:
        return "UNKNOWN"


def validate_query(
    sql_query,
    host,
    port,
    database,
    user,
    password
):
    """
    Perform full SQL validation.
    """

    query_type = classify_query(sql_query)

    if query_type != "READ":
        return False, "Only SELECT queries are allowed."

    if not validate_tables(
        sql_query,
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    ):
        return False, "Invalid table detected."

    return True, "Query validated successfully."