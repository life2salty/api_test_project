# API Test Automation Project

**Author:** Mansur Alimbekov  
**GitHub:** [@life2salty](https://github.com/life2salty)  
**Tech stack:** Python, pytest, Requests, REST API testing  
**Project type:** Learning / portfolio project

## About the project

This repository contains automated API tests for [JSONPlaceholder](https://jsonplaceholder.typicode.com), a public demo REST API.

The project is part of my QA Engineer learning journey and demonstrates basic API testing with Python, pytest, and Requests. It is a portfolio project; I am continuing to develop my testing skills and looking for my first QA opportunity.

## Test coverage

The current suite contains eight tests:

| Endpoint | Method | Scenario | Current checks |
|---|---|---|---|
| `/posts` | GET | Retrieve all posts | HTTP 200, response is a non-empty list |
| `/posts/1` | GET | Retrieve one post | HTTP 200, correct ID, title/body types, positive user ID |
| `/posts` | POST | Submit a new post | HTTP 201, title/body/userId match request, response contains ID |
| `/posts/1` | PUT | Submit an update for a post | HTTP 200, returned ID/title/body/userId match request |
| `/posts/1` | DELETE | Submit a delete request | HTTP 200 or 204; JSON object when response is HTTP 200 |
| `/posts/99999` | GET | Request a non-existent post | HTTP 404 |
| `/comments` | GET | Retrieve all comments | HTTP 200, non-empty list, expected fields in first item |
| `/users` | GET | Retrieve all users | HTTP 200, non-empty list, expected fields in first item |

## Tech stack

- **Python** — test implementation
- **pytest** — test runner and fixtures
- **Requests** — HTTP requests
- **pytest-html** — optional HTML test report
- **GitHub Actions** — run tests automatically on pushes and pull requests to `master`

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

### 5. (Optional) Generate an HTML report

```bash
python -m pytest --html=report.html
```

Open `report.html` in a browser to review the report. The report is generated locally and is not committed automatically.

## Continuous integration

The GitHub Actions workflow is located at `.github/workflows/pytest.yml`. It installs the dependencies and runs the test suite when code is pushed to `master`, when a pull request targets `master`, or when manually triggered from the Actions tab.

See [GitHub Actions](https://github.com/life2salty/api_test_project/actions) for run results. The workflow has been added to the repository; its successful execution should be verified in the Actions tab.

## Important note about JSONPlaceholder

JSONPlaceholder is a demo API. POST, PUT, and DELETE requests return simulated responses; they do not persist changes to a real database. These tests check the responses provided by the demo service, not durable data changes.

## Possible next improvements

- Add response schema validation.
- Add tests for more negative scenarios and boundary values.
- Improve reusable assertions and test data management.
- Save an HTML report as a GitHub Actions artifact.

## About me

I am learning QA engineering and building portfolio projects to practice manual and automated testing. I am looking for my first QA Engineer opportunity or internship and am open to completing a test assignment.

- **GitHub:** [github.com/life2salty](https://github.com/life2salty)
