from http import HTTPStatus
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_links():

    links = {
        'links': [
            'testlink1.com',
            'testlink2.com',
        ],
    }

    response = client.post('/visited_links/', json=links)
    assert response.status_code == HTTPStatus.CREATED
