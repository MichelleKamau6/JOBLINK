import { useState } from 'react';
import { Search, Filter, MapPin, DollarSign, Star, Calendar } from 'lucide-react';
import Button from './Button';

interface AdvancedSearchProps {
  onSearch: (filters: any) => void;
}

export default function AdvancedSearch({ onSearch }: AdvancedSearchProps) {
  const [showFilters, setShowFilters] = useState(false);
  const [filters, setFilters] = useState({
    keyword: '',
    location: '',
    category: '',
    priceRange: [0, 10000],
    rating: 0,
    availability: '',
    verified: false,
    distance: 25
  });

  const categories = [
    'Cleaning', 'Plumbing', 'Electrical', 'Gardening', 'Beauty', 'IT Support',
    'Painting', 'Catering', 'Photography', 'Tutoring', 'Handyman', 'Carpentry'
  ];

  const handleSearch = () => {
    onSearch(filters);
  };

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mb-8">
      {/* Main Search Bar */}
      <div className="flex flex-col md:flex-row gap-4 mb-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
          <input
            type="text"
            placeholder="What service do you need?"
            value={filters.keyword}
            onChange={(e) => setFilters({...filters, keyword: e.target.value})}
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        
        <div className="relative">
          <MapPin className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
          <input
            type="text"
            placeholder="Location"
            value={filters.location}
            onChange={(e) => setFilters({...filters, location: e.target.value})}
            className="w-full md:w-48 pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        
        <Button onClick={() => setShowFilters(!showFilters)} variant="secondary">
          <Filter size={16} className="mr-2" />
          Filters
        </Button>
        
        <Button onClick={handleSearch}>
          Search
        </Button>
      </div>

      {/* Advanced Filters */}
      {showFilters && (
        <div className="border-t pt-4 space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Category */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Category</label>
              <select
                value={filters.category}
                onChange={(e) => setFilters({...filters, category: e.target.value})}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="">All Categories</option>
                {categories.map(cat => (
                  <option key={cat} value={cat}>{cat}</option>
                ))}
              </select>
            </div>

            {/* Price Range */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <DollarSign size={16} className="inline mr-1" />
                Price Range (KSh)
              </label>
              <div className="flex items-center space-x-2">
                <input
                  type="number"
                  placeholder="Min"
                  value={filters.priceRange[0]}
                  onChange={(e) => setFilters({...filters, priceRange: [parseInt(e.target.value) || 0, filters.priceRange[1]]})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
                <span>-</span>
                <input
                  type="number"
                  placeholder="Max"
                  value={filters.priceRange[1]}
                  onChange={(e) => setFilters({...filters, priceRange: [filters.priceRange[0], parseInt(e.target.value) || 10000]})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
            </div>

            {/* Rating */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <Star size={16} className="inline mr-1" />
                Minimum Rating
              </label>
              <select
                value={filters.rating}
                onChange={(e) => setFilters({...filters, rating: parseInt(e.target.value)})}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value={0}>Any Rating</option>
                <option value={4}>4+ Stars</option>
                <option value={4.5}>4.5+ Stars</option>
                <option value={5}>5 Stars Only</option>
              </select>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Availability */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <Calendar size={16} className="inline mr-1" />
                Availability
              </label>
              <select
                value={filters.availability}
                onChange={(e) => setFilters({...filters, availability: e.target.value})}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="">Any Time</option>
                <option value="today">Available Today</option>
                <option value="tomorrow">Available Tomorrow</option>
                <option value="week">This Week</option>
                <option value="weekend">Weekends</option>
              </select>
            </div>

            {/* Distance */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Distance (km)
              </label>
              <select
                value={filters.distance}
                onChange={(e) => setFilters({...filters, distance: parseInt(e.target.value)})}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value={5}>Within 5 km</option>
                <option value={10}>Within 10 km</option>
                <option value={25}>Within 25 km</option>
                <option value={50}>Within 50 km</option>
                <option value={100}>Any Distance</option>
              </select>
            </div>

            {/* Verified Only */}
            <div className="flex items-center pt-6">
              <input
                type="checkbox"
                id="verified"
                checked={filters.verified}
                onChange={(e) => setFilters({...filters, verified: e.target.checked})}
                className="mr-2"
              />
              <label htmlFor="verified" className="text-sm font-medium text-gray-700">
                Verified Providers Only
              </label>
            </div>
          </div>

          <div className="flex justify-end space-x-2 pt-4">
            <Button 
              variant="secondary" 
              onClick={() => setFilters({
                keyword: '', location: '', category: '', priceRange: [0, 10000],
                rating: 0, availability: '', verified: false, distance: 25
              })}
            >
              Clear All
            </Button>
            <Button onClick={handleSearch}>
              Apply Filters
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}