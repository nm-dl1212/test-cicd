import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "hello-world"}

def test_calc_success(client):
    response = client.get('/calc?a=3&b=4')
    assert response.status_code == 200
    assert response.get_json() == {"message": "multiple result is 12.0"}

def test_calc_missing_param(client):
    response = client.get('/calc?a=3')
    assert response.status_code == 400
    assert "error" in response.get_json()
