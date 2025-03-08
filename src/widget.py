def mask_account_card(number_catr: str) -> str:
    """ Функция, которая умеет обрабатывать информацию как о картах, так и о счетах """
    mask_number = "Name card XXXX XX** **** XXXX"
    account_mask = "Счет **xxxx"
    number_1 = str(number_catr)
    if number_catr[-17] == " ":
        return f"{number_1[0:-12]} {number_1[-12:-10]}{mask_number[-12:-4]} {number_1[-4:]}"
    else:
        return f"{account_mask[:-4]}{number_1[-4:]}"


def get_date(date: str) -> str:
    """ Функцию, которая принимает на вход строку с датой в формате
'2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
'ДД.ММ.ГГГГ' """
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    return f'"{day}.{month}.{year}"'
