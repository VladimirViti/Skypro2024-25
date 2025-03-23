from src.widget import mask_account_card, get_date
from src.masks import get_mask_card_number, get_mask_account

def test_mask_namber_card(card_number):
    assert mask_account_card("Visa Platinum 7000792289606361") == card_number


def test_mask_namber_accout(mask_account):
    assert mask_account_card("Счет 73654108430135874305") == mask_account


def test_error_mask_account_cart(error_mask_account_cart):
    assert mask_account_card("Visa Platinum 7000792о2p89606361") == error_mask_account_cart
    assert mask_account_card("792ор289606361") == error_mask_account_cart
    assert mask_account_card("dsadsdsad") == error_mask_account_cart
    assert mask_account_card("546161") == error_mask_account_cart
    assert mask_account_card("8494dfsf/.") == error_mask_account_cart


def test_get_date():
    assert get_date("11.03.2024па") == "Некоректые данные"
    assert get_date("") == "Некоректые данные"


def test_get_date_not_assert():
    assert get_date("2024-03-11T02:26:18.671407") == '"11.03.2024"'

