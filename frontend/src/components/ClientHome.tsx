import { Link } from 'react-router-dom';
import { Search, Star } from 'lucide-react';
import Button from './Button';
import ServiceCategories from './ServiceCategories';

export default function ClientHome() {
  return (
    <div>
      {/* Client Hero Section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-5xl font-bold mb-6">Find Trusted Service Providers</h1>
            <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
              Book verified professionals for home services, repairs, and more. Quality guaranteed.
            </p>
            <Link to="/providers">
              <Button className="bg-white text-blue-600 hover:bg-gray-100 px-8 py-4 text-lg">
                <Search size={20} className="mr-2" />
                Browse Services
              </Button>
            </Link>
          </div>
        </div>
      </div>

      <ServiceCategories />

      {/* Quick Actions */}
      <div className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">What do you need help with?</h2>
          <div className="grid md:grid-cols-3 gap-8">
            <Link to="/providers?category=cleaning" className="group">
              <div className="bg-blue-50 group-hover:bg-blue-100 rounded-xl p-6 text-center transition-colors">
                <div className="text-4xl mb-4">🧹</div>
                <h3 className="text-xl font-semibold mb-2">House Cleaning</h3>
                <p className="text-gray-600">Professional cleaning services</p>
              </div>
            </Link>
            <Link to="/providers?category=plumbing" className="group">
              <div className="bg-green-50 group-hover:bg-green-100 rounded-xl p-6 text-center transition-colors">
                <div className="text-4xl mb-4">🔧</div>
                <h3 className="text-xl font-semibold mb-2">Plumbing</h3>
                <p className="text-gray-600">Repairs and installations</p>
              </div>
            </Link>
            <Link to="/providers?category=electrical" className="group">
              <div className="bg-yellow-50 group-hover:bg-yellow-100 rounded-xl p-6 text-center transition-colors">
                <div className="text-4xl mb-4">⚡</div>
                <h3 className="text-xl font-semibold mb-2">Electrical</h3>
                <p className="text-gray-600">Electrical work and repairs</p>
              </div>
            </Link>
          </div>
        </div>
      </div>

      {/* Emergency Services */}
      <div className="py-16 bg-red-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold text-red-800">🚨 Emergency Services</h2>
            <p className="text-red-600">Need urgent help? Get connected instantly</p>
          </div>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="bg-white rounded-xl p-6 border-l-4 border-red-500">
              <h3 className="font-semibold text-lg mb-2">🔧 Emergency Plumbing</h3>
              <p className="text-gray-600 mb-4">Burst pipes, leaks, blockages</p>
              <Button className="bg-red-600 hover:bg-red-700 w-full">Call Now</Button>
            </div>
            <div className="bg-white rounded-xl p-6 border-l-4 border-yellow-500">
              <h3 className="font-semibold text-lg mb-2">⚡ Emergency Electrical</h3>
              <p className="text-gray-600 mb-4">Power outages, faulty wiring</p>
              <Button className="bg-yellow-600 hover:bg-yellow-700 w-full">Call Now</Button>
            </div>
            <div className="bg-white rounded-xl p-6 border-l-4 border-blue-500">
              <h3 className="font-semibold text-lg mb-2">🔒 Locksmith</h3>
              <p className="text-gray-600 mb-4">Locked out, broken locks</p>
              <Button className="bg-blue-600 hover:bg-blue-700 w-full">Call Now</Button>
            </div>
          </div>
        </div>
      </div>

      {/* Recommended Providers */}
      <div className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-8">
            <h2 className="text-3xl font-bold">⭐ Top Rated Near You</h2>
            <Link to="/providers" className="text-blue-600 hover:text-blue-700">View All</Link>
          </div>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="bg-gray-50 rounded-xl p-6">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center mr-3">
                  <span className="text-white font-bold">JM</span>
                </div>
                <div>
                  <h3 className="font-semibold">John's Cleaning</h3>
                  <div className="flex items-center">
                    <Star size={16} className="text-yellow-400 fill-current" />
                    <span className="text-sm text-gray-600 ml-1">4.9 (127 reviews)</span>
                  </div>
                </div>
              </div>
              <p className="text-gray-600 mb-4">Professional house cleaning • KSh 2,000/hr</p>
              <Button className="w-full">Book Now</Button>
            </div>
            <div className="bg-gray-50 rounded-xl p-6">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-green-500 rounded-full flex items-center justify-center mr-3">
                  <span className="text-white font-bold">SM</span>
                </div>
                <div>
                  <h3 className="font-semibold">Sarah's Plumbing</h3>
                  <div className="flex items-center">
                    <Star size={16} className="text-yellow-400 fill-current" />
                    <span className="text-sm text-gray-600 ml-1">4.8 (89 reviews)</span>
                  </div>
                </div>
              </div>
              <p className="text-gray-600 mb-4">Expert plumbing services • KSh 3,500/hr</p>
              <Button className="w-full">Book Now</Button>
            </div>
            <div className="bg-gray-50 rounded-xl p-6">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-purple-500 rounded-full flex items-center justify-center mr-3">
                  <span className="text-white font-bold">DK</span>
                </div>
                <div>
                  <h3 className="font-semibold">David's Electric</h3>
                  <div className="flex items-center">
                    <Star size={16} className="text-yellow-400 fill-current" />
                    <span className="text-sm text-gray-600 ml-1">4.7 (156 reviews)</span>
                  </div>
                </div>
              </div>
              <p className="text-gray-600 mb-4">Licensed electrician • KSh 4,000/hr</p>
              <Button className="w-full">Book Now</Button>
            </div>
          </div>
        </div>
      </div>

      {/* Special Offers */}
      <div className="py-16 bg-gradient-to-r from-purple-600 to-pink-600 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold mb-4">🎉 Special Offers</h2>
            <p className="text-purple-100">Limited time deals from top providers</p>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-white/10 backdrop-blur rounded-xl p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-semibold">First Booking Discount</h3>
                <span className="bg-yellow-400 text-purple-800 px-3 py-1 rounded-full text-sm font-bold">20% OFF</span>
              </div>
              <p className="text-purple-100 mb-4">Get 20% off your first service booking. Valid for new customers only.</p>
              <Button className="bg-white text-purple-600 hover:bg-gray-100">Claim Offer</Button>
            </div>
            <div className="bg-white/10 backdrop-blur rounded-xl p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-semibold">Weekend Special</h3>
                <span className="bg-green-400 text-purple-800 px-3 py-1 rounded-full text-sm font-bold">15% OFF</span>
              </div>
              <p className="text-purple-100 mb-4">Book weekend services and save 15%. Available Saturday & Sunday.</p>
              <Button className="bg-white text-purple-600 hover:bg-gray-100">Book Weekend</Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}