import json
import os

def load_test_data():
    path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "test_data.json")
    with open(path, encoding='utf-8') as f:
        return json.load(f)
