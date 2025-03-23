from src.masks import get_mask_account, get_mask_card_number

# Импорт функций для маски номера карты и счета


def mask_account_card(number_catr: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if len(number_catr) < 17:
        return "Некоректые данные"
    if number_catr[-17] == " ":
        masks_number_card = str(get_mask_card_number(number_catr))
        return masks_number_card
    elif number_catr[:4] == "Счет":
        account_mask = str(get_mask_account(number_catr))
        return account_mask
    else:
        return "Некоректые данные"


# def get_date(date: str) -> str:
#     """Функцию, которая принимает на вход строку с датой в формате
#     '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
#     'ДД.ММ.ГГГГ'"""
#     if len(date) != 26:
#         return "Некоректые данные"
#     year = date[0:4]
#     month = date[5:7]
#     day = date[8:10]
#     if year.isdigit() != True or month.isdigit() != True or day.isdigit() != True:
#         return "Некоректые данные"
#     return f'"{day}.{month}.{year}"'
def get_date(date: str) -> str:
    """Функцию, которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
    'ДД.ММ.ГГГГ'"""
    if len(date) != 26:
        return "Некоректые данные"
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return "Некоректые данные"
    else:
        return f'"{day}.{month}.{year}"'
