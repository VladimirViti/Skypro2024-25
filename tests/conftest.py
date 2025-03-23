import pytest


@pytest.fixture
def card_number() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def content_error_card_number() -> str:
    return "Номер карты должен состоять только из цифр"


@pytest.fixture
def content_len_card_number() -> str:
    return "Номер карты состоит из 16 символов"


@pytest.fixture
def mask_account() -> str:
    return "Счет **4305"


@pytest.fixture
def account_data_is_missing() -> str:
    return "Номер счета состоит оз 20 цифрр. Вводите без пробелов и знаков припенания"


@pytest.fixture
def account_value_get_mask_accout() -> str:
    return "Номер счета состоит оз 20 цифрр. Вводите без пробелов и знаков припенания"


@pytest.fixture
def error_mask_account_cart() -> str:
    return "Некоректые данные"


@pytest.fixture
def filter_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def error_filter_list() -> list:
    return []


@pytest.fixture
def filter_key_CANCELED() -> list:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_revers() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_no_revers() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def sort_by_date_no_list() -> list:
    return []


@pytest.fixture
def error_get_date() -> list:
    return "Некоректые данные"


@pytest.fixture
def get_date_not_error() -> list:
    return '"11.03.2024"'
