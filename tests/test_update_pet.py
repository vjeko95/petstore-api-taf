import json
from src.api.pet_api import PetAPI
from src.utils.data_loader import load_test_data

data = load_test_data()


def test_update_pet():
    with open("data/test_data.json") as f:
        data = json.load(f)

    PetAPI.add_pet(data["pet"])

    response = PetAPI.update_pet(data["updated_pet"])
    assert response.status_code == 200
    assert response.json()["name"] == data["updated_pet"]["name"]
