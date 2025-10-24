from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import cloudinary
import cloudinary.uploader
import os

bp = Blueprint('upload', __name__)

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

@bp.route('/image', methods=['POST'])
@jwt_required()
def upload_image():
    """Upload Image to Cloudinary
    ---
    tags:
      - Upload
    security:
      - Bearer: []
    consumes:
      - multipart/form-data
    parameters:
      - in: formData
        name: image
        type: file
        required: true
        description: Image file to upload
    responses:
      200:
        description: Image uploaded successfully
      400:
        description: No image provided
    """
    if 'image' not in request.files:
        return jsonify({'message': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No image selected'}), 400
    
    try:
        # Upload to Cloudinary
        result = cloudinary.uploader.upload(
            file,
            folder="joblink",
            transformation=[
                {'width': 800, 'height': 600, 'crop': 'limit'},
                {'quality': 'auto'}
            ]
        )
        
        return jsonify({
            'message': 'Image uploaded successfully',
            'url': result['secure_url'],
            'public_id': result['public_id']
        })
    
    except Exception as e:
        return jsonify({'message': f'Upload failed: {str(e)}'}), 500