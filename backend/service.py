from backend.langchain_pipeline import run_nl_to_sql


def process_question(
    question,
    host,
    port,
    database,
    user,
    password
):
    """
    Main application entry point.
    """

    return run_nl_to_sql(
        question=question,
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )