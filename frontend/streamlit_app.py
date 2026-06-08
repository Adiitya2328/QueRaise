import streamlit as st
import requests


st.set_page_config(
    page_title="QueRaise",
    page_icon="🤖"
)

st.title("🤖 QueRaise AI SQL Generator")

st.write(
    "Ask questions about your database using natural language."
)

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
    "Database",
    value="chinook"
)

db_user = st.sidebar.text_input(
    "Username",
    value="postgres"
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
if "db_config" in st.session_state:
    st.sidebar.write("Database Saved")        
question = st.text_input(
    "Enter your question:"
)

if st.button("Generate Query"):

    if question:

        response = requests.post(
            "http://127.0.0.1:8000/query",
            json={
                "question": question
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