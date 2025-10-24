import pytest
import json
from app import create_app
from app.extensions import db
from app.models import User, Role, ServiceCategory, ProviderProfile

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        
        # Create roles and categories
        client_role = Role(name='client')
        provider_role = Role(name='provider')
        category = ServiceCategory(name='Cleaning', description='Cleaning services')
        db.session.add_all([client_role, provider_role, category])
        db.session.commit()
        
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(client):
    # Register and login a user
    client.post('/api/auth/register', json={
        'email': 'provider@example.com',
        'password': 'password123',
        'name': 'Test Provider',
        'role': 'provider'
    })
    
    response = client.post('/api/auth/login', json={
        'email': 'provider@example.com',
        'password': 'password123'
    })
    
    token = json.loads(response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_get_providers(client):
    """Test getting providers list"""
    response = client.get('/api/providers')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_create_provider_profile(client, auth_headers):
    """Test creating provider profile"""
    response = client.post('/api/providers', 
                          headers=auth_headers,
                          json={
                              'business_name': 'Clean Pro',
                              'service_category_id': 1,
                              'location': 'New York',
                              'hourly_rate': 25.0,
                              'description': 'Professional cleaning service'
                          })
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Provider profile created successfully'