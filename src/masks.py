def get_mask_card_number(card_number: int) -> str:
    """Функцию маскировки номера банковской карты"""
    number_1 = str(card_number)
    return f"{number_1[0:-12]} {number_1[-12:-10]}** **** {number_1[-4:]}"


def get_mask_account(get_accout: int) -> str:
    """Функцию маскировки номера банковского счета"""
    get_accout_str = str(get_accout)
    return f"{get_accout_str[:-20]}**{get_accout_str[-4:]}"
