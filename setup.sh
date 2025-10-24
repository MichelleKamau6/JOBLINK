#!/bin/bash

echo "🚀 Setting up JobLink Development Environment"

# Frontend setup
echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

# Backend setup
echo "🐍 Setting up Python virtual environment..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "🗄️ Initializing database..."
python init_db.py

echo "✅ Setup complete!"
echo ""
echo "To start development:"
echo "Frontend: cd frontend && npm run dev"
echo "Backend: cd backend && source venv/bin/activate && python app.py"
echo ""
echo "Access points:"
echo "Frontend: http://localhost:5173"
echo "Backend API: http://localhost:5000"
echo "API Docs: http://localhost:5000/api/docs"