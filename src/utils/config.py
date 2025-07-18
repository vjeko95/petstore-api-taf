import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {
    "api_key": API_KEY,
    "Content-Type": "application/json"
}
