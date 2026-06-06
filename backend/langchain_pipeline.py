from backend.langchain_sql_generator import create_sql_chain
from backend.schema_context import get_schema_context
from backend.sql_cleaner import clean_sql
from backend.sql_validator import validate_query
from backend.query_executor import execute_query


def run_nl_to_sql(question):
    """
    Complete NL-to-SQL workflow.
    """

    try:

        schema = get_schema_context()

        chain = create_sql_chain()

        response = chain.invoke(
            {
                "schema": schema,
                "question": question
            }
        )

        sql_query = clean_sql(response.content)

        is_valid, message = validate_query(sql_query)

        if not is_valid:
            return {
                "success": False,
                "message": message,
                "sql": sql_query,
                "results": None
            }

        results = execute_query(sql_query)

        return {
            "success": True,
            "message": message,
            "sql": sql_query,
            "results": results
        }

    except Exception:

        return {
            "success": False,
            "message": "LLM unavailable or quota exceeded.",
            "sql": None,
            "results": None
        }