from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_list):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, \
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED',\
'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date':'2018-10-14T08:21:33.419441'}],\
state = "EXECUTED") == filter_list


def test_eror_key_filter_by_state(error_filter_list):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, \
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED',\
'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date':'2018-10-14T08:21:33.419441'}],\
state = "EXEkhED") == error_filter_list
    assert filter_by_state([], state = "EXECUTED") == error_filter_list
    assert filter_by_state([], state="") == error_filter_list
    assert filter_by_state([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}, \
{'id': 939719570, 'state': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED',\
'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date':'2018-10-14T08:21:33.419441'}],\
state = "EXECUTED") == error_filter_list


def test_filter_by_state_key_CANCELED(filter_key_CANCELED):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, \
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED',\
'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date':'2018-10-14T08:21:33.419441'}],\
state = "CANCELED") == filter_key_CANCELED


def test_sort_by_date(sort_by_date_revers):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date':\
'2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], \
date = True) == sort_by_date_revers

def test_sort_by_no_revers_date(sort_by_date_no_revers):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date':\
'2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], \
date = False) == sort_by_date_no_revers


def test_sort_by_date_no_list(sort_by_date_no_list):
    assert sort_by_date([], date = False) == sort_by_date_no_list