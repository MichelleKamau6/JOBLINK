from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import ProviderProfile, ServiceCategory, User

bp = Blueprint('providers', __name__)

@bp.route('', methods=['GET'])
def get_providers():
    """Get All Providers with Advanced Search and Filtering
    ---
    tags:
      - Providers
    parameters:
      - in: query
        name: search
        type: string
        description: Search term for business name or description
      - in: query
        name: category
        type: string
        description: Filter by service category
      - in: query
        name: location
        type: string
        description: Filter by location
      - in: query
        name: min_rate
        type: number
        description: Minimum hourly rate
      - in: query
        name: max_rate
        type: number
        description: Maximum hourly rate
      - in: query
        name: min_rating
        type: number
        description: Minimum average rating
      - in: query
        name: sort_by
        type: string
        description: Sort by (rate_asc, rate_desc, rating_desc, name_asc)
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
        description: List of filtered providers
    """
    query = ProviderProfile.query.filter_by(is_active=True)
    
    # Search functionality
    search_term = request.args.get('search', '').strip()
    if search_term:
        query = query.filter(
            db.or_(
                ProviderProfile.business_name.ilike(f'%{search_term}%'),
                ProviderProfile.description.ilike(f'%{search_term}%')
            )
        )
    
    # Category filter
    category = request.args.get('category')
    if category:
        query = query.join(ServiceCategory).filter(ServiceCategory.name.ilike(f'%{category}%'))
    
    # Location filter
    location = request.args.get('location')
    if location:
        query = query.filter(ProviderProfile.location.ilike(f'%{location}%'))
    
    # Rate filters
    min_rate = request.args.get('min_rate', type=float)
    max_rate = request.args.get('max_rate', type=float)
    if min_rate is not None:
        query = query.filter(ProviderProfile.hourly_rate >= min_rate)
    if max_rate is not None:
        query = query.filter(ProviderProfile.hourly_rate <= max_rate)
    
    # Get all results for rating filter and sorting
    providers = query.all()
    
    # Rating filter (done in Python since it's a property)
    min_rating = request.args.get('min_rating', type=float)
    if min_rating is not None:
        providers = [p for p in providers if p.average_rating >= min_rating]
    
    # Sorting
    sort_by = request.args.get('sort_by', 'name_asc')
    if sort_by == 'rate_asc':
        providers.sort(key=lambda x: x.hourly_rate or 0)
    elif sort_by == 'rate_desc':
        providers.sort(key=lambda x: x.hourly_rate or 0, reverse=True)
    elif sort_by == 'rating_desc':
        providers.sort(key=lambda x: x.average_rating, reverse=True)
    elif sort_by == 'name_asc':
        providers.sort(key=lambda x: x.business_name.lower())
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_providers = providers[start:end]
    
    return jsonify({
        'providers': [{
            'id': p.id,
            'name': p.business_name,
            'service_category': p.category.name if p.category else None,
            'location': p.location,
            'hourly_rate': p.hourly_rate,
            'rating': p.average_rating,
            'review_count': len(p.reviews),
            'image_url': p.image_url,
            'description': p.description
        } for p in paginated_providers],
        'total': len(providers),
        'page': page,
        'per_page': per_page,
        'pages': (len(providers) + per_page - 1) // per_page
    })

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