from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_root() -> None:
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"status" : "Server running!"}


def test_statements_root() -> None:
    resp = client.get("/statements/")
    assert resp.status_code == 200
    assert resp.json() == {"status" : "Statements route running!"}


def test_quotes_root() -> None:
    resp = client.get("/quotes/")
    assert resp.status_code == 200
    assert resp.json() == {"status" : "Quotes route running!"}
