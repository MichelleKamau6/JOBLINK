from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from extensions import db
from models import Booking, ProviderProfile, Payment
from services.email_service import email_service

bp = Blueprint('bookings', __name__)

@bp.route('', methods=['POST'])
@jwt_required()
def create_booking():
    """Create New Booking
    ---
    tags:
      - Bookings
    security:
      - Bearer: []
    parameters:
      - in: body
        name: booking
        schema:
          type: object
          required:
            - provider_id
            - service_date
            - duration_hours
          properties:
            provider_id:
              type: integer
            service_date:
              type: string
              format: date-time
            duration_hours:
              type: integer
            notes:
              type: string
    responses:
      201:
        description: Booking created successfully
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    
    provider = ProviderProfile.query.get_or_404(data['provider_id'])
    service_date = datetime.fromisoformat(data['service_date'])
    duration = data['duration_hours']
    total_amount = provider.hourly_rate * duration
    
    booking = Booking(
        client_id=user_id,
        provider_id=provider.id,
        service_date=service_date,
        duration_hours=duration,
        total_amount=total_amount,
        notes=data.get('notes', '')
    )
    
    db.session.add(booking)
    db.session.commit()
    
    return jsonify({
        'message': 'Booking created successfully',
        'booking_id': booking.id,
        'total_amount': total_amount
    }), 201

@bp.route('', methods=['GET'])
@jwt_required()
def get_bookings():
    """Get User Bookings
    ---
    tags:
      - Bookings
    security:
      - Bearer: []
    responses:
      200:
        description: List of user bookings
    """
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(client_id=user_id).all()
    
    return jsonify([{
        'id': b.id,
        'provider_name': b.provider.business_name,
        'service_date': b.service_date.isoformat(),
        'duration_hours': b.duration_hours,
        'total_amount': b.total_amount,
        'status': b.status,
        'created_at': b.created_at.isoformat()
    } for b in bookings])

@bp.route('/<int:booking_id>/status', methods=['PUT'])
@jwt_required()
def update_booking_status():
    """Update Booking Status
    ---
    tags:
      - Bookings
    security:
      - Bearer: []
    parameters:
      - in: path
        name: booking_id
        type: integer
        required: true
      - in: body
        name: status
        schema:
          type: object
          required:
            - status
          properties:
            status:
              type: string
              enum: [confirmed, completed, cancelled]
    responses:
      200:
        description: Status updated successfully
    """
    booking_id = request.view_args['booking_id']
    data = request.get_json()
    
    booking = Booking.query.get_or_404(booking_id)
    booking.status = data['status']
    
    db.session.commit()
    
    return jsonify({'message': 'Booking status updated successfully'})