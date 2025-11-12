import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from app import create_app, db

@pytest.fixture
def client():
    """Fixture to provide a fresh test client and isolated in-memory database."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.drop_all()   # ensure no leftover tables from other tests
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_health_books(client):
    """Check that the /books endpoint returns 200 OK and empty list initially."""
    res = client.get('/api/v1/books/')
    assert res.status_code == 200
    assert res.json == []  # Expect no books yet

def test_register_and_login(client):
    """Register and then log in a user."""
    register_data = {"username": "testuser", "password": "12345"}
    res = client.post('/api/v1/auth/register', json=register_data)
    assert res.status_code == 201
    assert "user" in res.json

    login_data = {"username": "testuser", "password": "12345"}
    res = client.post('/api/v1/auth/login', json=login_data)
    assert res.status_code == 200
    assert "token" in res.json
