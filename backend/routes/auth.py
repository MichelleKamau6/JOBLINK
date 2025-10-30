from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db
from models import User, Role

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    """User Registration
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: user
        schema:
          type: object
          required:
            - email
            - password
            - name
          properties:
            email:
              type: string
            password:
              type: string
            name:
              type: string
            role:
              type: string
              default: client
    responses:
      201:
        description: User created successfully
      400:
        description: Validation error
    """
    data = request.get_json()
    
    # Validate required fields
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    required_fields = ['email', 'password', 'name']
    missing_fields = [field for field in required_fields if field not in data or not data[field]]
    
    if missing_fields:
        return jsonify({'message': f'Missing required fields: {", ".join(missing_fields)}'}), 400
    
    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    # Get or default to client role
    role = Role.query.filter_by(name=data.get('role', 'client')).first()
    if not role:
        role = Role.query.filter_by(name='client').first()
    
    if not role:
        return jsonify({'message': 'Role not found. Please initialize the database.'}), 500
    
    # Create user
    user = User(
        email=data['email'],
        name=data['name'],
        role_id=role.id
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    """User Login
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: credentials
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({
            'token': access_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role
            }
        })
    
    return jsonify({'message': 'Invalid credentials'}), 401

@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get Current User
    ---
    tags:
      - Authentication
    security:
      - Bearer: []
    responses:
      200:
        description: Current user information
    """
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    
    return jsonify({
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'role': user.role
    })