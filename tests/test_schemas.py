from jsonschema import validate


POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

COMMENT_SCHEMA = {
    "type": "object",
    "required": ["postId", "id", "name", "email", "body"],
    "properties": {
        "postId": {"type": "integer"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"},
    },
}

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
}


def test_post_response_matches_json_schema(api_client):
    session, url = api_client
    response = session.get(f"{url}/posts/1")

    assert response.status_code == 200
    validate(instance=response.json(), schema=POST_SCHEMA)


def test_posts_list_item_matches_json_schema(api_client):
    session, url = api_client
    response = session.get(f"{url}/posts")

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert posts
    validate(instance=posts[0], schema=POST_SCHEMA)


def test_comment_response_matches_json_schema(api_client):
    session, url = api_client
    response = session.get(f"{url}/comments/1")

    assert response.status_code == 200
    validate(instance=response.json(), schema=COMMENT_SCHEMA)


def test_user_response_matches_json_schema(api_client):
    session, url = api_client
    response = session.get(f"{url}/users/1")

    assert response.status_code == 200
    validate(instance=response.json(), schema=USER_SCHEMA)


def test_get_nonexistent_comment(api_client):
    session, url = api_client
    response = session.get(f"{url}/comments/99999")

    assert response.status_code == 404


def test_get_nonexistent_user(api_client):
    session, url = api_client
    response = session.get(f"{url}/users/99999")

    assert response.status_code == 404
