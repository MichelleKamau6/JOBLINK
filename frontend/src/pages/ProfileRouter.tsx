import { useAuth } from '../hooks/useAuthHook';
import ClientProfile from './ClientProfile';
import ProviderProfile from './ProviderProfile';

export default function ProfileRouter() {
  const { user } = useAuth();

  if (!user) {
    return <div>Loading...</div>;
  }

  // Route to appropriate profile based on user role
  if (user.role === 'provider') {
    return <ProviderProfile />;
  }

  // Default to client profile for customers and other roles
  return <ClientProfile />;
}