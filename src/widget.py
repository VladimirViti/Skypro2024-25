import masks
# Импорт функций для маски номера карты и счета


def mask_account_card(number_catr: str) -> str:
    """ Функция, которая умеет обрабатывать информацию как о картах, так и о счетах """
    if number_catr[-17] == " ":
        masks_number_card = str(masks.get_mask_card_number(number_catr))
        return masks_number_card
    else:
        account_mask = str(masks.get_mask_account(number_catr))
        return account_mask


def get_date(date: str) -> str:
    """ Функцию, которая принимает на вход строку с датой в формате
'2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
'ДД.ММ.ГГГГ' """
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    return f'"{day}.{month}.{year}"'
