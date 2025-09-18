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

## Adding Data

Example JSON for adding an expense:

```json
{
  "amount": 120,
  "category": "Grab",
  "notes": "Office commute"
}
