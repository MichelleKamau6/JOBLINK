import { useState } from 'react';
import { CreditCard, Shield, CheckCircle } from 'lucide-react';
import Button from '../components/Button';

export default function Payment() {
  const [paymentMethod, setPaymentMethod] = useState('mpesa');
  const [formData, setFormData] = useState({
    phone: '',
    amount: '2500',
    description: 'Plumbing Service - Kitchen Repair'
  });

  const handlePayment = () => {
    // Payment processing logic here
    console.log('Processing payment:', formData);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Complete Payment</h1>
          <p className="text-gray-600">Secure payment for your service booking</p>
        </div>

        {/* Payment Form */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          {/* Service Summary */}
          <div className="border-b border-gray-200 pb-6 mb-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Service Summary</h2>
            <div className="flex justify-between items-center">
              <div>
                <p className="font-medium text-gray-900">Plumbing Service</p>
                <p className="text-sm text-gray-600">Kitchen Repair - 2 hours</p>
                <p className="text-sm text-gray-600">Provider: John Smith</p>
              </div>
              <div className="text-right">
                <p className="text-2xl font-bold text-gray-900">KSh {formData.amount}</p>
                <p className="text-sm text-gray-600">Total Amount</p>
              </div>
            </div>
          </div>

          {/* Payment Method Selection */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Payment Method</h3>
            <div className="space-y-3">
              <label className="flex items-center p-4 border rounded-lg cursor-pointer hover:bg-gray-50">
                <input
                  type="radio"
                  name="payment"
                  value="mpesa"
                  checked={paymentMethod === 'mpesa'}
                  onChange={(e) => setPaymentMethod(e.target.value)}
                  className="mr-3"
                />
                <div className="flex-1">
                  <div className="flex items-center">
                    <div className="w-8 h-8 bg-green-600 rounded flex items-center justify-center mr-3">
                      <span className="text-white text-xs font-bold">M</span>
                    </div>
                    <span className="font-medium">M-Pesa</span>
                  </div>
                  <p className="text-sm text-gray-600 ml-11">Pay with your M-Pesa mobile money</p>
                </div>
              </label>

              <label className="flex items-center p-4 border rounded-lg cursor-pointer hover:bg-gray-50">
                <input
                  type="radio"
                  name="payment"
                  value="card"
                  checked={paymentMethod === 'card'}
                  onChange={(e) => setPaymentMethod(e.target.value)}
                  className="mr-3"
                />
                <div className="flex-1">
                  <div className="flex items-center">
                    <CreditCard className="w-8 h-8 text-blue-600 mr-3" />
                    <span className="font-medium">Credit/Debit Card</span>
                  </div>
                  <p className="text-sm text-gray-600 ml-11">Pay with Visa, Mastercard, or other cards</p>
                </div>
              </label>
            </div>
          </div>

          {/* Payment Details */}
          {paymentMethod === 'mpesa' && (
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                M-Pesa Phone Number
              </label>
              <input
                type="tel"
                value={formData.phone}
                onChange={(e) => setFormData({...formData, phone: e.target.value})}
                placeholder="254700123456"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <p className="text-sm text-gray-600 mt-1">
                You will receive an M-Pesa prompt on this number
              </p>
            </div>
          )}

          {paymentMethod === 'card' && (
            <div className="space-y-4 mb-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Card Number
                </label>
                <input
                  type="text"
                  placeholder="1234 5678 9012 3456"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Expiry Date
                  </label>
                  <input
                    type="text"
                    placeholder="MM/YY"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    CVV
                  </label>
                  <input
                    type="text"
                    placeholder="123"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
              </div>
            </div>
          )}

          {/* Security Notice */}
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
            <div className="flex items-start">
              <Shield className="w-5 h-5 text-blue-600 mr-3 mt-0.5" />
              <div>
                <h4 className="text-sm font-medium text-blue-900">Secure Payment</h4>
                <p className="text-sm text-blue-700">
                  Your payment information is encrypted and secure. We never store your card details.
                </p>
              </div>
            </div>
          </div>

          {/* Payment Button */}
          <Button 
            onClick={handlePayment}
            className="w-full py-4 text-lg"
          >
            <CheckCircle size={20} className="mr-2" />
            Pay KSh {formData.amount}
          </Button>

          {/* Terms */}
          <p className="text-xs text-gray-600 text-center mt-4">
            By completing this payment, you agree to our{' '}
            <a href="#" className="text-blue-600 hover:underline">Terms of Service</a>
            {' '}and{' '}
            <a href="#" className="text-blue-600 hover:underline">Privacy Policy</a>
          </p>
        </div>
      </div>
    </div>
  );
}