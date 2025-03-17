def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    nev_list_of_dictionaries = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            nev_list_of_dictionaries.append(dictionary)
    return nev_list_of_dictionaries


# Проверка работы функции
# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id':\
# 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED',\
# 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date':\
# '2018-10-14T08:21:33.419441'}], state = "EXECUTED"))


def sort_by_date(list_dictionaries: list[dict], date: bool = True) -> list[dict]:
    """Функция вовращает новый список, отсортированный по дате (date)"""
    sorted_list = sorted(list_dictionaries, key=lambda x: x["date"], reverse=date)
    return sorted_list


# Проверка работы функции
# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, \
# 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date':
# '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], \
# date = True))
