import pytest
from unittest.mock import patch, MagicMock
from services.email_service import EmailService
from services.mpesa_service import MPesaService

class TestEmailService:
    def test_send_booking_confirmation(self):
        """Test booking confirmation email"""
        with patch('app.services.email_service.SendGridAPIClient') as mock_sg:
            email_service = EmailService()
            
            booking_data = {
                'client_email': 'client@test.com',
                'client_name': 'Test Client',
                'provider_email': 'provider@test.com',
                'provider_name': 'Test Provider',
                'service_date': '2024-01-15T10:00:00',
                'duration_hours': 2,
                'total_amount': 50.0,
                'notes': 'Test booking'
            }
            
            result = email_service.send_booking_confirmation(booking_data)
            assert result == True
            assert mock_sg.return_value.send.call_count == 2  # Client + Provider emails

    def test_send_verification_email(self):
        """Test verification email"""
        with patch('app.services.email_service.SendGridAPIClient') as mock_sg:
            email_service = EmailService()
            
            result = email_service.send_verification_email('test@example.com', 'test-token')
            assert result == True
            mock_sg.return_value.send.assert_called_once()

class TestMPesaService:
    def test_generate_password(self):
        """Test M-Pesa password generation"""
        mpesa_service = MPesaService()
        password, timestamp = mpesa_service.generate_password()
        
        assert password is not None
        assert timestamp is not None
        assert len(timestamp) == 14  # YYYYMMDDHHMMSS format

    @patch('app.services.mpesa_service.requests.get')
    def test_get_access_token(self, mock_get):
        """Test M-Pesa access token retrieval"""
        mock_response = MagicMock()
        mock_response.json.return_value = {'access_token': 'test-token'}
        mock_get.return_value = mock_response
        
        mpesa_service = MPesaService()
        token = mpesa_service.get_access_token()
        
        assert token == 'test-token'

    @patch('app.services.mpesa_service.requests.post')
    @patch('app.services.mpesa_service.MPesaService.get_access_token')
    def test_initiate_stk_push(self, mock_token, mock_post):
        """Test STK Push initiation"""
        mock_token.return_value = 'test-token'
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'ResponseCode': '0',
            'CheckoutRequestID': 'test-checkout-id',
            'MerchantRequestID': 'test-merchant-id'
        }
        mock_post.return_value = mock_response
        
        mpesa_service = MPesaService()
        result = mpesa_service.initiate_stk_push(
            phone_number='254700000000',
            amount=100,
            account_reference='TEST-REF',
            transaction_desc='Test payment'
        )
        
        assert result['success'] == True
        assert 'checkout_request_id' in result