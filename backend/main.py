from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import datetime
import pandas as pd
import os

app = FastAPI()

# Paths inside container (mapped via docker-compose)
DB_PATH = "data/expenses.db"
EXPORT_PATH = "exports/transportation_expenses.xlsx"

# Ensure folders exist
os.makedirs("data", exist_ok=True)
os.makedirs("exports", exist_ok=True)


class Expense(BaseModel):
    amount: float
    category: str
    notes: str = ""


def init_db():
    conn = sqlite3.connect(DB_PATH)  # use DB_PATH
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()


# Initialize DB
init_db()


@app.post("/expenses")
def add_expense(expense: Expense):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    date = datetime.date.today().strftime("%Y-%m-%d")
    c.execute(
        "INSERT INTO expenses (date, amount, category, notes) VALUES (?, ?, ?, ?)",
        (date, expense.amount, expense.category, expense.notes)
    )
    conn.commit()
    conn.close()
    return {"message": "Expense added"}


@app.get("/expenses")
def get_expenses():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    conn.close()
    return {"expenses": rows}


@app.get("/export")
def export_expenses():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df.to_excel(EXPORT_PATH, index=False)  # save in mapped exports folder
    conn.close()
    return {"message": f"Exported to {EXPORT_PATH}"}
