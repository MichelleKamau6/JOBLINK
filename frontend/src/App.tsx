import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './hooks/useAuth';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Providers from './pages/Providers';
import ProviderProfile from './pages/ProviderProfile';
import Profile from './pages/Profile';
import Dashboard from './pages/Dashboard';
import Bookings from './pages/Bookings';
import About from './pages/About';
import Contact from './pages/Contact';
import Reviews from './pages/Reviews';
import Payment from './pages/Payment';
import ClientDashboard from './pages/ClientDashboard';
import ProviderDashboard from './pages/ProviderDashboard';
import HelpCenter from './pages/HelpCenter';
import PrivacyPolicy from './pages/PrivacyPolicy';
import Footer from './components/Footer';
import LiveChat from './components/LiveChat';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Navbar />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/providers" element={<Providers />} />
              <Route path="/providers/:id" element={<ProviderProfile />} />
              <Route 
                path="/profile" 
                element={
                  <ProtectedRoute>
                    <Profile />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/bookings" 
                element={
                  <ProtectedRoute>
                    <Bookings />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/dashboard" 
                element={
                  <ProtectedRoute requiredRole="admin">
                    <Dashboard />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/client-dashboard" 
                element={
                  <ProtectedRoute>
                    <ClientDashboard />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/provider-dashboard" 
                element={
                  <ProtectedRoute requiredRole="provider">
                    <ProviderDashboard />
                  </ProtectedRoute>
                } 
              />
              <Route path="/about" element={<About />} />
              <Route path="/reviews" element={<Reviews />} />
              <Route path="/help" element={<HelpCenter />} />
              <Route path="/privacy" element={<PrivacyPolicy />} />
              <Route path="/contact" element={<Contact />} />
              <Route 
                path="/payment" 
                element={
                  <ProtectedRoute>
                    <Payment />
                  </ProtectedRoute>
                } 
              />
            </Routes>
          </main>
          <Footer />
          <LiveChat />
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;