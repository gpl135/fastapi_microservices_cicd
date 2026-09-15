from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["service"] == "payment-service"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "UP"


def test_create_payment():

    payment = {
        "order_id": 1,
        "amount": 2500
    }

    response = client.post(
        "/payments",
        json=payment
    )

    assert response.status_code == 200

    data = response.json()

    assert data["order_id"] == 1
    assert data["amount"] == 2500
    assert data["status"] == "SUCCESS"