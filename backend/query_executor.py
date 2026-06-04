from backend.database import get_connection


def execute_query(query):
    """
    Execute SQL query and return results.
    """

    connection = get_connection()

    if not connection:
        return None

    try:
        cursor = connection.cursor()

        cursor.execute(query)

        results = cursor.fetchall()

        return results

    except Exception as e:
        print(f"Query Error: {e}")
        return None

    finally:
        connection.close()