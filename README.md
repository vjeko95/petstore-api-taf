
# 🐾 PetStore API Test Automation Framework

This project is a Test Automation Framework (TAF) designed to validate key API endpoints of the [Swagger Petstore](https://petstore.swagger.io/) using Python and Pytest.

---

## 📌 Objectives

- Automate API tests for:
  - `POST /pet` — Add a new pet
  - `GET /pet/{petId}` — Retrieve a pet by ID
  - `PUT /pet` — Update an existing pet
- Provide a scalable and maintainable structure for API testing
- Optional: Simulate authentication using an API key

---

## 📁 Project Structure

```
petstore-api-taf/
├── data/
│   └── test_data.json           # Test data for pet creation and update
├── src/
│   └── api/
│       └── pet_api.py           # API client with add/get/update methods
├── tests/
│   ├── test_add_pet.py          # Test for POST /pet
│   ├── test_get_pet.py          # Test for GET /pet/{id}
│   └── test_update_pet.py       # Test for PUT /pet
├── .env                         # Optional: Store API key
├── requirements.txt             # Python dependencies
├── pytest.ini                   # (Optional) Pytest config
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/petstore-api-taf.git
cd petstore-api-taf
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Optional: Add an API key

Create a `.env` file:

```env
API_KEY=test_api_key
```

Then make sure `python-dotenv` is used in `pet_api.py` (already supported via `os.getenv()`).

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🧩 Notes

- Test data is managed in `data/test_data.json`.
- Tests are designed to be simple, clear, and directly reflect real API usage.
- The API client in `src/api/pet_api.py` encapsulates all HTTP logic for reusability and clarity.

---

## 🔐 Optional API Key Support

The API client includes support for an optional API key via environment variable.  
If present, it will be added to the request headers.


