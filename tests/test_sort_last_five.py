
import pytest

from src.file_path import DATA_JSON
from src.utils.sort_last_five import sort_last_five

def test_checking_key_sorting():
    """Проверка сортировки по ключам state=EXECUTED"""
    last_five = sort_last_five(DATA_JSON)

    for i in last_five:
        assert i["state"] != "CANCELED"

def test_checking_date_sorting():
    """Проверка того что дата отсортирована по убыванию"""
    last_five = sort_last_five(DATA_JSON)

    dates = [item['date'] for item in last_five]
    assert dates == sorted(dates, reverse=True)

def test_checking_five_operations():
    """Проверка того что вывод равен 5 операциям"""
    last_five = sort_last_five(DATA_JSON)

    assert len(last_five) == 5

def test_errors_checking():
    """Проверка на ошибки"""
    last_five = sort_last_five(DATA_JSON)

    for i in last_five:
        with pytest.raises(AssertionError):
            assert i["from"] == "CANCELED"

    with pytest.raises(AssertionError):
        assert len(last_five) != 5