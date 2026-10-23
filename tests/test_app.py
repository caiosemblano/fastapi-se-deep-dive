from fastapi.testclient import TestClient

from fastapi_se_deep_dive.app import app

client = TestClient(app)


def test_app():
    response = client.get("/")

    assert response.json() == {"message": "Hello World"}
