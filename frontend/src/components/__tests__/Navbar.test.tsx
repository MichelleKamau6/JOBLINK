import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { vi } from 'vitest';
import Navbar from '../Navbar';
import { useAuth } from '../../hooks/useAuth';

// Mock the useAuth hook
vi.mock('../../hooks/useAuth');

const mockUseAuth = vi.mocked(useAuth);

const renderNavbar = () => {
  return render(
    <BrowserRouter>
      <Navbar />
    </BrowserRouter>
  );
};

describe('Navbar', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders JobLink brand', () => {
    mockUseAuth.mockReturnValue({
      user: null,
      login: vi.fn(),
      logout: vi.fn(),
      loading: false
    });

    renderNavbar();
    expect(screen.getByText('JobLink')).toBeInTheDocument();
  });

  it('shows login button when user is not authenticated', () => {
    mockUseAuth.mockReturnValue({
      user: null,
      login: vi.fn(),
      logout: vi.fn(),
      loading: false
    });

    renderNavbar();
    expect(screen.getByText('Login')).toBeInTheDocument();
  });

  it('shows user menu when authenticated', () => {
    mockUseAuth.mockReturnValue({
      user: { id: '1', email: 'test@example.com', name: 'Test User', role: 'client' },
      login: vi.fn(),
      logout: vi.fn(),
      loading: false
    });

    renderNavbar();
    expect(screen.getByText('Profile')).toBeInTheDocument();
    expect(screen.getByText('Logout')).toBeInTheDocument();
  });

  it('shows dashboard link for admin users', () => {
    mockUseAuth.mockReturnValue({
      user: { id: '1', email: 'admin@example.com', name: 'Admin User', role: 'admin' },
      login: vi.fn(),
      logout: vi.fn(),
      loading: false
    });

    renderNavbar();
    expect(screen.getByText('Dashboard')).toBeInTheDocument();
  });
});