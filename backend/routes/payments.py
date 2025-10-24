from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from extensions import db
from models import Payment, Booking
from services.mpesa_service import mpesa_service
from services.email_service import email_service

bp = Blueprint('payments', __name__)

@bp.route('/initiate', methods=['POST'])
@jwt_required()
def initiate_payment():
    """Initiate M-Pesa Payment
    ---
    tags:
      - Payments
    security:
      - Bearer: []
    parameters:
      - in: body
        name: payment
        schema:
          type: object
          required:
            - booking_id
            - phone_number
          properties:
            booking_id:
              type: integer
            phone_number:
              type: string
    responses:
      200:
        description: Payment initiated successfully
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    
    booking = Booking.query.get_or_404(data['booking_id'])
    
    if booking.client_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 403
    
    # Create payment record
    payment = Payment(
        booking_id=booking.id,
        amount=booking.total_amount,
        payment_method='mpesa'
    )
    db.session.add(payment)
    db.session.commit()
    
    # Initiate M-Pesa STK Push
    result = mpesa_service.initiate_stk_push(
        phone_number=data['phone_number'],
        amount=booking.total_amount,
        account_reference=f'BOOKING-{booking.id}',
        transaction_desc=f'Payment for booking {booking.id}'
    )
    
    if result['success']:
        payment.transaction_id = result.get('checkout_request_id')
        db.session.commit()
        
        return jsonify({
            'message': 'Payment initiated successfully',
            'payment_id': payment.id,
            'checkout_request_id': result.get('checkout_request_id')
        })
    else:
        payment.status = 'failed'
        db.session.commit()
        return jsonify({'message': result['message']}), 400

@bp.route('/callback', methods=['POST'])
def payment_callback():
    """M-Pesa Payment Callback
    ---
    tags:
      - Payments
    parameters:
      - in: body
        name: callback_data
        schema:
          type: object
    responses:
      200:
        description: Callback processed
    """
    data = request.get_json()
    
    try:
        # Extract callback data
        stk_callback = data.get('Body', {}).get('stkCallback', {})
        result_code = stk_callback.get('ResultCode')
        checkout_request_id = stk_callback.get('CheckoutRequestID')
        
        # Find payment by transaction ID
        payment = Payment.query.filter_by(transaction_id=checkout_request_id).first()
        
        if payment:
            if result_code == 0:  # Success
                payment.status = 'completed'
                payment.completed_at = datetime.utcnow()
                
                # Update booking status
                booking = payment.booking
                booking.status = 'confirmed'
                
                # Send confirmation emails
                email_data = {
                    'client_email': booking.client.email,
                    'client_name': booking.client.name,
                    'provider_email': booking.provider.user.email,
                    'provider_name': booking.provider.business_name,
                    'service_date': booking.service_date.isoformat(),
                    'duration_hours': booking.duration_hours,
                    'total_amount': booking.total_amount,
                    'notes': booking.notes
                }
                email_service.send_booking_confirmation(email_data)
                
            else:  # Failed
                payment.status = 'failed'
            
            db.session.commit()
    
    except Exception as e:
        print(f"Callback processing error: {str(e)}")
    
    return jsonify({'message': 'Callback processed'})

@bp.route('/status/<int:payment_id>', methods=['GET'])
@jwt_required()
def get_payment_status(payment_id):
    """Get Payment Status
    ---
    tags:
      - Payments
    security:
      - Bearer: []
    parameters:
      - in: path
        name: payment_id
        type: integer
        required: true
    responses:
      200:
        description: Payment status
    """
    payment = Payment.query.get_or_404(payment_id)
    
    return jsonify({
        'id': payment.id,
        'status': payment.status,
        'amount': payment.amount,
        'created_at': payment.created_at.isoformat(),
        'completed_at': payment.completed_at.isoformat() if payment.completed_at else None
    })