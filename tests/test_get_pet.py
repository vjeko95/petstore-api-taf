import json
from src.api.pet_api import PetAPI
from src.utils.data_loader import load_test_data

data = load_test_data()


def test_get_pet():
    with open("data/test_data.json") as f:
        data = json.load(f)

    PetAPI.add_pet(data["pet"])

    response = PetAPI.get_pet(data["pet"]["id"])
    assert response.status_code == 200
    assert response.json()["id"] == data["pet"]["id"]
