import psycopg2


def get_connection(
    host,
    port,
    database,
    user,
    password
):
    """
    Create PostgreSQL database connection.
    """

    try:

        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        return connection

    except Exception as e:

        print(f"Database connection failed: {e}")

        return None


def test_connection(
    host,
    port,
    database,
    user,
    password
):

    connection = get_connection(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    if connection:
        connection.close()
        return True

    return False