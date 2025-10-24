# JobLink Backend API

Flask-based REST API for the JobLink service provider platform.

## Features

- JWT Authentication with role-based access control
- RESTful API endpoints with Swagger documentation
- M-Pesa payment integration
- Email notifications via SendGrid
- Image upload via Cloudinary
- Geo-location based provider search
- Admin dashboard with analytics

## Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment variables:**
   Copy `.env.example` to `.env` and update values:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///joblink.db
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   SENDGRID_API_KEY=your-sendgrid-key
   MPESA_CONSUMER_KEY=your-mpesa-key
   ```

4. **Initialize database:**
   ```bash
   python init_db.py
   ```

5. **Run application:**
   ```bash
   python app.py
   ```

## API Documentation

- **Swagger UI:** http://localhost:5000/api/docs
- **Base URL:** http://localhost:5000/api

### Authentication Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Provider Endpoints
- `GET /api/providers` - List providers with filters
- `GET /api/providers/{id}` - Get provider details
- `POST /api/providers` - Create provider profile

### Booking Endpoints
- `POST /api/bookings` - Create booking
- `GET /api/bookings` - Get user bookings
- `PUT /api/bookings/{id}/status` - Update booking status

### Payment Endpoints
- `POST /api/payments/initiate` - Initiate M-Pesa payment
- `POST /api/payments/callback` - M-Pesa callback handler
- `GET /api/payments/status/{id}` - Get payment status

### Admin Endpoints
- `GET /api/admin/stats` - Dashboard statistics
- `GET /api/admin/users` - List all users
- `DELETE /api/admin/users/{id}` - Delete user

## Testing

```bash
pytest
```

## Deployment

The application is configured for deployment on Render with PostgreSQL database.

## Models

- **User** - Authentication and user profiles
- **Role** - User roles (client, provider, admin)
- **ProviderProfile** - Service provider details
- **ServiceCategory** - Service categories
- **Booking** - Service bookings
- **Payment** - Payment records
- **Review** - Provider reviews