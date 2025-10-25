#!/usr/bin/env python3
"""
Seed database with sample providers for testing search functionality
"""

from app import create_app
from extensions import db
from models import User, Role, ServiceCategory, ProviderProfile

def seed_providers():
    app = create_app()
    
    with app.app_context():
        # Create sample providers
        provider_role = Role.query.filter_by(name='provider').first()
        
        # Sample provider data
        providers_data = [
            {
                'name': 'John Mwangi',
                'email': 'john.cleaning@example.com',
                'business_name': 'John\'s Premium Cleaning',
                'category': 'Cleaning',
                'location': 'Nairobi',
                'rate': 2000,
                'description': 'Professional house and office cleaning services with eco-friendly products'
            },
            {
                'name': 'Sarah Wanjiku',
                'email': 'sarah.plumbing@example.com',
                'business_name': 'Sarah\'s Expert Plumbing',
                'category': 'Plumbing',
                'location': 'Kiambu',
                'rate': 3500,
                'description': 'Licensed plumber with 10+ years experience in residential and commercial plumbing'
            },
            {
                'name': 'David Kimani',
                'email': 'david.electric@example.com',
                'business_name': 'David\'s Electrical Solutions',
                'category': 'Electrical',
                'location': 'Nairobi',
                'rate': 4000,
                'description': 'Certified electrician specializing in home wiring and electrical repairs'
            },
            {
                'name': 'Grace Njeri',
                'email': 'grace.beauty@example.com',
                'business_name': 'Grace Beauty Studio',
                'category': 'Beauty',
                'location': 'Westlands',
                'rate': 1500,
                'description': 'Mobile beauty services including hair, nails, and makeup for all occasions'
            },
            {
                'name': 'Peter Ochieng',
                'email': 'peter.garden@example.com',
                'business_name': 'Peter\'s Garden Care',
                'category': 'Gardening',
                'location': 'Karen',
                'rate': 2500,
                'description': 'Professional landscaping and garden maintenance services'
            },
            {
                'name': 'Mary Akinyi',
                'email': 'mary.tutor@example.com',
                'business_name': 'Mary\'s Math Tutoring',
                'category': 'Tutoring',
                'location': 'Kilimani',
                'rate': 1800,
                'description': 'Experienced math tutor for primary and secondary school students'
            }
        ]
        
        for data in providers_data:
            # Check if user already exists
            existing_user = User.query.filter_by(email=data['email']).first()
            if existing_user:
                continue
                
            # Create user
            user = User(
                email=data['email'],
                name=data['name'],
                role_id=provider_role.id,
                is_verified=True
            )
            user.set_password('provider123')
            db.session.add(user)
            db.session.flush()
            
            # Get category
            category = ServiceCategory.query.filter_by(name=data['category']).first()
            
            # Create provider profile
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
        print(f"Seeded {len(providers_data)} sample providers!")

if __name__ == '__main__':
    seed_providers()