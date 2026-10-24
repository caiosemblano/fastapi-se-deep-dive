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


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Redisiano',
            'email': 'redis@gmail.com',
            'password': 'caios secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'redis@gmail.com',
        'username': 'Redisiano',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(client.get('/users/').json()['users']) == 0
