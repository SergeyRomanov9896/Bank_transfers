
import pytest
from datetime import datetime

from src.file_path import DATA_JSON
from src.utils.date_editor import date_editor

def test_correct_date_output():
    """Проверка на правильный вывод даты ДД.ММ.ГГГГ"""
    load_date = date_editor(DATA_JSON)

    for date in load_date:
        string = str(date)
        assert datetime.strptime(string, '%d.%m.%Y')

def test_incorrect_date_output():
    """Проверка на ошибку если дата выводится не в заданном значении ДД.ММ.ГГГГ"""
    load_date = date_editor(DATA_JSON)

    with pytest.raises(ValueError):
        for date in load_date:
            string = str(date)
            assert datetime.strptime(string, '%m.%d.%Y')
            assert datetime.strptime(string, '%Y.%m.%d')
            assert datetime.strptime(string, '%m.%Y.%d')
            assert datetime.strptime(string, '%Y.%d.%m')
            assert datetime.strptime(string, '%d.%Y.%m')