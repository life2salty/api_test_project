# API Test Automation Project

**Author:** [Your name or nickname]  
**Tech stack:** Python, Pytest, Requests, REST API  
**Status:** ✅ All tests passing

_________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Project Description

A collection of automated tests for the public REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com) (a fake API for testing).  
This project demonstrates my skills in **API test automation** using Python: writing positive/negative tests, validating status codes, JSON structure, and response fields.

This is my first portfolio project. I am actively learning and improving my skills to become a Junior QA Automation Engineer.

_________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Test Coverage

| Endpoint     | Method | Scenario                         | Validation                               |
|--------------|--------|----------------------------------|------------------------------------------|
| `/posts`     | GET    | Get all posts                    | Status 200, non-empty list               |
| `/posts/{id}`| GET    | Get a single post                | Status 200, correct ID                   |
| `/posts`     | POST   | Create a new post                | Status 201, title field, id exists       |
| `/posts/{id}`| PUT    | Fully update a post              | Status 200                               |
| `/posts/{id}`| DELETE | Delete a post                    | Status 200 or 204                        |
| `/posts/99999`| GET   | Get non‑existent post            | Status 404 (negative test)               |

Total tests: **6** (all passing ✅)

_________________________________________________________________________________________________________________________________________________________________________________________________________________________

## How to Run Locally

### Requirements
- Python 3.7+
- Git (optional, for cloning)

### Steps

1. **Clone the repository**
   
   git clone https://github.com/api_test_project/Mansur.git
   
2. Create and activate a virtual environment (recommended)

   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows 

3. Install dependencies

   pip install -r requirements.txt

4. Run test

   pytest

You will see green dots/checkmarks if all pass.

To generate an HTML report: pytest --html=report.html

5. Open report.html in your browser.

 
Sample Output
text
collected 6 items
tests/test_posts.py ......  [100%]
====================== 6 passed in 0.52s ======================

________________________________________________________________________________________________________________________________________________________________________________________________________________________

Project Structure
text
.
├── tests/
│   └── test_posts.py          # main tests
├── conftest.py                # fixture api_client (base URL, session)
├── requirements.txt           # dependencies
├── pytest.ini                 # pytest settings (optional)
├── README.md                  # this file
└── report.html                # generated after test run

________________________________________________________________________________________________________________________________________________________________________________________________________________________   

Future Improvements
  - Add tests for /comments and /users endpoints
  
  - Implement JSON Schema validation using jsonschema
  
  - Add logging
  
  - Set up CI/CD with GitHub Actions (auto-run tests on push)
  
  - Write UI tests with Playwright for a demo website

________________________________________________________________________________________________________________________________________________________________________________________________________________________

Contact

I am looking for my first job or internship in QA (manual/auto). Ready to complete a test assignment.

Telegram: [@El_Zipp0]

Email: [mansurcheg98@gmail.com]
