from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Review, Booking, ProviderProfile

bp = Blueprint('reviews', __name__)

@bp.route('', methods=['POST'])
@jwt_required()
def create_review():
    """Create Review
    ---
    tags:
      - Reviews
    security:
      - Bearer: []
    parameters:
      - in: body
        name: review
        schema:
          type: object
          required:
            - booking_id
            - rating
          properties:
            booking_id:
              type: integer
            rating:
              type: integer
              minimum: 1
              maximum: 5
            comment:
              type: string
    responses:
      201:
        description: Review created successfully
    """
    user_id = int(get_jwt_identity())
    data = request.get_json()
    
    booking = Booking.query.get_or_404(data['booking_id'])
    
    if booking.client_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 403
    
    if booking.status != 'completed':
        return jsonify({'message': 'Can only review completed bookings'}), 400
    
    existing_review = Review.query.filter_by(booking_id=booking.id).first()
    if existing_review:
        return jsonify({'message': 'Review already exists for this booking'}), 400
    
    review = Review(
        booking_id=booking.id,
        provider_id=booking.provider_id,
        client_id=user_id,
        rating=data['rating'],
        comment=data.get('comment', '')
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify({'message': 'Review created successfully'}), 201

@bp.route('/provider/<int:provider_id>', methods=['GET'])
def get_provider_reviews(provider_id):
    """Get Provider Reviews
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: provider_id
        type: integer
        required: true
    responses:
      200:
        description: Provider reviews
    """
    reviews = Review.query.filter_by(provider_id=provider_id).all()
    
    return jsonify([{
        'id': r.id,
        'rating': r.rating,
        'comment': r.comment,
        'client_name': r.client.name,
        'created_at': r.created_at.isoformat()
    } for r in reviews])