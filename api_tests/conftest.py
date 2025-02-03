import pytest
import requests
import random

@pytest.fixture
def url():
    return "http://localhost:8888"

@pytest.fixture
def headers():
    return {"content-type": "application/json"}

@pytest.fixture
def user(url, headers):
    response = requests.get(f'{url}/users?limit=1', headers=headers)
    return response.json()["users"][0]

@pytest.fixture
def token(user, url, headers):
    username = user["username"]
    password = user["password"]

    response = requests.post(
        url=f'{url}/auth/login', 
        headers=headers,
        json = {"username": username, "password": password}
    )
    return response.json()["accessToken"]

# Generate dummy user with random id
@pytest.fixture
def dummy_user_data(user):
    random_user = user
    random_user["id"] = 209
    return random_user

# Create a new user
@pytest.fixture
def new_user(url, token, dummy_user_data):
    response = requests.post(
        url=f'{url}/users/add',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"},
        json = dummy_user_data,
    )
    return response.json()

# Get first 10 users
@pytest.fixture
def get_10_users(url, token):
    response = requests.get(
        url=f'{url}/users?limit=10',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"}
    )
    return response.json()