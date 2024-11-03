import json

def load_data(path: str) -> list:
    """Загружает json файл"""
    with open(path, encoding="UTF-8") as file:
        data_json = json.load(file)

        return data_json