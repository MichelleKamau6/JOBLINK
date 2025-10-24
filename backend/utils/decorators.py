from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models import User

def require_role(required_role):
    """Decorator to require specific user role"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            
            if not user or user.role != required_role:
                return jsonify({'message': f'{required_role} access required'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def require_roles(*roles):
    """Decorator to require one of multiple roles"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            
            if not user or user.role not in roles:
                return jsonify({'message': 'Insufficient permissions'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator