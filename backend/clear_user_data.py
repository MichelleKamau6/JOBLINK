#!/usr/bin/env python3
"""
Script to clear user data from the database
Useful for starting fresh during development
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from extensions import db
from models import User, Booking, Payment, Review, ProviderProfile

def clear_user_data(email=None):
    """
    Clear user data from database
    If email is provided, only clear that specific user
    Otherwise, clear all users except admin
    """
    app = create_app()
    
    with app.app_context():
        if email:
            # Clear specific user
            user = User.query.filter_by(email=email).first()
            if user:
                print(f"Found user: {user.email}")
                
                # Delete related data
                Booking.query.filter_by(client_id=user.id).delete()
                Review.query.filter_by(client_id=user.id).delete()
                Payment.query.filter(Payment.booking_id.in_(
                    db.session.query(Booking.id).filter_by(client_id=user.id)
                )).delete(synchronize_session=False)
                
                # Delete provider profile if exists
                ProviderProfile.query.filter_by(user_id=user.id).delete()
                
                # Delete user
                db.session.delete(user)
                db.session.commit()
                
                print(f"✅ Successfully deleted user: {email}")
            else:
                print(f"❌ User not found: {email}")
        else:
            # Clear all non-admin users
            users = User.query.filter(User.email != 'admin@joblink.com').all()
            count = len(users)
            
            for user in users:
                # Delete related data
                Booking.query.filter_by(client_id=user.id).delete()
                Review.query.filter_by(client_id=user.id).delete()
                ProviderProfile.query.filter_by(user_id=user.id).delete()
                db.session.delete(user)
            
            db.session.commit()
            print(f"✅ Successfully deleted {count} users (kept admin)")

def list_users():
    """List all users in the database"""
    app = create_app()
    
    with app.app_context():
        users = User.query.all()
        print("\n📋 Current users in database:")
        print("-" * 60)
        for user in users:
            # Get role name - handle both relationship and direct attribute
            if hasattr(user.role, 'name'):
                role_name = user.role.name
            elif isinstance(user.role, str):
                role_name = user.role
            else:
                role_name = 'No role'
            print(f"Email: {user.email:30} | Role: {role_name:10} | ID: {user.id}")
        print("-" * 60)
        print(f"Total: {len(users)} users\n")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Clear user data from database')
    parser.add_argument('--email', type=str, help='Specific email to delete')
    parser.add_argument('--list', action='store_true', help='List all users')
    parser.add_argument('--all', action='store_true', help='Delete all non-admin users')
    
    args = parser.parse_args()
    
    if args.list:
        list_users()
    elif args.email:
        clear_user_data(args.email)
        list_users()
    elif args.all:
        confirm = input("⚠️  This will delete ALL non-admin users. Continue? (yes/no): ")
        if confirm.lower() == 'yes':
            clear_user_data()
            list_users()
        else:
            print("Cancelled.")
    else:
        print("Usage:")
        print("  List users:           python clear_user_data.py --list")
        print("  Delete specific user: python clear_user_data.py --email user@example.com")
        print("  Delete all users:     python clear_user_data.py --all")
