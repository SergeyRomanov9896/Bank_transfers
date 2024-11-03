
from src.utils.sort_last_five import sort_last_five

def card_details(path: str) -> dict:
    """Возвращает данные карты того кто переводит и данные карты кому переводит"""
    load_five = sort_last_five(path)

    list_cards_from = []
    list_cards_to = []

    for card in load_five:
        card_from = str(card["from"])
        card_to = str(card["to"])

        parts_1 = card_from.split(" ")
        parts_2 = card_to.split(" ")

        if parts_1[-1].isdigit() and parts_2[-1].isdigit():
            card_name_from = " ".join(parts_1[:-1])
            card_name_to = " ".join(parts_2[:-1])

            card_number_from = parts_1[-1]
            card_number_to = parts_2[-1]

            if len(card_number_from) == 16:
                from_str = f"{card_name_from} {card_number_from[:4]} {card_number_from[4:6]}** **** {card_number_from[12:16]}"
            else:
                from_str = f"{card_name_from} {card_number_from[:4]} {card_number_from[4:6]}** **** {card_number_from[16:20]}"

            if len(card_number_to) == 20:
                to_str = f"{card_name_to} **** **** **** {card_number_to[16:20]}"
            else:
                to_str = f"{card_name_to} **** **** **** {card_number_to[12:16]}"

            list_cards_from.append(from_str)
            list_cards_to.append(to_str)

    credit_cards = {"from": list_cards_from,
                    "to": list_cards_to}

    return credit_cards