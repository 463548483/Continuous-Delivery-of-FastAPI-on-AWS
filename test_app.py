from fastapi.testclient import TestClient
from app import app


def test_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, this is page to make prediction"}


def test_predict():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "sepal_length": 1.0,
                "sepal_width": 2.0,
                "petal_length": 3.0,
                "petal_width": 4.0,
            },
        )
        assert response.status_code == 200
        assert response.json() == {"class": "virginica"}
