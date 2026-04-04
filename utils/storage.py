import json
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

            if content == "":
                return []

            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)