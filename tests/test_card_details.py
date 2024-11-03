
from src.file_path import DATA_JSON
from src.utils.card_details import card_details

def test_checking_stars():
    """Проверяет на указанное кол-во символа '*'"""
    load_cards = card_details(DATA_JSON)

    assert load_cards["from"][0].count("*") == 6
    assert load_cards["from"][1].count("*") == 6
    assert load_cards["from"][2].count("*") == 6
    assert load_cards["from"][3].count("*") == 6
    assert load_cards["from"][4].count("*") == 6

    assert load_cards["to"][0].count("*") == 12
    assert load_cards["to"][1].count("*") == 12
    assert load_cards["to"][2].count("*") == 12
    assert load_cards["to"][3].count("*") == 12
    assert load_cards["to"][4].count("*") == 12