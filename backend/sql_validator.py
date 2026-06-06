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



from backend.schema_validator import validate_tables


def validate_query(sql_query):
    """
    Perform full SQL validation.
    """

    query_type = classify_query(sql_query)

    # Version 1 = READ ONLY

    if query_type != "READ":
        return False, "Only SELECT queries are allowed."

    if not validate_tables(sql_query):
        return False, "Invalid table detected."

    return True, "Query validated successfully."
