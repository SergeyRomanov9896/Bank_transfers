
from src.utils.sort_last_five import sort_last_five

def transfer_amount(path: str) -> list:
    """Возвращает кол-во переведенной суммы и вид валюты"""
    load_five = sort_last_five(path)

    list_sum = []

    for amount in load_five:
        list_sum.append(f"{amount["operationAmount"]["amount"]} {amount["operationAmount"]["currency"]["name"]}")

    return list_sum