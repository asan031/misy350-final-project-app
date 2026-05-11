import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

USERS_FILE = BASE_DIR / "data" / "users.json"
INVENTORY_FILE = BASE_DIR / "data" / "inventory.json"
SALES_FILE = BASE_DIR / "data" / "sales.json"


class DataManager:

    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def save_json(file_path, data):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)