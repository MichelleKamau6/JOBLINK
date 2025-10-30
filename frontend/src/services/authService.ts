import axios from 'axios';
import type { RegisterData } from '../types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authService = {
  async login(email: string, password: string) {
    const response = await api.post('/auth/login', { email, password });
    return response.data;
  },

  async getCurrentUser() {
    const response = await api.get('/auth/me');
    return response.data;
  },

  async register(userData: RegisterData) {
    const response = await api.post('/auth/register', userData);
    return response.data;
  }
};

export const providerService = {
  async searchProviders(filters: {
    search?: string;
    category?: string;
    location?: string;
    min_rate?: number;
    max_rate?: number;
    min_rating?: number;
    sort_by?: string;
    page?: number;
  }) {
    const params = new URLSearchParams();
    Object.entries(filters).forEach(([key, value]) => {
      if (value !== undefined && value !== '') {
        params.append(key, value.toString());
      }
    });
    
    const response = await api.get(`/providers?${params}`);
    return response.data;
  },

  async getProvider(id: number) {
    const response = await api.get(`/providers/${id}`);
    return response.data;
  }
};

export default api;