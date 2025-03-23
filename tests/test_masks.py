from src.masks import get_mask_card_number, get_mask_account
from typing import Any


def test_get_mask_card_number(card_number: str) -> Any:
    assert get_mask_card_number("Visa Platinum 7000792289606361") == card_number


def test_get_mask_card_number_int(content_error_card_number: str) -> Any:
    assert get_mask_card_number("Visa Platinum 7000792ор289606361") == content_error_card_number


def test_get_mask_card_number_len(content_len_card_number: str) -> Any:
    assert get_mask_card_number("792ор289606361") == content_len_card_number


def test_get_mask_account(mask_account: str) -> Any:
    assert get_mask_account("Счет 73654108430135874305") == mask_account


def get_mask_account_data_is_missing(account_data_is_missing: str) -> Any:
    assert get_mask_account_data_is_missing("") == account_data_is_missing
    assert get_mask_account_data_is_missing("fsddaf") == account_data_is_missing


def test_value_get_mask_accout(account_value_get_mask_accout: str) -> Any:
    assert get_mask_account("dsadsdsad") == account_value_get_mask_accout
    assert get_mask_account("546161") == account_value_get_mask_accout
    assert get_mask_account("8494dfsf/.") == account_value_get_mask_accout
