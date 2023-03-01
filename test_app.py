import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert len(response.json) == 3

def test_get_user(client):
    response = client.get('/api/users/1')
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'

def test_get_user_not_found(client):
    response = client.get('/api/users/4')
    assert response.status_code == 404
    assert response.json['error'] == 'User not found'

def test_add_user(client):
    new_user = {'name': 'Alice Brown', 'age': 35}
    response = client.post('/api/users', json=new_user)
    assert response.status_code == 201
    assert response.json['name'] == 'Alice Brown'
