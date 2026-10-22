# API Test Plan — JSONPlaceholder

**Project:** API Test Automation Portfolio  
**Tester:** Mansur Alimbekov  
**Target:** https://jsonplaceholder.typicode.com  
**Status:** Learning / portfolio document; not a commercial test assignment.

## 1. Objective

Verify selected REST API response behavior, including HTTP status codes, response structure, required fields, data types, and selected negative scenarios. The project demonstrates test design and automation practice using Python, pytest, Requests, and JSON Schema.

## 2. Scope

### In scope
- Retrieve posts, comments, and users.
- Retrieve an individual post, comment, and user.
- Submit simulated create, update, and delete requests for posts.
- Request resources with non-existent IDs.
- Validate response fields and JSON structure.
- Run automated tests locally and through GitHub Actions.
- Execute a separate Postman collection with Newman.

### Out of scope
- Authentication and authorization.
- Performance, load, security, and penetration testing.
- Persistent data verification after write operations.
- Production reliability or service-level guarantees.

## 3. Test approach

- **Functional API checks:** verify expected endpoint behavior and status codes.
- **Response validation:** check JSON types, required fields, and selected field values.
- **Negative checks:** request IDs that do not exist and verify 404 responses.
- **Contract/schema checks:** validate representative post, comment, and user responses against JSON Schema.
- **Automation:** run tests with pytest; execute the Postman collection with Newman.
- **CI:** use GitHub Actions to run the Python suite on pushes and pull requests to `master` and publish an HTML report artifact.

## 4. Test data

The project uses the public JSONPlaceholder demo API. The tests use known demo resource IDs (for example, post ID 1) and a high ID (99999) to check not-found behavior.

## 5. Entry and exit criteria

**Entry criteria**
- The public demo API is reachable.
- Python dependencies are installed for local execution, or the GitHub Actions runner can install them.
- The repository and test files are available.

**Exit criteria**
- The automated test run completes and produces a report.
- Any failures are reviewed and distinguished from possible environment or third-party demo-service issues.
- Known service limitations are documented.

## 6. Risks and limitations

JSONPlaceholder is a demo service. POST, PUT, and DELETE operations return simulated responses and do not persist changes to a real database. Passing these checks does not prove persistence, production readiness, or full API coverage. External service availability can also affect test runs.

## 7. Evidence

- [Python tests](../tests/test_posts.py)
- [JSON Schema tests](../tests/test_schemas.py)
- [Postman collection documentation](../postman/README.md)
- [GitHub Actions runs](https://github.com/life2salty/api_test_project/actions)

## 8. Future improvements

- Add boundary-value and query-parameter scenarios.
- Validate content types and additional response headers.
- Add reusable schema and assertion helpers where appropriate.
- Record test execution results and investigate reproducible failures.
- Add a concise defect-report example only when an actual reproducible defect is observed.
