import { render, screen, fireEvent } from '@testing-library/react';
import { vi } from 'vitest';
import ProviderCard from '../ProviderCard';

const mockProvider = {
  id: '1',
  name: 'Test Provider',
  service_category: 'Cleaning',
  location: 'Test City',
  hourly_rate: 25,
  rating: 4.5,
  description: 'Test description'
};

describe('ProviderCard', () => {
  it('renders provider information', () => {
    const mockOnBook = vi.fn();
    
    render(<ProviderCard provider={mockProvider} onBook={mockOnBook} />);
    
    expect(screen.getByText('Test Provider')).toBeInTheDocument();
    expect(screen.getByText('Cleaning')).toBeInTheDocument();
    expect(screen.getByText('Test City')).toBeInTheDocument();
    expect(screen.getByText('$25/hr')).toBeInTheDocument();
  });

  it('calls onBook when Book Now button is clicked', () => {
    const mockOnBook = vi.fn();
    
    render(<ProviderCard provider={mockProvider} onBook={mockOnBook} />);
    
    fireEvent.click(screen.getByText('Book Now'));
    expect(mockOnBook).toHaveBeenCalledWith('1');
  });
});