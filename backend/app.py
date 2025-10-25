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
            db.create_all()
            
            # Import models after app context is created
            from models import Role, ServiceCategory, User
            
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
            
            # Create admin user
            admin_role = Role.query.filter_by(name='admin').first()
            if admin_role and not User.query.filter_by(email='admin@joblink.com').first():
                admin_user = User(
                    email='admin@joblink.com',
                    name='Admin User',
                    role_id=admin_role.id,
                    is_verified=True
                )
                admin_user.set_password('admin123')
                db.session.add(admin_user)
            
            # Create sample client
            client_role = Role.query.filter_by(name='client').first()
            if client_role and not User.query.filter_by(email='client@example.com').first():
                client_user = User(
                    email='client@example.com',
                    name='John Doe',
                    role_id=client_role.id,
                    is_verified=True
                )
                client_user.set_password('client123')
                db.session.add(client_user)
            
            db.session.commit()
            print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")
    
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)