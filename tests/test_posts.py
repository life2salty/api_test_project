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
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
    assert post["userId"] > 0


def test_create_post(api_client):
    session, url = api_client
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = session.post(f"{url}/posts", json=new_post)

    assert response.status_code == 201
    created = response.json()
    assert created["title"] == new_post["title"]
    assert created["body"] == new_post["body"]
    assert created["userId"] == new_post["userId"]
    assert "id" in created


def test_update_post(api_client):
    session, url = api_client
    updated_data = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1,
    }
    response = session.put(f"{url}/posts/1", json=updated_data)

    assert response.status_code == 200
    updated = response.json()
    assert updated["id"] == updated_data["id"]
    assert updated["title"] == updated_data["title"]
    assert updated["body"] == updated_data["body"]
    assert updated["userId"] == updated_data["userId"]


def test_delete_post(api_client):
    session, url = api_client
    response = session.delete(f"{url}/posts/1")

    assert response.status_code in [200, 204]
    if response.status_code == 200:
        assert isinstance(response.json(), dict)


def test_get_nonexistent_post(api_client):
    session, url = api_client
    response = session.get(f"{url}/posts/99999")

    assert response.status_code == 404


def test_get_all_comments(api_client):
    session, url = api_client
    response = session.get(f"{url}/comments")

    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) > 0
    assert {"postId", "id", "name", "email", "body"} <= comments[0].keys()


def test_get_all_users(api_client):
    session, url = api_client
    response = session.get(f"{url}/users")

    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    assert {"id", "name", "username", "email"} <= users[0].keys()
