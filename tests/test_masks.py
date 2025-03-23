from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

def test_get_mask_card_number_int():
    assert get_mask_card_number("Visa Platinum 7000792ор289606361") == "Номер карты должен состоять только из цифр"


def test_get_mask_card_number_len():
    assert get_mask_card_number("792ор289606361") == "Номер карты состоит из 16 символов"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("Счет 73654108430135874305") == "Счет **4305"


def test_value_get_mask_accout():
    assert get_mask_account("dsadsdsad") == "Номер счета состоит оз 20 цифрр. Вводите без пробелов и знаков припенания"
    assert get_mask_account("546161") == "Номер счета состоит оз 20 цифрр. Вводите без пробелов и знаков припенания"
    assert get_mask_account("8494dfsf/.") == "Номер счета состоит оз 20 цифрр. Вводите без пробелов и знаков припенания"
