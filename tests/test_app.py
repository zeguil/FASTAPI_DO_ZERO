from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_main_return_OK_e_ola_mundo_():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'msg': 'ola mundo'}
