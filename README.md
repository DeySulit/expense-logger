# Transportation Expense Tracker

A containerized application to track transportation expenses and generate Excel reports.  
Built with **FastAPI**, **SQLite**, and **Docker**, this app lets you log daily transportation costs, view them, and export them as Excel spreadsheets.  

> 💡 Useful for documenting transportation expenses for **tax deductions or tax shield purposes**, helping you keep accurate records for filing.

---

## Features
- Add daily/weekly transportation expenses via API.
- View all recorded expenses.
- Export expenses to Excel (`.xlsx`) for reporting or tax documentation.
- Containerized with Docker and Docker Compose for easy deployment.
- Persistent data storage via Docker volumes.

---

## Project Structure
```bash
transportation-expense-tracker/
├── backend/ # FastAPI API code
├── data/ # SQLite DB (persistent storage)
├── exports/ # Excel exports
├── docker-compose.yml
├── README.md
└── .github/ # CI/CD pipelines (optional)
```
---

## Getting Started

### Requirements
- Docker
- Docker Compose

### Run the Application
From the project root:

```bash
docker-compose up --build -d
```

The API will be available at http://localhost:8000.

API Endpoints

POST /expenses → Add a new expense.

GET /expenses → Retrieve all expenses.

GET /export → Export all expenses to Excel (exports/transportation_expenses.xlsx).

You can also use the Swagger UI: http://localhost:8000/docs

---
## Adding Data

Example JSON for adding an expense:

```json
{
  "amount": 120,
  "category": "Grab",
  "notes": "Office commute"
}
```
---

## Exporting Data

Once you have added expenses, run:
```bash
curl http://localhost:8000/export
```

The Excel file will appear in the exports/ folder on your host machine.
