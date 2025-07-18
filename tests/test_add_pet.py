import json
from src.api.pet_api import PetAPI
from src.utils.data_loader import load_test_data

data = load_test_data()


def test_add_pet():
    with open("data/test_data.json") as f:
        data = json.load(f)

    response = PetAPI.add_pet(data["pet"])
    assert response.status_code == 200
    assert response.json()["name"] == data["pet"]["name"]
