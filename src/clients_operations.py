
from src.file_path import DATA_JSON

from src.utils.date_editor import date_editor
from src.utils.card_details import card_details
from src.utils.transfer_amount import transfer_amount

def clients_operations():
    """Выводит пять последних успешных банковских операций клиента с данными карты и валютной единицей"""
    load_date = date_editor(DATA_JSON)
    load_card = card_details(DATA_JSON)
    load_amount = transfer_amount(DATA_JSON)

    for information in range(len(load_date)):
        print(f"{load_date[information]} Перевод организации\n{load_card["from"][information]}"
              f" -> {load_card["to"][information]}\n{load_amount[information]}")
        print()

clients_operations()