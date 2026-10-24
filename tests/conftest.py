import pytest
from fastapi.testclient import TestClient

from fastapi_se_deep_dive.app import app


@pytest.fixture
def client():
    return TestClient(app)
