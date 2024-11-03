
from src.utils.load_data import load_data

def sort_last_five(path: str) -> list:
    """Возвращает последние 5 успешных операций клиента и удаляет пустой словарь в одном из id,
     отсортировывает по EXECUTED, from и date"""
    data = load_data(path)

    load_fix_list = [fix for fix in data if fix]  # Удаляет пустой словарь в списке словарей
    sort_executed = [state for state in load_fix_list if state.get("state") == "EXECUTED" and state.get("from")] # Сортировка по EXECUTE и from
    sort_executed.sort(key=lambda time: time['date'])  # Сортировка даты по возрастанию
    last_five_operations = [sort_executed[i] for i in range(len(sort_executed)-5, len(sort_executed))] # Вывод последних 5 операций
    last_five_operations.sort(reverse=True, key=lambda time: time['date']) # Сортировка даты по убыванию

    return last_five_operations