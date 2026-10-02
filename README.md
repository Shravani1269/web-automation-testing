# Web Automation Testing Framework

A Python-based automation testing framework built using Playwright, Pytest, REST API testing, JSON test data, HTML reporting, and GitHub Actions CI.

The framework automates web application workflows and validates REST APIs using reusable, maintainable test components.


## Project Overview

This project demonstrates an end-to-end software testing framework covering:

- Web UI automation
- Page Object Model (POM)
- Functional testing
- Negative testing
- REST API testing
- JSON response validation
- Test data management
- Smoke testing
- Regression testing
- HTML test reporting
- Git version control
- Continuous Integration using GitHub Actions

The web automation tests are implemented using the **SauceDemo** demo application.

REST API tests are implemented using the **JSONPlaceholder** REST API.


## Technologies Used

 Technology & Purpose 

Python - Programming language 
Pytest - Test framework 
Playwright - Web UI automation 
Requests - REST API testing 
JSON - Test data management 
HTML - Test reporting 
Git - Version control 
GitHub - Source code repository 
GitHub Actions - Continuous Integration 


## Framework Architecture

The project follows the **Page Object Model (POM)** design pattern.

web-automation-testing/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── api_tests/
│   └── test_api.py
│
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│
├── test_data/
│   └── test_data.json
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md