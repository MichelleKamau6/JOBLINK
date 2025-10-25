# Add this to app.py temporarily to seed data after deployment

@app.route('/seed-data')
def seed_data():
    from models import User, Role, ServiceCategory, ProviderProfile
    
    provider_role = Role.query.filter_by(name='provider').first()
    
    providers_data = [
        {
            'name': 'John Mwangi',
            'email': 'john.cleaning@example.com',
            'business_name': 'John\'s Premium Cleaning',
            'category': 'Cleaning',
            'location': 'Nairobi',
            'rate': 2000,
            'description': 'Professional house and office cleaning services'
        },
        # Add other providers...
    ]
    
    for data in providers_data:
        if User.query.filter_by(email=data['email']).first():
            continue
            
        user = User(
            email=data['email'],
            name=data['name'],
            role_id=provider_role.id,
            is_verified=True
        )
        user.set_password('provider123')
        db.session.add(user)
        db.session.flush()
        
        category = ServiceCategory.query.filter_by(name=data['category']).first()
        
        provider = ProviderProfile(
            user_id=user.id,
            service_category_id=category.id,
            business_name=data['business_name'],
            description=data['description'],
            location=data['location'],
            hourly_rate=data['rate'],
            is_active=True
        )
        db.session.add(provider)
    
    db.session.commit()
    return {'message': 'Data seeded successfully!'}