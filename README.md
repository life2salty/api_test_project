# API Test Automation Project

**Author:** Mansur Alimbekov  
**GitHub:** [@life2salty](https://github.com/life2salty)  
**Tech stack:** Python, pytest, Requests, jsonschema, REST API testing  
**Project type:** Learning / portfolio project

## About the project

This repository contains automated API tests for [JSONPlaceholder](https://jsonplaceholder.typicode.com), a public demo REST API.

The project is part of my QA Engineer learning journey and demonstrates API testing with Python, pytest, Requests, JSON Schema validation, and GitHub Actions. It is a portfolio project; I am continuing to develop my testing skills and looking for my first QA opportunity.

## Portfolio projects

- **Python API automation:** [pytest + Requests tests](./tests/test_posts.py) with JSON Schema validation and GitHub Actions CI.
- **Postman API testing:** [13-request collection](./postman/JSONPlaceholder_API_Tests.postman_collection.json) with environment variables, response assertions, JSON Schema checks, negative scenarios, Newman execution, and HTML/JUnit reports in CI. See the [Postman project README](./postman/README.md).

## QA documentation

- [API Test Plan](./docs/test-plan.md) — scope, approach, entry/exit criteria, risks, and limitations.
- [API Test Cases](./docs/test-cases.md) — 14 existing automated scenarios and clearly separated ideas for future coverage.

## Test coverage

The suite currently contains 14 tests across two files:

| File | Scenario | Current checks |
|---|---|---|
| `tests/test_posts.py` | Get all posts | HTTP 200, response is a non-empty list |
| `tests/test_posts.py` | Get a single post | HTTP 200, correct ID, title/body types, positive user ID |
| `tests/test_posts.py` | Create a post | HTTP 201, title/body/userId match request, response contains ID |
| `tests/test_posts.py` | Update a post | HTTP 200, returned ID/title/body/userId match request |
| `tests/test_posts.py` | Delete a post | HTTP 200 or 204; JSON object when response is HTTP 200 |
| `tests/test_posts.py` | Request a non-existent post | HTTP 404 |
| `tests/test_posts.py` | Get all comments | HTTP 200, non-empty list, expected fields in first item |
| `tests/test_posts.py` | Get all users | HTTP 200, non-empty list, expected fields in first item |
| `tests/test_schemas.py` | Post response schema | Validate a single post against a JSON Schema |
| `tests/test_schemas.py` | Posts list item schema | Validate a post from the list against a JSON Schema |
| `tests/test_schemas.py` | Comment response schema | Validate a comment against a JSON Schema |
| `tests/test_schemas.py` | User response schema | Validate a user against a JSON Schema |
| `tests/test_schemas.py` | Non-existent comment | HTTP 404 |
| `tests/test_schemas.py` | Non-existent user | HTTP 404 |

## Tech stack

- **Python** — test implementation
- **pytest** — test runner and fixtures
- **Requests** — HTTP requests
- **jsonschema** — validate API response structure
- **pytest-html** — generate HTML test reports
- **GitHub Actions** — automatically run tests on pushes and pull requests to `master`

## Run the tests locally

### 1. Clone the repository

```bash
git clone https://github.com/life2salty/api_test_project.git
cd api_test_project
```

### 2. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the test suite

```bash
python -m pytest -v
```

### 5. Generate an HTML report (optional)

```bash
python -m pytest -v --html=report.html --self-contained-html
```

Open `report.html` in a browser to review the report.

## Continuous integration and test reports

The GitHub Actions workflow is located at `.github/workflows/pytest.yml`. It installs dependencies, runs the tests, creates `report.html`, and uploads it as an artifact named `api-test-report`. Artifacts are retained for 14 days.

To download a report:

1. Open the [GitHub Actions runs](https://github.com/life2salty/api_test_project/actions).
2. Open a completed run.
3. Find **Artifacts** near the bottom of the run summary.
4. Download `api-test-report` and open `report.html` from the ZIP archive.

## Important note about JSONPlaceholder

JSONPlaceholder is a demo API. POST, PUT, and DELETE requests return simulated responses; they do not persist changes to a real database. These tests check the responses provided by the demo service, not durable data changes.

## Possible next improvements

- Add more negative scenarios and boundary-value tests.
- Improve reusable assertions and test data management.
- Validate additional fields and nested objects in response schemas.
- Add a pull request template and issue templates.

## About me

I am learning QA engineering and building portfolio projects to practice manual and automated testing. I am looking for my first QA Engineer opportunity or internship and am open to completing a test assignment.

- **GitHub:** [github.com/life2salty](https://github.com/life2salty)
