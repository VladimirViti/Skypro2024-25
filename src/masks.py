def get_mask_card_number(number_catr: int) -> str:
    """Функцию маскировки номера банковской карты"""
    mask_number = "XXXX XX** **** XXXX"
    number_1 = str(number_catr)
    return f"{number_1[:4]} {number_1[4:6]}{mask_number[7:-4]} {number_1[-4:]}"


def get_mask_account(get_accout: int) -> str:
    """Функцию маскировки номера банковского счета"""
    mask_account = "**XXXX"
    get_accout_str = str(get_accout)
    return f"{mask_account[:2]}{get_accout_str[-4:]}"
