
import re
from datetime import datetime

from src.utils.sort_last_five import sort_last_five

def date_editor(path: str) -> list:
    """Возвращает корректное значения даты: ДД.ММ.ГГГГ"""
    load_five = sort_last_five(path)

    list_date = []

    for time in load_five:
        date_form = str(time["date"])
        sp_1 = re.split("[-T,\\s]+", date_form)
        formatted_date = f"{sp_1[2]}.{sp_1[1]}.{sp_1[0]}"
        dt = datetime.strptime(formatted_date, '%d.%m.%Y')
        list_date.append(f"{dt.day}.{dt.month}.{dt.year}")

    return list_date