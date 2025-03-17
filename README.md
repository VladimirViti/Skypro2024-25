# Учебный проект
## Цель проекта:
1. Отработать практические навыки работы с языком программирования ***Python***;
2. Освоить программное обеспечение ***Pycharm***;
3. Освоить работу с удаленным репозиторием [***Github***](https://github.com/)
### В данном проекте реализованы различные функции:

1. В файле *masks*:

```python 
def get_mask_card_number(number_catr: int) -> str:
    """Функцию маскировки номера банковской карты"""
    number_1 = str(number_catr)
    return f"{number_1[0:-12]} {number_1[-12:-10]}** **** {number_1[-4:]}"


def get_mask_account(get_accout: int) -> str:
    """Функцию маскировки номера банковского счета"""
    get_accout_str = str(get_accout)
    return f"{get_accout_str[:-20]}**{get_accout_str[-4:]}"
```

2. В файле *processing*:

```python
def filter_by_state(list_of_dictionaries:list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
 соответствует указанному значению. """
    nev_list_of_dictionaries = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            nev_list_of_dictionaries.append(dictionary)
    return (nev_list_of_dictionaries)

# Проверка работы функции
# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570,\
# 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': \
# '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], state = "EXECUTED"))


def sort_by_date(list_dictionaries:list[dict], date: bool = True) -> list[dict]:
    """ Функция вовращает новый список, отсортированный по дате (date) """
    sorted_list = sorted(list_dictionaries, key=lambda x: x["date"], reverse=date)
    return (sorted_list)

# Проверка работы функции
#print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, \
# 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': 
# '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], date = True)) ```
```
![Skypro](https://static.cashback.mts.ru/404m4loltfqymqx_lgo.png)

