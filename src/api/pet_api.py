import requests
import os

BASE_URL = "https://petstore.swagger.io/v2"
API_KEY = os.getenv("PETSTORE_API_KEY", "test_api_key")

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "api_key": API_KEY
}

class PetAPI:

    @staticmethod
    def add_pet(pet_data):
        return requests.post(f"{BASE_URL}/pet", json=pet_data, headers=HEADERS)

    @staticmethod
    def get_pet(pet_id):
        return requests.get(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)

    @staticmethod
    def update_pet(pet_data):
        return requests.put(f"{BASE_URL}/pet", json=pet_data, headers=HEADERS)
