from backend.query_executor import execute_query
from backend.utils import print_results

query = """
SELECT name
FROM artist
LIMIT 5;
"""

results = execute_query(query)

print_results(results)