#!/bin/bash

echo "🚀 Deploying JobLink to Production"

# Frontend deployment to Vercel
echo "📦 Deploying Frontend to Vercel..."
cd frontend
npm run build
npx vercel --prod
cd ..

# Backend deployment to Render
echo "🐍 Preparing Backend for Render..."
cd backend

# Create Render build script
cat > build.sh << 'EOF'
#!/bin/bash
pip install -r requirements.txt
python init_db.py
EOF

chmod +x build.sh

# Create Render start script  
cat > start.sh << 'EOF'
#!/bin/bash
python app.py
EOF

chmod +x start.sh

echo "✅ Deployment scripts created!"
echo ""
echo "Next steps:"
echo "1. Push code to GitHub"
echo "2. Connect Render to your GitHub repository"
echo "3. Set environment variables in Render dashboard"
echo "4. Deploy backend service"
echo ""
echo "Environment variables needed:"
echo "- SECRET_KEY"
echo "- DATABASE_URL (PostgreSQL)"
echo "- CLOUDINARY_CLOUD_NAME"
echo "- CLOUDINARY_API_KEY" 
echo "- CLOUDINARY_API_SECRET"
echo "- SENDGRID_API_KEY"
echo "- MPESA_CONSUMER_KEY"
echo "- MPESA_CONSUMER_SECRET"
echo "- MPESA_SHORTCODE"
echo "- MPESA_PASSKEY"