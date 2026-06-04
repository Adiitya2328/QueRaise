from backend.config import settings

print("DB_HOST:", settings.DB_HOST)
print("DB_NAME:", settings.DB_NAME)
print("DB_USER:", settings.DB_USER)
print("DB_PASSWORD:", settings.DB_PASSWORD)

from backend.database import get_connection

connection = get_connection()

if connection:
    print("✅ Connection Test Passed")
    connection.close()
else:
    print("❌ Connection Test Failed")