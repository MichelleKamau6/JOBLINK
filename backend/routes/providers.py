from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import ProviderProfile, ServiceCategory, User

bp = Blueprint('providers', __name__)

@bp.route('', methods=['GET'])
def get_providers():
    """Get All Providers
    ---
    tags:
      - Providers
    parameters:
      - in: query
        name: category
        type: string
        description: Filter by service category
      - in: query
        name: location
        type: string
        description: Filter by location
      - in: query
        name: page
        type: integer
        default: 1
      - in: query
        name: per_page
        type: integer
        default: 10
    responses:
      200:
        description: List of providers
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category')
    location = request.args.get('location')
    
    query = ProviderProfile.query.filter_by(is_active=True)
    
    if category:
        query = query.join(ServiceCategory).filter(ServiceCategory.name.ilike(f'%{category}%'))
    
    if location:
        query = query.filter(ProviderProfile.location.ilike(f'%{location}%'))
    
    providers = query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify([{
        'id': p.id,
        'name': p.business_name,
        'service_category': p.category.name,
        'location': p.location,
        'hourly_rate': p.hourly_rate,
        'rating': p.average_rating,
        'image_url': p.image_url,
        'description': p.description
    } for p in providers.items])

@bp.route('/<int:provider_id>', methods=['GET'])
def get_provider(provider_id):
    """Get Provider Details
    ---
    tags:
      - Providers
    parameters:
      - in: path
        name: provider_id
        type: integer
        required: true
    responses:
      200:
        description: Provider details
      404:
        description: Provider not found
    """
    provider = ProviderProfile.query.get_or_404(provider_id)
    
    return jsonify({
        'id': provider.id,
        'name': provider.business_name,
        'service_category': provider.category.name,
        'location': provider.location,
        'hourly_rate': provider.hourly_rate,
        'rating': provider.average_rating,
        'image_url': provider.image_url,
        'description': provider.description,
        'reviews': [{
            'rating': r.rating,
            'comment': r.comment,
            'client_name': r.client.name,
            'created_at': r.created_at.isoformat()
        } for r in provider.reviews]
    })

@bp.route('', methods=['POST'])
@jwt_required()
def create_provider():
    """Create Provider Profile
    ---
    tags:
      - Providers
    security:
      - Bearer: []
    parameters:
      - in: body
        name: provider
        schema:
          type: object
          required:
            - business_name
            - service_category_id
            - location
            - hourly_rate
          properties:
            business_name:
              type: string
            service_category_id:
              type: integer
            location:
              type: string
            hourly_rate:
              type: number
            description:
              type: string
    responses:
      201:
        description: Provider created successfully
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    
    provider = ProviderProfile(
        user_id=user_id,
        business_name=data['business_name'],
        service_category_id=data['service_category_id'],
        location=data['location'],
        hourly_rate=data['hourly_rate'],
        description=data.get('description', '')
    )
    
    db.session.add(provider)
    db.session.commit()
    
    return jsonify({'message': 'Provider profile created successfully'}), 201