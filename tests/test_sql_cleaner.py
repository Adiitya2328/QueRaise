from backend.sql_cleaner import clean_sql

query = """
```sql
SELECT * FROM artist;

"""

print(clean_sql(query))