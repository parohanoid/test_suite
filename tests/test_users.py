import pytest
import requests


def test_current_user(url, token, user):
    response = requests.get(
        url=f'{url}/user/me',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"}
    )
    assert response.status_code == 200

    # Check if the user is the same as the one we got from the fixture
    assert response.json()["id"] == user["id"]
    assert response.json() == user


def test_search_users(url, token, user):
    response = requests.get(
        url=f'{url}/users/search?q=Emily',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"}
    )

    assert response.status_code == 200
    
    res_json = response.json()

    # Check if the user is in the search results
    for res_user in res_json["users"]:
        if res_user["firstName"] == "Emily":
            assert res_user["id"] == user["id"]
            assert res_user == user
            break

def test_filter_users(url, token):
    response = requests.get(
        url=f'{url}/users/filter?key=hair.color&value=Brown&limit=10',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"}
    )

    assert response.status_code == 200

    res_json = response.json()

    # Check if all users have brown hair
    for user in res_json["users"]:
        assert user["hair"]["color"] == "Brown"



def test_create_user(url, token, dummy_user_data):
    response = requests.post(
        url=f'{url}/users/add',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"},
        json = dummy_user_data,
    )
    assert response.status_code == 201


def test_update_user(url, token, new_user):
    response = requests.put(
        url=f'{url}/users/2',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"},
        json = {
            "lastName": "Owais"
            }
    )
    assert response.status_code == 200
    assert response.json()["lastName"] == "Owais"

def test_delete_user(url, token, user):
    response = requests.delete(
        url=f'{url}/users/1',
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["isDeleted"] == True
    assert "deletedOn" in response.json()

    # Add deleted data to new_user
    deletedOn = response.json()["deletedOn"]
    user["isDeleted"] = True
    user["deletedOn"] = deletedOn

    assert response.json() == user

# Check get single users
def test_get_single_user(url, token, get_10_users):
    for user in get_10_users["users"]:
        response = requests.get(
            url=f'{url}/users/{user["id"]}',
            headers={"Authorization": f"Bearer {token}", "content-type": "application/json"}
        )
        assert response.status_code == 200
        assert response.json() == user