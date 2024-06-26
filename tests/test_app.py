from http import HTTPStatus


def test_main_return_OK_e_ola_mundo_(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'msg': 'ola mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'UserTest',
            'password': 'password',
            'email': 'teste@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'UserTest',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'UserTest',
                'email': 'teste@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'UserTest2',
            'email': 'teste@test.com',
            'password': '123',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'UserTest2',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_update_user_nonexistent(client):
    response = client.put(
        '/users/9999',
        json={
            'username': 'NonExistentUser',
            'email': 'nonexistent@test.com',
            'password': '123',
            'id': 9999,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_nonexistent(client):
    response = client.delete('/users/9999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_user(client):
    client.post(
        '/users/',
        json={
            'username': 'UserTest',
            'password': '123',
            'email': 'teste@test.com',
        },
    )

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'UserTest',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_user_nonexistent(client):
    response = client.get('/users/9999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
