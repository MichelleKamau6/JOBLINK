from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models import User, Booking, Payment, ProviderProfile
from utils.decorators import require_role
from datetime import datetime, timedelta

bp = Blueprint('analytics', __name__)

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
@require_role('admin')
def get_dashboard_stats():
    """Get Dashboard Analytics
    ---
    tags:
      - Analytics
    security:
      - Bearer: []
    responses:
      200:
        description: Dashboard statistics
    """
    # Basic counts
    total_users = User.query.count()
    total_providers = ProviderProfile.query.count()
    total_bookings = Booking.query.count()
    
    # Revenue calculations
    completed_payments = Payment.query.filter_by(status='completed').all()
    total_revenue = sum(p.amount for p in completed_payments)
    
    # Recent activity (last 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_bookings = Booking.query.filter(Booking.created_at >= thirty_days_ago).count()
    recent_users = User.query.filter(User.created_at >= thirty_days_ago).count()
    
    # Top categories
    category_stats = db.session.query(
        ProviderProfile.service_category_id,
        db.func.count(Booking.id).label('booking_count')
    ).join(Booking).group_by(ProviderProfile.service_category_id).all()
    
    return jsonify({
        'overview': {
            'total_users': total_users,
            'total_providers': total_providers,
            'total_bookings': total_bookings,
            'total_revenue': float(total_revenue)
        },
        'recent_activity': {
            'new_bookings_30d': recent_bookings,
            'new_users_30d': recent_users
        },
        'top_categories': [
            {'category_id': stat[0], 'booking_count': stat[1]} 
            for stat in category_stats
        ]
    })

@bp.route('/revenue', methods=['GET'])
@jwt_required()
@require_role('admin')
def get_revenue_analytics():
    """Get Revenue Analytics
    ---
    tags:
      - Analytics
    security:
      - Bearer: []
    responses:
      200:
        description: Revenue analytics
    """
    # Monthly revenue for last 12 months
    monthly_revenue = []
    for i in range(12):
        start_date = datetime.utcnow().replace(day=1) - timedelta(days=30*i)
        end_date = start_date + timedelta(days=31)
        
        revenue = db.session.query(db.func.sum(Payment.amount)).filter(
            Payment.status == 'completed',
            Payment.created_at >= start_date,
            Payment.created_at < end_date
        ).scalar() or 0
        
        monthly_revenue.append({
            'month': start_date.strftime('%Y-%m'),
            'revenue': float(revenue)
        })
    
    return jsonify({'monthly_revenue': monthly_revenue[::-1]})