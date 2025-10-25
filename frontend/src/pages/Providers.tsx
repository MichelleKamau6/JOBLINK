import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { providerService } from '../services/authService';
import ProviderCard from '../components/ProviderCard';
import BookingModal from '../components/BookingModal';
import SearchFilters, { type SearchFilters as FilterType } from '../components/SearchFilters';
import { AlertCircle } from 'lucide-react';

interface Provider {
  id: number;
  name: string;
  service_category: string;
  rating: number;
  review_count: number;
  image_url?: string;
  location: string;
  hourly_rate: number;
  description: string;
}

interface SearchResult {
  providers: Provider[];
  total: number;
  page: number;
  pages: number;
}

export default function Providers() {
  const [searchResult, setSearchResult] = useState<SearchResult>({ providers: [], total: 0, page: 1, pages: 1 });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedProvider, setSelectedProvider] = useState<Provider | null>(null);
  const [showBookingModal, setShowBookingModal] = useState(false);
  const navigate = useNavigate();



  const searchProviders = async (filters: FilterType) => {
    console.log('Searching providers with filters:', filters);
    setLoading(true);
    setError('');
    try {
      const result = await providerService.searchProviders({
        search: filters.search || undefined,
        category: filters.category || undefined,
        location: filters.location || undefined,
        min_rate: filters.min_rate ? Number(filters.min_rate) : undefined,
        max_rate: filters.max_rate ? Number(filters.max_rate) : undefined,
        min_rating: filters.min_rating ? Number(filters.min_rating) : undefined,
        sort_by: filters.sort_by || 'name_asc'
      });
      console.log('Search result:', result);
      setSearchResult(result);
    } catch (err) {
      console.error('Search error:', err);
      setError('Failed to search providers. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    searchProviders({
      search: '',
      category: '',
      location: '',
      min_rate: '',
      max_rate: '',
      min_rating: '',
      sort_by: 'name_asc'
    });
  }, []);

  const handleBook = (providerId: string) => {
    const provider = searchResult.providers.find(p => p.id === Number(providerId));
    if (provider) {
      setSelectedProvider(provider);
      setShowBookingModal(true);
    }
  };

  const handleBookingSubmit = async (_bookingData: any) => {
    try {
      // await api.post('/bookings', bookingData);
      setShowBookingModal(false);
      alert('Booking submitted successfully!');
      navigate('/bookings');
    } catch (error) {
      console.error('Booking failed:', error);
      alert('Booking failed. Please try again.');
    }
  };

  if (loading) {
    return <div className="flex justify-center items-center h-64">Loading providers...</div>;
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Service Providers</h1>
        <div className="text-sm text-gray-600">
          {searchResult.total} provider{searchResult.total !== 1 ? 's' : ''} found
        </div>
      </div>
      
      <SearchFilters onSearch={searchProviders} loading={loading} />
      
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6 flex items-center">
          <AlertCircle className="text-red-500 mr-2" size={20} />
          <span className="text-red-700">{error}</span>
        </div>
      )}
      
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="bg-gray-200 animate-pulse rounded-lg h-64"></div>
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {searchResult.providers.map((provider) => (
            <ProviderCard
              key={provider.id}
              provider={provider}
              onBook={handleBook}
            />
          ))}
        </div>
      )}
      
      {!loading && searchResult.providers.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500 text-lg mb-4">No providers found matching your criteria.</p>
          <p className="text-gray-400">Try adjusting your search filters or browse all categories.</p>
        </div>
      )}

      <BookingModal
        isOpen={showBookingModal}
        onClose={() => setShowBookingModal(false)}
        provider={selectedProvider ? {
          id: selectedProvider.id.toString(),
          name: selectedProvider.name,
          hourly_rate: selectedProvider.hourly_rate
        } : null}
        onSubmit={handleBookingSubmit}
      />
    </div>
  );
}