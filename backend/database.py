import psycopg2
from backend.config import settings


def get_connection():
    try:
        connection = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD
        )

        
        return connection

    except Exception as e:
        print(f"Database connection failed: {e}")
        return None