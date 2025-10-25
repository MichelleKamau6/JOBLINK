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
    CORS(app)
    
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
                'seed': '/seed-data'
            }
        }
    
    # Seed data route
    @app.route('/seed-data')
    def seed_data():
        from models import User, Role, ServiceCategory, ProviderProfile
        
        try:
            provider_role = Role.query.filter_by(name='provider').first()
            
            providers_data = [
                {
                    'name': 'John Mwangi',
                    'email': 'john.cleaning@example.com',
                    'business_name': 'John\'s Premium Cleaning',
                    'category': 'Cleaning',
                    'location': 'Nairobi',
                    'rate': 2000,
                    'description': 'Professional house and office cleaning services'
                },
                {
                    'name': 'Sarah Wanjiku',
                    'email': 'sarah.plumbing@example.com',
                    'business_name': 'Sarah\'s Expert Plumbing',
                    'category': 'Plumbing',
                    'location': 'Kiambu',
                    'rate': 3500,
                    'description': 'Licensed plumber with 10+ years experience'
                },
                {
                    'name': 'David Kimani',
                    'email': 'david.electric@example.com',
                    'business_name': 'David\'s Electrical Solutions',
                    'category': 'Electrical',
                    'location': 'Nairobi',
                    'rate': 4000,
                    'description': 'Certified electrician specializing in home wiring'
                }
            ]
            
            for data in providers_data:
                if User.query.filter_by(email=data['email']).first():
                    continue
                    
                user = User(
                    email=data['email'],
                    name=data['name'],
                    role_id=provider_role.id,
                    is_verified=True
                )
                user.set_password('provider123')
                db.session.add(user)
                db.session.flush()
                
                category = ServiceCategory.query.filter_by(name=data['category']).first()
                
                provider = ProviderProfile(
                    user_id=user.id,
                    service_category_id=category.id,
                    business_name=data['business_name'],
                    description=data['description'],
                    location=data['location'],
                    hourly_rate=data['rate'],
                    is_active=True
                )
                db.session.add(provider)
            
            db.session.commit()
            return {'message': 'Sample data seeded successfully!', 'providers_added': len(providers_data)}
        except Exception as e:
            return {'error': str(e)}, 500
    
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
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Initialize database on first run
    try:
        with app.app_context():
            from models import Role, ServiceCategory, User
            db.create_all()
            
            # Create roles if they don't exist
            for role_name in ['client', 'provider', 'admin']:
                if not Role.query.filter_by(name=role_name).first():
                    role = Role(name=role_name)
                    db.session.add(role)
            
            # Create service categories if they don't exist
            categories = [
                {'name': 'Cleaning', 'description': 'Home and office cleaning services'},
                {'name': 'Plumbing', 'description': 'Plumbing repairs and installations'},
                {'name': 'Electrical', 'description': 'Electrical repairs and installations'},
                {'name': 'Gardening', 'description': 'Garden maintenance and landscaping'},
                {'name': 'Handyman', 'description': 'General home repairs and maintenance'},
                {'name': 'Beauty', 'description': 'Beauty and wellness services'},
                {'name': 'Tutoring', 'description': 'Educational and tutoring services'},
                {'name': 'IT Support', 'description': 'Computer and technology support'}
            ]
            
            for cat_data in categories:
                if not ServiceCategory.query.filter_by(name=cat_data['name']).first():
                    category = ServiceCategory(**cat_data)
                    db.session.add(category)
            
            db.session.commit()
            
            # Add sample providers
            provider_role = Role.query.filter_by(name='provider').first()
            
            providers_data = [
                {
                    'name': 'John Mwangi',
                    'email': 'john.cleaning@example.com',
                    'business_name': 'John\'s Premium Cleaning',
                    'category': 'Cleaning',
                    'location': 'Nairobi',
                    'rate': 2000,
                    'description': 'Professional house and office cleaning services'
                },
                {
                    'name': 'Sarah Wanjiku',
                    'email': 'sarah.plumbing@example.com',
                    'business_name': 'Sarah\'s Expert Plumbing',
                    'category': 'Plumbing',
                    'location': 'Kiambu',
                    'rate': 3500,
                    'description': 'Licensed plumber with 10+ years experience'
                },
                {
                    'name': 'David Kimani',
                    'email': 'david.electric@example.com',
                    'business_name': 'David\'s Electrical Solutions',
                    'category': 'Electrical',
                    'location': 'Nairobi',
                    'rate': 4000,
                    'description': 'Certified electrician specializing in home wiring'
                }
            ]
            
            for data in providers_data:
                if not User.query.filter_by(email=data['email']).first():
                    user = User(
                        email=data['email'],
                        name=data['name'],
                        role_id=provider_role.id,
                        is_verified=True
                    )
                    user.set_password('provider123')
                    db.session.add(user)
                    db.session.flush()
                    
                    category = ServiceCategory.query.filter_by(name=data['category']).first()
                    
                    provider = ProviderProfile(
                        user_id=user.id,
                        service_category_id=category.id,
                        business_name=data['business_name'],
                        description=data['description'],
                        location=data['location'],
                        hourly_rate=data['rate'],
                        is_active=True
                    )
                    db.session.add(provider)
            
            db.session.commit()
            print("Database initialized successfully with sample data")
    except Exception as e:
        print(f"Database initialization error: {e}")
    
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)