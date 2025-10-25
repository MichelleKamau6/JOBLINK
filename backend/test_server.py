from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is working'})

@app.route('/api/auth/register', methods=['POST'])
def register():
    return jsonify({'message': 'Register endpoint working'})

@app.route('/api/auth/login', methods=['POST'])
def login():
    return jsonify({'message': 'Login endpoint working'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)