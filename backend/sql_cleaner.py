def clean_sql(sql_query):
    """
    Clean Gemini output and return raw SQL.
    """

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")

    return sql_query.strip()