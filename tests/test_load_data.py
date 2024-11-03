
import pytest

from src.file_path import DATA_JSON
from src.utils.load_data import load_data

def test_checking_data():
    """Проверка на наличия данных"""
    data_json = load_data(DATA_JSON)

    assert data_json

    for key in data_json:
        if key != {}:
            assert isinstance(key["id"], int)
            assert isinstance(key["state"], str)
            assert isinstance(key["date"], str)
            assert isinstance(key["operationAmount"], dict)
            assert isinstance(key["operationAmount"]["amount"], str)
            assert isinstance(key["operationAmount"]["currency"], dict)
            assert isinstance(key["operationAmount"]["currency"]["name"], str)
            assert isinstance(key["operationAmount"]["currency"]["code"], str)

            assert isinstance(key["description"], str)
        if "from" not in key:
            continue
        else:
            assert isinstance(key["from"], str)
            assert isinstance(key["to"], str)


def test_key_not_empty():
    """Проверка на пустой словарь в списке словарей"""
    data_json = load_data(DATA_JSON)

    for key in data_json:
        if key == {}:
            with pytest.raises(AssertionError):
                assert key