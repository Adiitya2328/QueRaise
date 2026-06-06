from backend.langchain_pipeline import run_nl_to_sql


def process_question(question):
    """
    Main application entry point.
    """

    return run_nl_to_sql(question)