from http import HTTPStatus


def test_app(client):
    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'Caio',
            'email': 'caio@gmail.com',
            'password': 'caios secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'caio@gmail.com',
        'username': 'Caio',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'caio@gmail.com',
                'username': 'Caio',
            }
        ]
    }
