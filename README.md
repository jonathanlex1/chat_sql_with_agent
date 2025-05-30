# SQL Chatbot with Agent Built with Langchain and Streamlit

This project is an LLM-powered chatbot application that allows users to ask questions in natural language and receive answers along with the corresponding SQL queries based on their local database. It's built using Langchain, Streamlit, and open-source models served via Groq.

## Key Features

- Powered by the **open-source LLM `meta-llama/llama-4-scout-17b-16e-instruct`** via **Groq API**
- Built with **Langchain** and connected to your local RDBMS
- The agent interprets user questions and generates relevant **SQL queries**
- Supports two types of relational databases:
  - **MySQL**
  - **SQL Server** (via ODBC on Windows)


## How to Use This App

### 1. Clone the Repository

```bash
git clone https://github.com/jonathanlex1/chat_sql_with_agent
cd app.py
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Configure Database Connection

**For SQL Server:**
You will need:

- Server name (e.g., LAPTOP-XXXX\SQLEXPRESS)
- Database name (e.g., coffee_sales_db)
- Either use a trusted connection or provide your SQL login credentials

**For MySQL:**
You will need:

- host (e.g., localhost)
- username and password
- database name

These configurations can be entered in the script or via the Streamlit interface.

## Run and Ask Questions 
```bash
streamlit run app.py
```
Then:

1. Enter your database configuration

2. Ask questions like:

    - "How much was the total profit in Q1 2024?"

    - "Which product had the highest sales last month?"

3. The LLM will answer and display the generated SQL query

## Technologies Used 
- Langchain
- Groq API
- Streamlit
- SQLAlchemy
- PyODBC for SQL Server
- mysql-connector-python for MySQL

## Notes 
- Ensure you have installed the correct ODBC driver, e.g., ODBC Driver 17 for SQL Server

- The model 'meta-llama/llama-4-scout-17b-16e-instruct' must be accessible through Groq API

- Your MySQL and SQL Server instances must be running and accessible from Python