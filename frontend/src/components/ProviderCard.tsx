import Rating from './Rating';
import Button from './Button';
import VerificationBadges from './VerificationBadges';

interface Provider {
  id: number;
  name: string;
  service_category: string;
  location: string;
  hourly_rate: number;
  rating: number;
  review_count?: number;
  image_url?: string;
  description: string;
}

interface ProviderCardProps {
  provider: Provider;
  onBook: (providerId: string) => void;
}

export default function ProviderCard({ provider, onBook }: ProviderCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      {provider.image_url && (
        <img 
          src={provider.image_url} 
          alt={provider.name}
          className="w-full h-48 object-cover"
        />
      )}
      <div className="p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-2">{provider.name}</h3>
        <p className="text-primary-600 font-medium mb-1">{provider.service_category}</p>
        <p className="text-gray-600 mb-2">{provider.location}</p>
        <p className="text-gray-700 text-sm mb-3 line-clamp-2">{provider.description}</p>
        
        <VerificationBadges 
          verifications={{
            idVerified: true,
            backgroundCheck: Math.random() > 0.3,
            insurance: Math.random() > 0.5,
            license: Math.random() > 0.6
          }}
          size="sm"
        />
        
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center">
            <Rating rating={provider.rating} />
            {provider.review_count !== undefined && (
              <span className="text-sm text-gray-500 ml-2">({provider.review_count})</span>
            )}
          </div>
          <span className="text-lg font-bold text-gray-900">
            KSh {provider.hourly_rate}/hr
          </span>
        </div>
        
        <Button 
          onClick={() => onBook(provider.id.toString())}
          className="w-full"
        >
          Book Now
        </Button>
      </div>
    </div>
  );
}