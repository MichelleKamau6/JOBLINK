#!/usr/bin/env python3
import os
import sys
from app import create_app

if __name__ == '__main__':
    app = create_app()
    print("Starting JobLink server on http://localhost:5000")
    print("Available endpoints:")
    print("- POST /api/auth/register")
    print("- POST /api/auth/login")
    print("- GET /api/auth/me")
    app.run(host='0.0.0.0', port=5000, debug=True)