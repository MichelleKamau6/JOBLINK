import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import current_app

class EmailService:
    def __init__(self):
        self.sg = SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
        self.from_email = os.getenv('FROM_EMAIL', 'noreply@joblink.com')
    
    def send_booking_confirmation(self, booking_data):
        """Send booking confirmation email to client and provider"""
        try:
            # Email to client
            client_message = Mail(
                from_email=self.from_email,
                to_emails=booking_data['client_email'],
                subject='Booking Confirmation - JobLink',
                html_content=f"""
                <h2>Booking Confirmed!</h2>
                <p>Your booking with {booking_data['provider_name']} has been confirmed.</p>
                <p><strong>Service Date:</strong> {booking_data['service_date']}</p>
                <p><strong>Duration:</strong> {booking_data['duration_hours']} hours</p>
                <p><strong>Total Amount:</strong> ${booking_data['total_amount']}</p>
                <p>Thank you for using JobLink!</p>
                """
            )
            
            # Email to provider
            provider_message = Mail(
                from_email=self.from_email,
                to_emails=booking_data['provider_email'],
                subject='New Booking Request - JobLink',
                html_content=f"""
                <h2>New Booking Request</h2>
                <p>You have a new booking request from {booking_data['client_name']}.</p>
                <p><strong>Service Date:</strong> {booking_data['service_date']}</p>
                <p><strong>Duration:</strong> {booking_data['duration_hours']} hours</p>
                <p><strong>Amount:</strong> ${booking_data['total_amount']}</p>
                <p><strong>Notes:</strong> {booking_data.get('notes', 'None')}</p>
                <p>Please log in to your dashboard to confirm or decline this booking.</p>
                """
            )
            
            self.sg.send(client_message)
            self.sg.send(provider_message)
            return True
            
        except Exception as e:
            current_app.logger.error(f"Email sending failed: {str(e)}")
            return False
    
    def send_verification_email(self, user_email, verification_token):
        """Send email verification"""
        try:
            message = Mail(
                from_email=self.from_email,
                to_emails=user_email,
                subject='Verify Your Email - JobLink',
                html_content=f"""
                <h2>Welcome to JobLink!</h2>
                <p>Please verify your email address by clicking the link below:</p>
                <a href="http://localhost:5173/verify-email?token={verification_token}">Verify Email</a>
                <p>If you didn't create an account, please ignore this email.</p>
                """
            )
            
            self.sg.send(message)
            return True
            
        except Exception as e:
            current_app.logger.error(f"Verification email failed: {str(e)}")
            return False

email_service = EmailService()