# API Test Cases — JSONPlaceholder

**Project:** API Test Automation Portfolio  
**Status:** Test design documentation for a learning project.

The cases below describe current coverage in the repository. They are not a claim of commercial testing experience.

| ID | Endpoint / scenario | Test idea | Expected result | Current automation |
|---|---|---|---|---|
| API-001 | `GET /posts` | Retrieve all posts | HTTP 200; JSON list is non-empty | Python / pytest |
| API-002 | `GET /posts/1` | Retrieve a known post | HTTP 200; ID matches; title/body are strings; userId is positive | Python / pytest |
| API-003 | `POST /posts` | Submit a new post payload | HTTP 201; response echoes submitted fields and includes an ID | Python / pytest |
| API-004 | `PUT /posts/1` | Submit updated post fields | HTTP 200; response contains expected ID and updated fields | Python / pytest |
| API-005 | `DELETE /posts/1` | Submit delete request | HTTP 200 or 204; if 200, response is a JSON object | Python / pytest |
| API-006 | `GET /posts/99999` | Request a non-existent post | HTTP 404 | Python / pytest |
| API-007 | `GET /comments` | Retrieve comments | HTTP 200; non-empty list; expected fields present in first item | Python / pytest |
| API-008 | `GET /users` | Retrieve users | HTTP 200; non-empty list; expected fields present in first item | Python / pytest |
| API-009 | `GET /posts/1` | Validate post response schema | Response matches required fields and data types in POST_SCHEMA | Python / pytest |
| API-010 | `GET /posts` | Validate a list item against post schema | HTTP 200; list non-empty; first item matches schema | Python / pytest |
| API-011 | `GET /comments/1` | Validate comment response schema | HTTP 200; response matches COMMENT_SCHEMA | Python / pytest |
| API-012 | `GET /users/1` | Validate user response schema | HTTP 200; response matches USER_SCHEMA | Python / pytest |
| API-013 | `GET /comments/99999` | Request a non-existent comment | HTTP 404 | Python / pytest |
| API-014 | `GET /users/99999` | Request a non-existent user | HTTP 404 | Python / pytest |

## Additional scenarios to implement

These are ideas for future work, not claims that the checks already exist:
- Filter posts by a valid `userId` and verify every returned post has that `userId`.
- Verify response `Content-Type` is JSON for selected endpoints.
- Check behavior for malformed or unsupported query parameters where the demo API defines expected behavior.
- Add more robust schema constraints for fields and nested objects when supported by the API contract.

## Important limitation

JSONPlaceholder simulates write operations. The create/update/delete checks validate returned responses only; they do not prove that data is persisted.
