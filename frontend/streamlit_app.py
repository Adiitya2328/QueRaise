import streamlit as st
import requests


st.set_page_config(
    page_title="QueRaise",
    page_icon="🤖"
)

st.title("🤖 QueRaise — Ask in English. Get Real Data.")

st.write(
    "Skip the syntax. Powered by LLM + LangChain — type any question, QueRaise generates SQL, runs it live on PostgreSQL, and returns real results instantly. Read-only. Safe. Fast."
)

# ---------------------------
# Database Connection Sidebar
# ---------------------------

st.sidebar.header("Database Connection")

db_host = st.sidebar.text_input(
    "Host",
    value="localhost"
)

db_port = st.sidebar.text_input(
    "Port",
    value="5432"
)

db_name = st.sidebar.text_input(
    "Database Name"
)

db_user = st.sidebar.text_input(
    "Database Username"
)

db_password = st.sidebar.text_input(
    "Password",
    type="password"
)

connect_clicked = st.sidebar.button(
    "Connect"
)

if connect_clicked:

    response = requests.post(
        "http://127.0.0.1:8000/test-connection",
        json={
            "host": db_host,
            "port": int(db_port),
            "database": db_name,
            "user": db_user,
            "password": db_password
        }
    )

    data = response.json()

    if data["success"]:

        st.session_state["db_config"] = {
            "host": db_host,
            "port": int(db_port),
            "database": db_name,
            "user": db_user,
            "password": db_password
        }

        st.sidebar.success(
            f"Connected to {db_name}"
        )

    else:

        st.sidebar.error(
            "Connection Failed"
        )

# ---------------------------
# Question Input
# ---------------------------

question = st.text_input(
    "Enter your question:"
)

if st.button("Ask QueRaise"):

    if "db_config" not in st.session_state:

        st.error(
            "Please connect to a database first."
        )

    elif not question:

        st.warning(
            "Please enter a question."
        )

    else:

        response = requests.post(
            "http://127.0.0.1:8000/query",
            json={
                "question": question,
                "host": st.session_state["db_config"]["host"],
                "port": st.session_state["db_config"]["port"],
                "database": st.session_state["db_config"]["database"],
                "user": st.session_state["db_config"]["user"],
                "password": st.session_state["db_config"]["password"]
            }
        )

        data = response.json()

        st.subheader("Status")
        st.write(data["message"])

        st.subheader("Generated SQL")
        st.code(
            data["sql"],
            language="sql"
        )

        st.subheader("Results")

        if data["results"]:
            st.table(data["results"])
        else:
            st.write("No results found.")