import random
import string
from apis.users_api import UserAPI

def generate_random_email():
    return f"qa_user_{''.join(random.choices(string.ascii_lowercase, k=5))}@testmail.com"

def test_create_verify_delete_user():
    api = UserAPI("https://automationexercise.com/api")
    name = "QA User"
    email = generate_random_email()
    password = "Test@123"

    # Create user
    create_response = api.create_account(name, email, password)
    assert create_response.status_code == 200
    assert create_response.json().get("responseCode") == 201

    # Verify login
    login_response = api.verify_login(email, password)
    assert login_response.status_code == 200
    assert login_response.json().get("responseCode") == 200

    # Get user detail
    details_response = api.get_user_detail_by_email(email)
    assert details_response.status_code == 200
    assert "user" in details_response.json()

    # Delete user
    delete_response = api.delete_account(email)
    assert delete_response.status_code == 200
    assert delete_response.json().get("responseCode") == 200
