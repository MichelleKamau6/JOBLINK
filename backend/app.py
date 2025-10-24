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
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    
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
    app.run(debug=True)