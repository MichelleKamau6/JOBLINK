from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import User
from services.email_service import email_service
import secrets

bp = Blueprint('notifications', __name__)

@bp.route('/send-verification', methods=['POST'])
@jwt_required()
def send_verification_email():
    """Send Email Verification
    ---
    tags:
      - Notifications
    security:
      - Bearer: []
    responses:
      200:
        description: Verification email sent
    """
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    
    if user.is_verified:
        return jsonify({'message': 'Email already verified'}), 400
    
    # Generate verification token
    verification_token = secrets.token_urlsafe(32)
    
    # Store token in user record (you might want to add a verification_token field)
    # For now, we'll just send the email
    
    success = email_service.send_verification_email(user.email, verification_token)
    
    if success:
        return jsonify({'message': 'Verification email sent successfully'})
    else:
        return jsonify({'message': 'Failed to send verification email'}), 500

@bp.route('/verify-email', methods=['POST'])
def verify_email():
    """Verify Email Address
    ---
    tags:
      - Notifications
    parameters:
      - in: body
        name: verification
        schema:
          type: object
          required:
            - token
          properties:
            token:
              type: string
    responses:
      200:
        description: Email verified successfully
    """
    data = request.get_json()
    token = data.get('token')
    
    # TODO: Implement token validation logic
    # For now, just return success
    
    return jsonify({'message': 'Email verified successfully'})

@bp.route('/test-email', methods=['POST'])
@jwt_required()
def test_email():
    """Test Email Functionality
    ---
    tags:
      - Notifications
    security:
      - Bearer: []
    responses:
      200:
        description: Test email sent
    """
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    
    # Test booking confirmation email
    test_data = {
        'client_email': user.email,
        'client_name': user.name,
        'provider_email': 'provider@test.com',
        'provider_name': 'Test Provider',
        'service_date': '2024-01-15T10:00:00',
        'duration_hours': 2,
        'total_amount': 50.0,
        'notes': 'Test booking'
    }
    
    success = email_service.send_booking_confirmation(test_data)
    
    if success:
        return jsonify({'message': 'Test email sent successfully'})
    else:
        return jsonify({'message': 'Failed to send test email'}), 500