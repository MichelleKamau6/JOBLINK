import pytest
import json
from app import create_app
from app.extensions import db
from app.models import User, Role

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        
        # Create roles
        client_role = Role(name='client')
        admin_role = Role(name='admin')
        db.session.add_all([client_role, admin_role])
        db.session.commit()
        
        yield app
        
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register_user(client):
    """Test user registration"""
    response = client.post('/api/auth/register', 
                          json={
                              'email': 'test@example.com',
                              'password': 'password123',
                              'name': 'Test User'
                          })
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'User created successfully'

def test_login_user(client):
    """Test user login"""
    # First register a user
    client.post('/api/auth/register', 
                json={
                    'email': 'test@example.com',
                    'password': 'password123',
                    'name': 'Test User'
                })
    
    # Then login
    response = client.post('/api/auth/login',
                          json={
                              'email': 'test@example.com',
                              'password': 'password123'
                          })
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'token' in data
    assert data['user']['email'] == 'test@example.com'

def test_invalid_login(client):
    """Test login with invalid credentials"""
    response = client.post('/api/auth/login',
                          json={
                              'email': 'nonexistent@example.com',
                              'password': 'wrongpassword'
                          })
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'