
from src.file_path import DATA_JSON
from src.utils.transfer_amount import transfer_amount

def test_transfer_amount():
    """Проверяет то что сумма перевода состоит из цифр"""
    load_transfer = transfer_amount(DATA_JSON)

    list_count = []

    for currency in load_transfer:
        string_1 = str(currency)
        breaking = string_1.split(" ")
        list_count.append(breaking[0])

    for i in list_count:
        l = list(i)
        l.remove(".")
        jon = "".join(l)
        assert jon.isdigit()