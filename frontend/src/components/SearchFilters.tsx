import { useState } from 'react';
import { Search, Filter, MapPin, DollarSign, Star } from 'lucide-react';
import Button from './Button';

interface SearchFiltersProps {
  onSearch: (filters: SearchFilters) => void;
  loading?: boolean;
}

export type SearchFilters = {
  search: string;
  category: string;
  location: string;
  min_rate: string;
  max_rate: string;
  min_rating: string;
  sort_by: string;
}

export default function SearchFilters({ onSearch, loading }: SearchFiltersProps) {
  const [filters, setFilters] = useState<SearchFilters>({
    search: '',
    category: '',
    location: '',
    min_rate: '',
    max_rate: '',
    min_rating: '',
    sort_by: 'name_asc'
  });

  const [showAdvanced, setShowAdvanced] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(filters);
  };

  const handleReset = () => {
    const resetFilters = {
      search: '',
      category: '',
      location: '',
      min_rate: '',
      max_rate: '',
      min_rating: '',
      sort_by: 'name_asc'
    };
    setFilters(resetFilters);
    onSearch(resetFilters);
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-6">
      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Main Search */}
        <div className="flex gap-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
            <input
              type="text"
              placeholder="Search services, providers..."
              value={filters.search}
              onChange={(e) => setFilters({ ...filters, search: e.target.value })}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <Button type="submit" disabled={loading} className="px-6">
            {loading ? 'Searching...' : 'Search'}
          </Button>
        </div>

        {/* Quick Filters */}
        <div className="flex flex-wrap gap-2">
          <select
            value={filters.category}
            onChange={(e) => setFilters({ ...filters, category: e.target.value })}
            className="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          >
            <option value="">All Categories</option>
            <option value="Cleaning">Cleaning</option>
            <option value="Plumbing">Plumbing</option>
            <option value="Electrical">Electrical</option>
            <option value="Gardening">Gardening</option>
            <option value="Beauty">Beauty</option>
            <option value="Tutoring">Tutoring</option>
            <option value="IT Support">IT Support</option>
            <option value="Handyman">Handyman</option>
          </select>

          <div className="relative">
            <MapPin className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={16} />
            <input
              type="text"
              placeholder="Location"
              value={filters.location}
              onChange={(e) => setFilters({ ...filters, location: e.target.value })}
              className="pl-9 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <select
            value={filters.sort_by}
            onChange={(e) => setFilters({ ...filters, sort_by: e.target.value })}
            className="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          >
            <option value="name_asc">Name A-Z</option>
            <option value="rate_asc">Price: Low to High</option>
            <option value="rate_desc">Price: High to Low</option>
            <option value="rating_desc">Highest Rated</option>
          </select>

          <button
            type="button"
            onClick={() => setShowAdvanced(!showAdvanced)}
            className="flex items-center px-3 py-2 text-blue-600 hover:text-blue-700"
          >
            <Filter size={16} className="mr-1" />
            Advanced
          </button>
        </div>

        {/* Advanced Filters */}
        {showAdvanced && (
          <div className="grid md:grid-cols-3 gap-4 p-4 bg-gray-50 rounded-lg">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                <DollarSign size={16} className="inline mr-1" />
                Min Rate (KSh/hr)
              </label>
              <input
                type="number"
                placeholder="0"
                value={filters.min_rate}
                onChange={(e) => setFilters({ ...filters, min_rate: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                <DollarSign size={16} className="inline mr-1" />
                Max Rate (KSh/hr)
              </label>
              <input
                type="number"
                placeholder="10000"
                value={filters.max_rate}
                onChange={(e) => setFilters({ ...filters, max_rate: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                <Star size={16} className="inline mr-1" />
                Min Rating
              </label>
              <select
                value={filters.min_rating}
                onChange={(e) => setFilters({ ...filters, min_rating: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                <option value="">Any Rating</option>
                <option value="4">4+ Stars</option>
                <option value="3">3+ Stars</option>
                <option value="2">2+ Stars</option>
              </select>
            </div>
          </div>
        )}

        {/* Reset Button */}
        <div className="flex justify-end">
          <button
            type="button"
            onClick={handleReset}
            className="text-gray-600 hover:text-gray-800 text-sm"
          >
            Clear all filters
          </button>
        </div>
      </form>
    </div>
  );
}