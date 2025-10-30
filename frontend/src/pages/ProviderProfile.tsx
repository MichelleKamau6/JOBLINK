import { useState } from 'react';
import { useAuth } from '../hooks/useAuthHook';
import { User, Mail, MapPin, DollarSign, Star, Award, Camera, Upload, Plus, Edit3 } from 'lucide-react';
import Button from '../components/Button';
import VerificationBadges from '../components/VerificationBadges';
import LocationPicker from '../components/LocationPicker';

export default function ProviderProfile() {
  const { user } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    name: user?.name || '',
    email: user?.email || '',
    phone: '+254 700 123 456',
    location: 'Nairobi, Kenya',
    bio: 'Professional service provider with 5+ years of experience in plumbing and home repairs.',
    hourlyRate: 2500,
    services: ['Plumbing', 'Pipe Repair', 'Bathroom Installation'],
    availability: {
      monday: true,
      tuesday: true,
      wednesday: true,
      thursday: true,
      friday: true,
      saturday: false,
      sunday: false
    }
  });

  const portfolio = [
    { id: 1, title: 'Kitchen Renovation', image: '/api/placeholder/300/200', description: 'Complete kitchen plumbing installation' },
    { id: 2, title: 'Bathroom Repair', image: '/api/placeholder/300/200', description: 'Fixed leaking pipes and installed new fixtures' },
    { id: 3, title: 'Water Heater Installation', image: '/api/placeholder/300/200', description: 'Installed and configured new water heating system' }
  ];

  const reviews = [
    { id: 1, client: 'Mary W.', rating: 5, comment: 'Excellent work! Very professional and punctual.', date: '2024-12-15' },
    { id: 2, client: 'John K.', rating: 4, comment: 'Good service, fair pricing. Would recommend.', date: '2024-12-10' },
    { id: 3, client: 'Sarah M.', rating: 5, comment: 'Fixed the problem quickly and explained everything clearly.', date: '2024-12-05' }
  ];

  const earnings = {
    thisMonth: 45000,
    lastMonth: 38000,
    totalEarnings: 250000,
    completedJobs: 48
  };

  const handleSave = () => {
    setIsEditing(false);
    // Save logic here
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-gradient-to-r from-green-600 to-blue-600 text-white">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="flex flex-col md:flex-row items-center gap-8">
            <div className="relative">
              <div className="w-32 h-32 bg-white rounded-full flex items-center justify-center text-gray-400 text-4xl shadow-lg">
                <User size={48} />
              </div>
              <button className="absolute bottom-2 right-2 bg-green-500 hover:bg-green-600 text-white p-2 rounded-full shadow-lg transition-colors">
                <Camera size={16} />
              </button>
            </div>
            
            <div className="text-center md:text-left flex-1">
              <h1 className="text-4xl font-bold mb-2">{user?.name || 'Provider Name'}</h1>
              <p className="text-green-100 text-lg mb-4">Professional Plumber • 5+ Years Experience</p>
              <div className="flex flex-wrap gap-4 justify-center md:justify-start mb-4">
                <div className="flex items-center gap-2">
                  <Mail size={16} />
                  <span>{user?.email}</span>
                </div>
                <div className="flex items-center gap-2">
                  <MapPin size={16} />
                  <span>{formData.location}</span>
                </div>
                <div className="flex items-center gap-2">
                  <DollarSign size={16} />
                  <span>KSh {formData.hourlyRate}/hr</span>
                </div>
              </div>
              <VerificationBadges 
                verifications={{
                  idVerified: true,
                  backgroundCheck: true,
                  insurance: true,
                  license: true
                }}
              />
            </div>
            
            <div className="flex flex-col gap-2">
              <Button 
                onClick={() => setIsEditing(!isEditing)}
                className="bg-white text-green-600 hover:bg-gray-100"
              >
                <Edit3 size={16} className="mr-2" />
                {isEditing ? 'Cancel' : 'Edit Profile'}
              </Button>
              <div className="text-center">
                <div className="flex items-center justify-center gap-1 mb-1">
                  <Star size={16} fill="currentColor" className="text-yellow-400" />
                  <span className="font-bold">4.8</span>
                  <span className="text-green-100">(24 reviews)</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-6">
            {/* Business Information */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Business Information</h2>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Business Name</label>
                  {isEditing ? (
                    <input
                      type="text"
                      value={formData.name}
                      onChange={(e) => setFormData({...formData, name: e.target.value})}
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    />
                  ) : (
                    <p className="text-gray-900 bg-gray-50 px-4 py-3 rounded-lg">{formData.name}</p>
                  )}
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Hourly Rate (KSh)</label>
                  {isEditing ? (
                    <input
                      type="number"
                      value={formData.hourlyRate}
                      onChange={(e) => setFormData({...formData, hourlyRate: parseInt(e.target.value)})}
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    />
                  ) : (
                    <p className="text-gray-900 bg-gray-50 px-4 py-3 rounded-lg">KSh {formData.hourlyRate}</p>
                  )}
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
                  {isEditing ? (
                    <input
                      type="tel"
                      value={formData.phone}
                      onChange={(e) => setFormData({...formData, phone: e.target.value})}
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    />
                  ) : (
                    <p className="text-gray-900 bg-gray-50 px-4 py-3 rounded-lg">{formData.phone}</p>
                  )}
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Service Area</label>
                  {isEditing ? (
                    <LocationPicker 
                      onLocationSelect={(location) => setFormData({...formData, location})}
                      currentLocation={formData.location}
                    />
                  ) : (
                    <p className="text-gray-900 bg-gray-50 px-4 py-3 rounded-lg">{formData.location}</p>
                  )}
                </div>
              </div>
              
              <div className="mt-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Professional Bio</label>
                {isEditing ? (
                  <textarea
                    value={formData.bio}
                    onChange={(e) => setFormData({...formData, bio: e.target.value})}
                    rows={4}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                  />
                ) : (
                  <p className="text-gray-900 bg-gray-50 px-4 py-3 rounded-lg">{formData.bio}</p>
                )}
              </div>

              {/* Services */}
              <div className="mt-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Services Offered</label>
                <div className="flex flex-wrap gap-2">
                  {formData.services.map((service, index) => (
                    <span key={index} className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-medium">
                      {service}
                    </span>
                  ))}
                  {isEditing && (
                    <button className="px-3 py-1 border-2 border-dashed border-green-300 text-green-600 rounded-full text-sm font-medium hover:bg-green-50">
                      <Plus size={14} className="inline mr-1" />
                      Add Service
                    </button>
                  )}
                </div>
              </div>
              
              {isEditing && (
                <div className="mt-6 flex gap-4">
                  <Button onClick={handleSave}>Save Changes</Button>
                  <Button variant="secondary" onClick={() => setIsEditing(false)}>Cancel</Button>
                </div>
              )}
            </div>

            {/* Portfolio */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900">Portfolio</h2>
                <Button size="sm">
                  <Upload size={16} className="mr-2" />
                  Add Work
                </Button>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {portfolio.map((item) => (
                  <div key={item.id} className="border border-gray-200 rounded-lg overflow-hidden">
                    <div className="h-48 bg-gray-200 flex items-center justify-center">
                      <span className="text-gray-500">Portfolio Image</span>
                    </div>
                    <div className="p-4">
                      <h3 className="font-semibold text-gray-900 mb-2">{item.title}</h3>
                      <p className="text-sm text-gray-600">{item.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Reviews */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Customer Reviews</h2>
              <div className="space-y-4">
                {reviews.map((review) => (
                  <div key={review.id} className="border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center">
                        <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center mr-3">
                          <span className="text-sm font-bold">{review.client.charAt(0)}</span>
                        </div>
                        <span className="font-medium">{review.client}</span>
                      </div>
                      <div className="flex items-center">
                        {[...Array(5)].map((_, i) => (
                          <Star 
                            key={i} 
                            size={16} 
                            className={i < review.rating ? 'text-yellow-400' : 'text-gray-300'} 
                            fill="currentColor" 
                          />
                        ))}
                      </div>
                    </div>
                    <p className="text-gray-700 mb-2">{review.comment}</p>
                    <p className="text-sm text-gray-500">{review.date}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Earnings Summary */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4">
                <Award size={20} className="inline mr-2 text-green-500" />
                Earnings Summary
              </h3>
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">This Month</span>
                  <span className="font-bold text-green-600">KSh {earnings.thisMonth.toLocaleString()}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Last Month</span>
                  <span className="font-bold text-gray-900">KSh {earnings.lastMonth.toLocaleString()}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Total Earnings</span>
                  <span className="font-bold text-gray-900">KSh {earnings.totalEarnings.toLocaleString()}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Completed Jobs</span>
                  <span className="font-bold text-gray-900">{earnings.completedJobs}</span>
                </div>
              </div>
            </div>

            {/* Availability */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4">Weekly Availability</h3>
              <div className="space-y-2">
                {Object.entries(formData.availability).map(([day, available]) => (
                  <div key={day} className="flex items-center justify-between">
                    <span className="capitalize text-gray-700">{day}</span>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                      available ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                    }`}>
                      {available ? 'Available' : 'Unavailable'}
                    </span>
                  </div>
                ))}
              </div>
              <Button variant="secondary" className="w-full mt-4">
                Update Schedule
              </Button>
            </div>

            {/* Performance */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4">Performance Metrics</h3>
              <div className="space-y-4">
                <div className="text-center p-4 bg-green-50 rounded-lg">
                  <div className="text-2xl font-bold text-green-600">98%</div>
                  <div className="text-sm text-gray-600">Response Rate</div>
                </div>
                <div className="text-center p-4 bg-blue-50 rounded-lg">
                  <div className="text-2xl font-bold text-blue-600">4.8★</div>
                  <div className="text-sm text-gray-600">Average Rating</div>
                </div>
                <div className="text-center p-4 bg-purple-50 rounded-lg">
                  <div className="text-2xl font-bold text-purple-600">95%</div>
                  <div className="text-sm text-gray-600">Completion Rate</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}