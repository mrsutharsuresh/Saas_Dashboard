import requests
import sys

BASE_URL = "http://127.0.0.1:8001"

def test_flow():
    # 1. Register
    email = "test@example.com"
    password = "password123"
    print(f"1. Registering user {email}...")
    reg_response = requests.post(f"{BASE_URL}/auth/register", json={"email": email, "password": password})
    
    if reg_response.status_code == 200:
        print("   Success: User registered.")
    elif reg_response.status_code == 400 and "already registered" in reg_response.text:
        print("   Note: User already exists, proceeding to login.")
    else:
        print(f"   Failed: {reg_response.text}")
        sys.exit(1)

    # 2. Login
    print("2. Logging in...")
    login_response = requests.post(f"{BASE_URL}/auth/token", data={"username": email, "password": password})
    if login_response.status_code != 200:
        print(f"   Failed Login: {login_response.text}")
        sys.exit(1)
    
    token = login_response.json()["access_token"]
    print("   Success: Got JWT Token.")
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Create Project
    print("3. Creating Project...")
    proj_data = {"title": "Test Project", "survey_number": "999", "portal_data": "{}"}
    proj_response = requests.post(f"{BASE_URL}/projects/", json=proj_data, headers=headers)
    if proj_response.status_code != 200:
        print(f"   Failed Project Creation: {proj_response.text}")
        sys.exit(1)
    print("   Success: Project Created.")

    # 4. List Projects
    print("4. Listing Projects...")
    list_response = requests.get(f"{BASE_URL}/projects/", headers=headers)
    if list_response.status_code != 200:
        print(f"   Failed List Projects: {list_response.text}")
        sys.exit(1)
    
    projects = list_response.json()
    print(f"   Success: Found {len(projects)} projects.")
    print("Verification Complete!")

if __name__ == "__main__":
    test_flow()
