import pytest
import json
from app import create_app
from extensions import db
from models import User, Role, ServiceCategory, ProviderProfile, Booking

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        
        # Create test data if they don't exist
        if not Role.query.filter_by(name='client').first():
            client_role = Role(name='client')
            db.session.add(client_role)
        if not Role.query.filter_by(name='provider').first():
            provider_role = Role(name='provider')
            db.session.add(provider_role)
        if not ServiceCategory.query.filter_by(name='Cleaning').first():
            category = ServiceCategory(name='Cleaning')
            db.session.add(category)
        db.session.commit()
        
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_booking(client):
    """Test booking creation"""
    # Register users
    client.post('/api/auth/register', json={
        'email': 'client@test.com',
        'password': 'password123',
        'name': 'Test Client',
        'role': 'client'
    })
    
    client.post('/api/auth/register', json={
        'email': 'provider@test.com',
        'password': 'password123',
        'name': 'Test Provider',
        'role': 'provider'
    })
    
    # Login client
    response = client.post('/api/auth/login', json={
        'email': 'client@test.com',
        'password': 'password123'
    })
    client_token = json.loads(response.data)['token']
    
    # Login provider and create profile
    response = client.post('/api/auth/login', json={
        'email': 'provider@test.com',
        'password': 'password123'
    })
    provider_token = json.loads(response.data)['token']
    
    client.post('/api/providers', 
                headers={'Authorization': f'Bearer {provider_token}'},
                json={
                    'business_name': 'Test Service',
                    'service_category_id': 1,
                    'location': 'Test City',
                    'hourly_rate': 25.0
                })
    
    # Create booking
    response = client.post('/api/bookings',
                          headers={'Authorization': f'Bearer {client_token}'},
                          json={
                              'provider_id': 1,
                              'service_date': '2024-12-25T10:00:00',
                              'duration_hours': 2
                          })
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'booking_id' in data