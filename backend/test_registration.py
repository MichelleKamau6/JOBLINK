#!/usr/bin/env python3
"""
Test registration endpoint to diagnose issues
"""

import requests
import json

API_URL = "http://localhost:5000/api"

def test_registration():
    """Test user registration"""
    
    print("🧪 Testing Registration Endpoint\n")
    print("=" * 60)
    
    # Test data
    test_users = [
        {
            "email": "testuser1@example.com",
            "password": "password123",
            "name": "Test User 1",
            "role": "client"
        },
        {
            "email": "testprovider@example.com",
            "password": "password123",
            "name": "Test Provider",
            "role": "provider"
        }
    ]
    
    for user in test_users:
        print(f"\n📝 Testing registration for: {user['email']}")
        print("-" * 60)
        
        try:
            response = requests.post(
                f"{API_URL}/auth/register",
                json=user,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            
            if response.status_code == 201:
                print("✅ Registration successful!")
            elif response.status_code == 400:
                print("⚠️  User might already exist or validation error")
            else:
                print(f"❌ Unexpected status code: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ ERROR: Cannot connect to server!")
            print("   Make sure the backend server is running on port 5000")
            print("   Run: cd backend && python run_server.py")
            return
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
    
    print("\n" + "=" * 60)
    print("\n🔍 Testing with missing fields (should fail):")
    print("-" * 60)
    
    # Test with missing required field
    invalid_user = {
        "email": "invalid@example.com",
        "password": "test123"
        # Missing 'name' field
    }
    
    try:
        response = requests.post(
            f"{API_URL}/auth/register",
            json=invalid_user,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code in [400, 422, 500]:
            print("✅ Correctly rejected invalid data")
        else:
            print("⚠️  Should have rejected this request")
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
    
    print("\n" + "=" * 60)
    print("\n✨ Test complete!")

if __name__ == '__main__':
    test_registration()
