from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import User, Booking, Payment, ProviderProfile

bp = Blueprint('admin', __name__)

def require_admin():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    if not user or user.role != 'admin':
        return jsonify({'message': 'Admin access required'}), 403
    return None

@bp.route('/stats', methods=['GET'])
@jwt_required()
def get_stats():
    """Get Admin Statistics
    ---
    tags:
      - Admin
    security:
      - Bearer: []
    responses:
      200:
        description: Admin statistics
      403:
        description: Admin access required
    """
    admin_check = require_admin()
    if admin_check:
        return admin_check
    
    total_users = User.query.count()
    total_bookings = Booking.query.count()
    total_revenue = db.session.query(db.func.sum(Payment.amount)).filter_by(status='completed').scalar() or 0
    
    return jsonify({
        'total_users': total_users,
        'total_bookings': total_bookings,
        'total_revenue': float(total_revenue)
    })

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """Get All Users
    ---
    tags:
      - Admin
    security:
      - Bearer: []
    responses:
      200:
        description: List of all users
    """
    admin_check = require_admin()
    if admin_check:
        return admin_check
    
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'email': u.email,
        'name': u.name,
        'role': u.role,
        'is_verified': u.is_verified,
        'created_at': u.created_at.isoformat()
    } for u in users])

@bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    """Delete User
    ---
    tags:
      - Admin
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
    responses:
      200:
        description: User deleted successfully
    """
    admin_check = require_admin()
    if admin_check:
        return admin_check
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'})

@bp.route('/providers', methods=['GET'])
@jwt_required()
def get_all_providers():
    """Get All Providers for Admin
    ---
    tags:
      - Admin
    security:
      - Bearer: []
    responses:
      200:
        description: List of all providers
    """
    admin_check = require_admin()
    if admin_check:
        return admin_check
    
    providers = ProviderProfile.query.all()
    return jsonify([{
        'id': p.id,
        'business_name': p.business_name,
        'user_email': p.user.email,
        'category': p.category.name,
        'location': p.location,
        'is_active': p.is_active,
        'created_at': p.created_at.isoformat()
    } for p in providers])