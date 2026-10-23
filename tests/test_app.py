from fastapi.testclient import TestClient

from fastapi_se_deep_dive.app import app




def test_app():
    """
    3 steps test (AAA) for main (app)
    A: Arrange
    A: Act
    A: Assert
    """

    #Arrange
    client = TestClient(app)

    #Act
    response = client.get('/')

    #Assert
    assert response.json() == {'message': 'Hello World'}
