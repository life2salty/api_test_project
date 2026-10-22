# JSONPlaceholder API Testing — Postman

This folder contains an importable Postman collection for practicing REST API testing against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a public demo API.

## Coverage

The collection includes 13 requests covering:
- Retrieve posts, comments, and users
- Create, update, and delete a post (simulated by JSONPlaceholder)
- Filter posts by `userId`
- Assert HTTP status codes and response fields
- Validate post, comment, and user response bodies with JSON Schema
- Negative checks for non-existent post, comment, and user IDs

The collection contains request-level Postman tests. It is a learning portfolio project, not evidence of commercial experience.

## Import into Postman

1. Download or open the collection JSON: [JSONPlaceholder_API_Tests.postman_collection.json](./JSONPlaceholder_API_Tests.postman_collection.json).
2. In Postman, select **Import** and choose the JSON file.
3. Import the environment file: [JSONPlaceholder.postman_environment.json](./JSONPlaceholder.postman_environment.json).
4. Select **JSONPlaceholder API Environment** in the environment selector.
5. Open the collection and select **Run**.
6. Run the full collection and review the request-level test results.

The collection also has default collection variables for `baseUrl`, `postId`, `missingId`, and `userId`, so it can be run without selecting an environment. Environment values override collection variables when an environment is selected.

## Run from the command line with Newman

Newman runs exported Postman Collection v2.1 JSON files from a terminal and can be used in CI:

```bash
npm install --global newman
newman run postman/JSONPlaceholder_API_Tests.postman_collection.json \
  --environment postman/JSONPlaceholder.postman_environment.json
```

From the root of this repository, that command uses the collection and environment files checked into GitHub.

## Continuous integration

The workflow at [`.github/workflows/postman.yml`](../.github/workflows/postman.yml) runs the collection with Newman on pushes and pull requests targeting `master`, and uploads a test report artifact.

View [Postman CI runs](https://github.com/life2salty/api_test_project/actions/workflows/postman.yml).

## Note about the test API

JSONPlaceholder is a fake/demo REST API. POST, PUT, and DELETE responses are simulated; they do not persist changes to a database. The tests validate the response received from the demo service.

## Project links

- [Python API automation tests](../tests/test_posts.py)
- [JSON Schema tests](../tests/test_schemas.py)
- [Main project README](../README.md)
