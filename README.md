# JobLink - Service Provider Platform

A comprehensive platform connecting clients with service providers, featuring booking management, payments, and reviews.

## Project Structure

```
JOBLINK/
├── frontend/          # React + Vite + Tailwind CSS
├── backend/           # Flask API + SQLAlchemy
├── docs/              # Design assets and documentation
└── .github/           # CI/CD workflows and templates
```

## Team & Roles

- **Erick** - Scrum Master & Frontend Developer
- **Michelle** - Frontend Developer & UI Designer  
- **Donaldson** - Backend Lead (Core APIs & Auth)
- **Abdiaziz** - Backend Developer (Integrations & QA)

## Quick Start

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
flask db upgrade
flask run
```

## Environment Setup

1. Copy `.env.example` to `.env` in both frontend and backend directories:
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```

2. Update environment variables with your configuration:
   - Get Cloudinary credentials from https://cloudinary.com
   - Get SendGrid API key from https://sendgrid.com
   - Get M-Pesa credentials from Safaricom Developer Portal

3. Set up integrations (Cloudinary, SendGrid, M-Pesa)

## Development Workflow

- Main branch: `main` (production)
- Development branch: `dev` 
- Feature branches: `feature/JIRA-XXX-description`
- All PRs require review before merge

## Documentation

- [API Documentation](http://localhost:5000/api/docs) (Swagger)
- [Design System](docs/design-system.md)
- [Figma Prototype](#) (Link to be added by Michelle)

## Tech Stack

**Frontend:**
- React 18 + TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios

**Backend:**
- Flask + SQLAlchemy
- JWT Authentication
- PostgreSQL/SQLite
- Swagger/OpenAPI

**Integrations:**
- Cloudinary (Image uploads)
- SendGrid (Email notifications)
- M-Pesa (Payments)

## Sprint Progress

- [x] Sprint 1: Setup & Coordination
- [ ] Sprint 2: Core Features
- [ ] Sprint 3: Finalize & Deploy