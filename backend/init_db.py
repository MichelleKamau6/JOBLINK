#!/usr/bin/env python3
"""
Database initialization script for JobLink
Creates tables and seeds initial data
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from extensions import db
from models import Role, User, ServiceCategory

def init_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Create roles
        roles = ['client', 'provider', 'admin']
        for role_name in roles:
            if not Role.query.filter_by(name=role_name).first():
                role = Role(name=role_name)
                db.session.add(role)
        
        # Create service categories
        categories = [
            {'name': 'Cleaning', 'description': 'Home and office cleaning services'},
            {'name': 'Plumbing', 'description': 'Plumbing repairs and installations'},
            {'name': 'Electrical', 'description': 'Electrical repairs and installations'},
            {'name': 'Gardening', 'description': 'Garden maintenance and landscaping'},
            {'name': 'Handyman', 'description': 'General home repairs and maintenance'},
            {'name': 'Beauty', 'description': 'Beauty and wellness services'},
            {'name': 'Tutoring', 'description': 'Educational and tutoring services'},
            {'name': 'IT Support', 'description': 'Computer and technology support'}
        ]
        
        for cat_data in categories:
            if not ServiceCategory.query.filter_by(name=cat_data['name']).first():
                category = ServiceCategory(**cat_data)
                db.session.add(category)
        
        # Create admin user
        admin_role = Role.query.filter_by(name='admin').first()
        if not User.query.filter_by(email='admin@joblink.com').first():
            admin_user = User(
                email='admin@joblink.com',
                name='Admin User',
                role_id=admin_role.id,
                is_verified=True
            )
            admin_user.set_password('admin123')
            db.session.add(admin_user)
        
        # Create sample client
        client_role = Role.query.filter_by(name='client').first()
        if not User.query.filter_by(email='client@example.com').first():
            client_user = User(
                email='client@example.com',
                name='John Doe',
                role_id=client_role.id,
                is_verified=True
            )
            client_user.set_password('client123')
            db.session.add(client_user)
        
        db.session.commit()
        print("Database initialized successfully!")
        print("Admin user: admin@joblink.com / admin123")
        print("Client user: client@example.com / client123")

if __name__ == '__main__':
    init_database()