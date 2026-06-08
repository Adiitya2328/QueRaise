from backend.database import test_connection

success = test_connection(
    host="localhost",
    port=5432,
    database="chinook",
    user="postgres",
    password="YOUR_PASSWORD"
)

if success:
    print("✅ Connection Test Passed")
else:
    print("❌ Connection Test Failed")