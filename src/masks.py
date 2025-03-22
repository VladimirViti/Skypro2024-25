def get_mask_card_number(card_number: int) -> str:
    """Функцию маскировки номера банковской карты"""
    number_1 = str(card_number)
    str_number = number_1[-16:]
    if str_number.isdigit() == True:
        return f"{number_1[0:-12]} {number_1[-12:-10]}** **** {number_1[-4:]}"
    elif len(number_1) < 16:
        return "Номер карты состоит из 16 символов"
    else:
        return "Номер карты должен состоять только из цифр"


def get_mask_account(get_accout: int) -> str:
    """Функцию маскировки номера банковского счета"""
    get_accout_str = str(get_accout)
    if len(get_accout_str) == 20 and get_accout_str.isdigit() == True:
        return f"{get_accout_str[:-20]}**{get_accout_str[-4:]}"
    else:
        return "Номер счета состоит оз 20 цифрр. Вводите номер счета без пробелов и знаков припенания"
