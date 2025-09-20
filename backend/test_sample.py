import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# --- Health check ---
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] in ["OK", "Service up", "Running"]

# --- GET expenses (should return a list, even if empty) ---
def test_get_expenses_empty():
    response = client.get("/expenses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# --- POST an expense ---
def test_add_expense():
    payload = {
        "category": "transportation",
        "amount": 15.5,
        "description": "Bus fare"
    }
    response = client.post("/expenses", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["category"] == payload["category"]
    assert data["amount"] == payload["amount"]

# --- GET expenses should now return at least one item ---
def test_get_expenses_after_insert():
    response = client.get("/expenses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "category" in data[0]
    assert "amount" in data[0]
