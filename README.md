# Pet Store API Test Automation Framework

This project implements a **Test Automation Framework (TAF)** for validating key endpoints of the [Swagger Petstore API](https://petstore.swagger.io/).

## Table of Contents

* [Overview](#overview)
* [Installation](#installation)
* [Project Structure](#project-structure)
* [Running Tests](#running-tests)
* [API Under Test](#api-under-test)
* [Authentication](#authentication)
* [Dependencies](#dependencies)
* [Test Scenarios](#test-scenarios)

## Overview

This framework automates the testing of the following API endpoints:

* `POST /pet` – Add a new pet
* `GET /pet/{petId}` – Retrieve pet by ID
* `PUT /pet` – Update an existing pet

## Installation

```bash
# Clone the repository
git clone https://github.com/vjeko95/petstore-api-taf.git
cd petstore-api-taf

# (Optional) Create virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
petstore-api-taf/
├── data/
│   └── test_data.json           # Static JSON data for testing
├── src/
│   └── api/
│       └── pet_api.py           # Abstraction layer for API calls
├── tests/
│   ├── test_add_pet.py         # Test for POST /pet
│   ├── test_get_pet.py         # Test for GET /pet/{id}
│   └── test_update_pet.py      # Test for PUT /pet
├── .env                        # (Optional) Environment variables like API keys
├── requirements.txt            # Python dependencies
└── pytest.ini                  # Pytest configuration
```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_add_pet.py
```

## API Under Test

* [Swagger Petstore Documentation](https://petstore.swagger.io/)

## Authentication

If enabled, all requests can include an `api_key` header:

```python
headers = {"api_key": os.getenv("API_KEY")}
```

You can define the API key in a `.env` file:

```
API_KEY=test_api_key
```

## Dependencies

Key libraries used:

* `pytest` – Test runner
* `requests` – HTTP client
* `python-dotenv` – Loads `.env` file values

Install them with:

```bash
pip install -r requirements.txt
```

## Test Scenarios

Each test case:

* Load pet data from `test_data.json`
* Sends API request (POST, GET, PUT)
* Asserts expected response code and data

## Author

Developed by Vjekoslav Večković
