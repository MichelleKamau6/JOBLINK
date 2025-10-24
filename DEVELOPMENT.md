# JobLink Development Guide

## Quick Start

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd JOBLINK
   ./setup.sh
   ```

2. **Start Development Servers**
   ```bash
   # Terminal 1 - Frontend
   cd frontend
   npm run dev
   
   # Terminal 2 - Backend
   cd backend
   source venv/bin/activate
   python app.py
   ```

## Sprint Tasks by Team Member

### 🙋 Erick - Scrum Master & Frontend Developer

**Sprint 1 - Setup & Coordination**
- [x] JIRA-ERK-001: Initialize Monorepo & Branch Strategy
- [x] JIRA-ERK-002: Configure CI/PR rules & Github-Jira integration
- [x] JIRA-ERK-003: Frontend scaffold & routing
- [ ] JIRA-ERK-004: Sprint planning & backlog grooming

**Sprint 2 - Core Frontend Features**
- [ ] JIRA-ERK-005: Auth flow integration (login/logout)
- [ ] JIRA-ERK-006: Provider List & Card Component
- [ ] JIRA-ERK-007: Booking UI skeleton & API calls
- [ ] JIRA-ERK-008: PR reviews & release to dev branch

### 🎨 Michelle - Frontend Developer / UI Designer

**Sprint 1 - Design System & Components**
- [ ] JIRA-MIC-001: Figma Style Guide + Components
- [ ] JIRA-MIC-002: Design core screens (desktop)
- [x] JIRA-MIC-003: Export assets & Tailwind tokens mapping

**Sprint 2 - Component Implementation**
- [x] JIRA-MIC-004: Build reusable UI components in React
- [ ] JIRA-MIC-005: Provider Profile page & reviews UI
- [ ] JIRA-MIC-006: Responsiveness & accessibility pass

### ⚙️ Donaldson - Backend Lead

**Sprint 1 - DB & Models**
- [x] JIRA-DON-001: Setup Flask project & DB connection
- [x] JIRA-DON-002: Create DB models & ERD
- [x] JIRA-DON-003: Swagger / OpenAPI scaffold

**Sprint 2 - Auth, Providers & Bookings**
- [x] JIRA-DON-004: JWT Auth & RBAC
- [x] JIRA-DON-005: Provider CRUD & search endpoints
- [x] JIRA-DON-006: Booking endpoints & validation
- [x] JIRA-DON-007: Rating aggregation endpoint

### 🧠 Abdiaziz - Backend Developer

**Sprint 1 - Integrations plan & stubs**
- [x] JIRA-ABD-001: Cloudinary integration (upload endpoint)
- [ ] JIRA-ABD-002: SendGrid stub & verification workflow

**Sprint 2 - Payments & Notifications**
- [x] JIRA-ABD-003: M-Pesa sandbox integration (STK Push)
- [ ] JIRA-ABD-004: Email notifications on booking events
- [ ] JIRA-ABD-005: Webhook security & retry logic

## Development Workflow

1. **Branch Strategy**
   - `main` - Production branch
   - `dev` - Development branch
   - `feature/JIRA-XXX-description` - Feature branches

2. **Pull Request Process**
   - Create feature branch from `dev`
   - Implement feature with tests
   - Create PR using provided template
   - Require at least one review
   - Merge to `dev` after approval

3. **Testing Requirements**
   - Frontend: React Testing Library + Vitest
   - Backend: pytest with Flask-Testing
   - All PRs must include tests

## API Documentation

- **Swagger UI**: http://localhost:5000/api/docs
- **Base URL**: http://localhost:5000/api

### Key Endpoints

**Authentication**
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

**Providers**
- `GET /api/providers` - List providers
- `GET /api/providers/{id}` - Get provider details
- `POST /api/providers` - Create provider profile

**Bookings**
- `POST /api/bookings` - Create booking
- `GET /api/bookings` - Get user bookings
- `PUT /api/bookings/{id}/status` - Update booking status

## Environment Variables

### Frontend (.env)
```
VITE_API_URL=http://localhost:5000/api
```

### Backend (.env)
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=dev-secret-key
DATABASE_URL=sqlite:///joblink.db
CLOUDINARY_CLOUD_NAME=your-cloud-name
SENDGRID_API_KEY=your-sendgrid-key
MPESA_CONSUMER_KEY=your-consumer-key
```

## Database Schema

### Core Models
- **User**: Authentication and user profiles
- **Role**: User roles (client, provider, admin)
- **ProviderProfile**: Service provider details
- **ServiceCategory**: Service categories
- **Booking**: Service bookings
- **Payment**: Payment records
- **Review**: Provider reviews

## Testing

### Frontend Tests
```bash
cd frontend
npm test
npm run test:ui  # Visual test runner
```

### Backend Tests
```bash
cd backend
source venv/bin/activate
pytest
```

## Deployment

### Frontend (Vercel)
- Connect GitHub repository
- Set build command: `npm run build`
- Set output directory: `dist`
- Add environment variables

### Backend (Render)
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `python app.py`
- Add environment variables

## Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure Flask-CORS is configured
   - Check API URL in frontend .env

2. **Database Issues**
   - Run `python init_db.py` to reset database
   - Check DATABASE_URL in backend .env

3. **Authentication Issues**
   - Verify JWT_SECRET_KEY matches
   - Check token storage in localStorage

### Getting Help

1. Check existing GitHub issues
2. Review API documentation
3. Ask team members in daily standup
4. Create detailed bug reports with steps to reproduce