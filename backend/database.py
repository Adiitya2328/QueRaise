import psycopg2
from backend.config import settings


def get_connection(
    host=None,
    port=None,
    database=None,
    user=None,
    password=None
):


    """
    Create PostgreSQL database connection.
    Uses custom details if provided, otherwise uses .env settings.
    """

    try:
        connection = psycopg2.connect(
            host=host or settings.DB_HOST,
            port=port or settings.DB_PORT,
            database=database or settings.DB_NAME,
            user=user or settings.DB_USER,
            password=password or settings.DB_PASSWORD
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