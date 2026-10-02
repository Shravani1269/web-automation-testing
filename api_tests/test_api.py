import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_get_post():
    response = requests.get(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


@pytest.mark.api
def test_get_multiple_posts():
    response = requests.get(
        f"{BASE_URL}/posts"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data[:5]:
        assert "id" in post
        assert "title" in post
        assert "body" in post
        assert "userId" in post


@pytest.mark.api
def test_create_post():
    payload = {
        "title": "Automation Testing",
        "body": "Testing REST APIs using Python requests",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


@pytest.mark.api
def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Automation Test",
        "body": "Updated API test data",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]


@pytest.mark.api
def test_delete_post():
    response = requests.delete(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200


@pytest.mark.api
def test_invalid_endpoint():
    response = requests.get(
        f"{BASE_URL}/invalid-endpoint"
    )

    assert response.status_code == 404