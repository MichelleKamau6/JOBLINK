import { Link } from 'react-router-dom';
import { CheckCircle, Users, Clock, Shield, Star, ArrowRight } from 'lucide-react';
import Hero from '../components/Hero';
import ServiceCategories from '../components/ServiceCategories';
import Button from '../components/Button';

export default function Home() {
  return (
    <div>
      <Hero />
      <ServiceCategories />
      
      {/* Features Section */}
      <div className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Why Choose JobLink?</h2>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center p-6">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">🛡️</span>
              </div>
              <h3 className="text-xl font-semibold mb-2">Verified Providers</h3>
              <p className="text-gray-600">All service providers are background-checked and verified</p>
            </div>
            <div className="text-center p-6">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">💳</span>
              </div>
              <h3 className="text-xl font-semibold mb-2">Secure Payments</h3>
              <p className="text-gray-600">Safe and secure M-Pesa payment processing</p>
            </div>
            <div className="text-center p-6">
              <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">⭐</span>
              </div>
              <h3 className="text-xl font-semibold mb-2">Quality Guaranteed</h3>
              <p className="text-gray-600">Read reviews and ratings from real customers</p>
            </div>
          </div>
        </div>
      </div>

      {/* How It Works Section */}
      <div className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">How JobLink Works</h2>
            <p className="text-xl text-gray-600">Get connected with trusted service providers in 3 simple steps</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-20 h-20 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-6">
                <span className="text-white text-2xl font-bold">1</span>
              </div>
              <h3 className="text-xl font-semibold mb-4">Search & Browse</h3>
              <p className="text-gray-600">Browse through our verified service providers and read reviews from other customers</p>
            </div>
            <div className="text-center">
              <div className="w-20 h-20 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-6">
                <span className="text-white text-2xl font-bold">2</span>
              </div>
              <h3 className="text-xl font-semibold mb-4">Book & Schedule</h3>
              <p className="text-gray-600">Select your preferred provider, choose a convenient time, and book your service</p>
            </div>
            <div className="text-center">
              <div className="w-20 h-20 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-6">
                <span className="text-white text-2xl font-bold">3</span>
              </div>
              <h3 className="text-xl font-semibold mb-4">Pay & Review</h3>
              <p className="text-gray-600">Pay securely through M-Pesa and leave a review to help other customers</p>
            </div>
          </div>
        </div>
      </div>

      {/* Statistics Section */}
      <div className="py-16 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4">Trusted by Thousands</h2>
            <p className="text-xl text-blue-100">Join our growing community of satisfied customers and providers</p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-5xl font-bold mb-2">500+</div>
              <div className="text-blue-100">Verified Providers</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">2,000+</div>
              <div className="text-blue-100">Happy Customers</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">5,000+</div>
              <div className="text-blue-100">Services Completed</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">4.8★</div>
              <div className="text-blue-100">Average Rating</div>
            </div>
          </div>
        </div>
      </div>

      {/* Testimonials Section */}
      <div className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">What Our Customers Say</h2>
            <p className="text-xl text-gray-600">Real reviews from real customers</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-gray-50 rounded-xl p-6">
              <div className="flex items-center mb-4">
                <div className="flex text-yellow-400">
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                </div>
              </div>
              <p className="text-gray-700 mb-4">"Amazing service! The plumber arrived on time and fixed my kitchen sink perfectly. Highly recommend JobLink!"</p>
              <div className="flex items-center">
                <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center mr-3">
                  <span className="text-white font-bold">M</span>
                </div>
                <div>
                  <div className="font-semibold">Mary Wanjiku</div>
                  <div className="text-sm text-gray-600">Nairobi</div>
                </div>
              </div>
            </div>
            <div className="bg-gray-50 rounded-xl p-6">
              <div className="flex items-center mb-4">
                <div className="flex text-yellow-400">
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                </div>
              </div>
              <p className="text-gray-700 mb-4">"Professional electrician, fair pricing, and excellent work quality. JobLink made it so easy to find reliable help."</p>
              <div className="flex items-center">
                <div className="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center mr-3">
                  <span className="text-white font-bold">J</span>
                </div>
                <div>
                  <div className="font-semibold">John Kamau</div>
                  <div className="text-sm text-gray-600">Kiambu</div>
                </div>
              </div>
            </div>
            <div className="bg-gray-50 rounded-xl p-6">
              <div className="flex items-center mb-4">
                <div className="flex text-yellow-400">
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                  <Star size={20} fill="currentColor" />
                </div>
              </div>
              <p className="text-gray-700 mb-4">"Great platform! I've used it multiple times for different services. Always reliable and professional providers."</p>
              <div className="flex items-center">
                <div className="w-10 h-10 bg-purple-500 rounded-full flex items-center justify-center mr-3">
                  <span className="text-white font-bold">A</span>
                </div>
                <div>
                  <div className="font-semibold">Anne Muthoni</div>
                  <div className="text-sm text-gray-600">Mombasa</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* For Providers Section */}
      <div className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl font-bold text-gray-900 mb-6">Grow Your Business with JobLink</h2>
              <p className="text-xl text-gray-600 mb-6">
                Join thousands of service providers who are growing their businesses through our platform.
              </p>
              <div className="space-y-4 mb-8">
                <div className="flex items-center">
                  <CheckCircle className="text-green-500 mr-3" size={24} />
                  <span className="text-gray-700">Get more customers and bookings</span>
                </div>
                <div className="flex items-center">
                  <CheckCircle className="text-green-500 mr-3" size={24} />
                  <span className="text-gray-700">Manage your schedule and payments</span>
                </div>
                <div className="flex items-center">
                  <CheckCircle className="text-green-500 mr-3" size={24} />
                  <span className="text-gray-700">Build your reputation with reviews</span>
                </div>
                <div className="flex items-center">
                  <CheckCircle className="text-green-500 mr-3" size={24} />
                  <span className="text-gray-700">No upfront costs or hidden fees</span>
                </div>
              </div>
              <Link to="/register">
                <Button className="inline-flex items-center">
                  Join as Provider
                  <ArrowRight size={16} className="ml-2" />
                </Button>
              </Link>
            </div>
            <div className="bg-gradient-to-br from-blue-100 to-purple-100 rounded-2xl p-8">
              <div className="grid grid-cols-2 gap-6 text-center">
                <div>
                  <Users className="text-blue-600 mx-auto mb-2" size={32} />
                  <div className="text-2xl font-bold text-gray-900">500+</div>
                  <div className="text-sm text-gray-600">Active Providers</div>
                </div>
                <div>
                  <Clock className="text-green-600 mx-auto mb-2" size={32} />
                  <div className="text-2xl font-bold text-gray-900">24/7</div>
                  <div className="text-sm text-gray-600">Support</div>
                </div>
                <div>
                  <Shield className="text-purple-600 mx-auto mb-2" size={32} />
                  <div className="text-2xl font-bold text-gray-900">100%</div>
                  <div className="text-sm text-gray-600">Secure</div>
                </div>
                <div>
                  <Star className="text-yellow-600 mx-auto mb-2" size={32} />
                  <div className="text-2xl font-bold text-gray-900">4.8★</div>
                  <div className="text-sm text-gray-600">Rating</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Call to Action Section */}
      <div className="py-16 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-4xl font-bold mb-4">Ready to Get Started?</h2>
          <p className="text-xl text-blue-100 mb-8">
            Whether you need a service or want to provide one, JobLink is here to help you connect.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/providers">
              <Button className="bg-white text-blue-600 hover:bg-gray-100 px-8 py-3">
                Find Services
              </Button>
            </Link>
            <Link to="/register">
              <Button className="border-2 border-white text-white hover:bg-white hover:text-blue-600 px-8 py-3">
                Become a Provider
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}