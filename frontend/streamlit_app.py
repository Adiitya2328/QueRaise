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