# 🚀 QueRaise

### AI-Powered Natural Language to SQL Query Generator

Transform plain English questions into executable SQL queries using AI, PostgreSQL, FastAPI, and Streamlit.

---

## 📌 Project Overview

QueRaise allows users to ask questions in natural language such as:

> "Show the top 10 customers by revenue"

and automatically:

```text
Natural Language
        ↓
AI Model
        ↓
Generated SQL
        ↓
PostgreSQL Database
        ↓
Results & Visualizations
```

---

## 🎯 Project Goal

Build an end-to-end AI-powered analytics assistant capable of:

* Understanding natural language
* Generating SQL queries
* Executing queries safely
* Returning tabular results
* Creating visual insights automatically

---

## 🛠️ Tech Stack

| Layer                  | Technology    |
| ---------------------- | ------------- |
| Database               | PostgreSQL 18 |
| Backend                | FastAPI       |
| Frontend               | Streamlit     |
| AI Model               | Google Gemini |
| Data Processing        | Pandas        |
| Database Driver        | psycopg2      |
| Environment Management | python-dotenv |
| Version Control        | Git + GitHub  |

---

## 📂 Project Structure

```text
QueRaise/

├── backend/
│   ├── app.py
│   ├── database.py
│   └── config.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   └── Chinook_PostgreSql.sql
│
├── prompts/
├── logs/
├── tests/
├── docker/
│
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## 🗄️ Database

This project currently uses the **Chinook Sample Database**.

### Tables

* Artist
* Album
* Track
* Customer
* Employee
* Invoice
* InvoiceLine
* Genre
* Playlist
* PlaylistTrack
* MediaType

### Dataset Statistics

| Table          | Records |
| -------------- | ------: |
| Artist         |     275 |
| Album          |     347 |
| Track          |    3503 |
| Customer       |      59 |
| Invoice        |     412 |
| Invoice Line   |    2240 |
| Playlist       |      18 |
| Playlist Track |    8715 |

---

## 🗺️ Development Roadmap

- [x] Phase 1 — Database Setup
- [x] Phase 2 — Database Connection
- [ ] Phase 3 — Query Execution Layer
- [ ] Phase 4 — AI SQL Generation
- [ ] Phase 5 — FastAPI Backend
- [ ] Phase 6 — Streamlit Frontend
- [ ] Phase 7 — Charts & Analytics
- [ ] Phase 8 — Docker & Deployment

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.

---



```
```

