import pytest

def test_get_all_posts(api_client):
    session, url = api_client
    response = session.get(f"{url}/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_post(api_client):
    session, url = api_client
    post_id = 1
    response = session.get(f"{url}/posts/{post_id}")
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id

def test_create_post(api_client):
    session, url = api_client
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = session.post(f"{url}/posts", json=new_post)
    assert response.status_code == 201
    created = response.json()
    assert created["title"] == "foo"
    assert "id" in created

def test_update_post(api_client):
    session, url = api_client
    updated_data = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = session.put(f"{url}/posts/1", json=updated_data)
    assert response.status_code == 200

def test_delete_post(api_client):
    session, url = api_client
    response = session.delete(f"{url}/posts/1")
    assert response.status_code in [200, 204]

def test_get_nonexistent_post(api_client):
    session, url = api_client
    response = session.get(f"{url}/posts/99999")
    assert response.status_code == 404