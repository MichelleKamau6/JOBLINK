export interface SearchFilters {
  keyword: string;
  location: string;
  category: string;
  priceRange: [number, number];
  rating: number;
  availability: string;
  verified: boolean;
  distance: number;
}

export interface BookingData {
  provider_id: string;
  service_date: string;
  duration_hours: number;
  notes: string;
}

export interface RegisterData {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
  role: string;
}

export interface User {
  id: string;
  email: string;
  role: string;
  name: string;
}

export interface Provider {
  id: string;
  name: string;
  latitude: number;
  longitude: number;
  location: string;
}

export interface ProviderSearchFilters {
  search?: string;
  category?: string;
  location?: string;
  min_rate?: number;
  max_rate?: number;
  min_rating?: number;
  sort_by?: string;
  page?: number;
}
