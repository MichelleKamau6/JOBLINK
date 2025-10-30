from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flasgger import Swagger
from extensions import db
from routes import auth, providers, bookings, admin, payments, upload, reviews, analytics, notifications
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///joblink.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    CORS(app, origins=['*'], allow_headers=['Content-Type', 'Authorization'], methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
    
    # Swagger configuration
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/api/docs/"
    }
    swagger = Swagger(app, config=swagger_config)
    
    # Root route
    @app.route('/')
    def home():
        return {
            'message': 'JobLink API is running!',
            'version': '1.0.0',
            'endpoints': {
                'providers': '/api/providers',
                'auth': '/api/auth',
                'docs': '/api/docs',
                'create-admin': '/create-admin'
            }
        }
    

    
    # Register blueprints
    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    app.register_blueprint(providers.bp, url_prefix='/api/providers')
    app.register_blueprint(bookings.bp, url_prefix='/api/bookings')
    app.register_blueprint(admin.bp, url_prefix='/api/admin')
    app.register_blueprint(payments.bp, url_prefix='/api/payments')
    app.register_blueprint(upload.bp, url_prefix='/api/upload')
    app.register_blueprint(reviews.bp, url_prefix='/api/reviews')
    app.register_blueprint(analytics.bp, url_prefix='/api/analytics')
    app.register_blueprint(notifications.bp, url_prefix='/api/notifications')
    
    # Create admin user route
    @app.route('/create-admin')
    def create_admin():
        from models import User, Role
        try:
            admin_role = Role.query.filter_by(name='admin').first()
            if not admin_role:
                return {'error': 'Admin role not found'}, 400
                
            existing_admin = User.query.filter_by(email='admin@joblink.com').first()
            if existing_admin:
                return {'message': 'Admin user already exists'}
                
            admin_user = User(
                email='admin@joblink.com',
                name='Admin User',
                role_id=admin_role.id,
                is_verified=True
            )
            admin_user.set_password('admin123')
            db.session.add(admin_user)
            db.session.commit()
            
            return {'message': 'Admin user created successfully', 'email': 'admin@joblink.com', 'password': 'admin123'}
        except Exception as e:
            return {'error': str(e)}, 500
    
    return app