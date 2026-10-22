# API Test Automation Project

**Author:** Mansur Alimbekov  
**GitHub:** [@life2salty](https://github.com/life2salty)  
**Tech stack:** Python, pytest, Requests, REST API testing  
**Project type:** Learning / portfolio project

## About the project

This repository contains a small set of automated API tests for [JSONPlaceholder](https://jsonplaceholder.typicode.com), a public demo REST API.

The project is part of my QA Engineer learning journey and demonstrates basic API testing with Python, pytest, and Requests. It is a portfolio project; I am continuing to develop my testing skills and looking for my first QA opportunity.

## Test coverage

The current suite contains six tests:

| Endpoint | Method | Scenario | Current checks |
|---|---|---|---|
| `/posts` | GET | Retrieve all posts | HTTP 200, response is a list, list is not empty |
| `/posts/1` | GET | Retrieve one post | HTTP 200, returned post ID is 1 |
| `/posts` | POST | Submit a new post | HTTP 201, title matches, response contains an ID |
| `/posts/1` | PUT | Submit an update for a post | HTTP 200 |
| `/posts/1` | DELETE | Submit a delete request | HTTP 200 or 204 |
| `/posts/99999` | GET | Request a non-existent post | HTTP 404 |

These checks reflect what the tests currently assert. For example, the PUT test currently checks the status code only; it does not validate the updated response fields.

## Tech stack

- **Python** — test implementation
- **pytest** — test runner and fixtures
- **Requests** — HTTP requests
- **pytest-html** — optional HTML test report

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
python -m pytest
```

### 5. (Optional) Generate an HTML report

```bash
python -m pytest --html=report.html
```

Open `report.html` in a browser to review the report. The report is generated locally and is not committed automatically.

> **Note:** The test suite has not been independently executed as part of this README update, so no test result is claimed here.

## Project structure

```text
.
├── tests/
│   └── test_posts.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Important note about JSONPlaceholder

JSONPlaceholder is a demo API. POST, PUT, and DELETE requests return simulated responses; they do not persist changes to a real database. These tests check the responses provided by the demo service, not durable data changes.

## Possible next improvements

- Add assertions for more response fields in the update test.
- Add tests for other endpoints, such as `/comments` and `/users`.
- Add response schema validation.
- Add clearer test names and shared assertions where useful.
- Run the suite automatically with GitHub Actions.

## About me

I am learning QA engineering and building portfolio projects to practice manual and automated testing. I am looking for my first QA Engineer opportunity or internship and am open to completing a test assignment.

- **GitHub:** [github.com/life2salty](https://github.com/life2salty)
