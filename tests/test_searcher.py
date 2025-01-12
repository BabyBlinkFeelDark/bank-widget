import pytest
from src.searcher import search_for_str, count_operations_by_category


@pytest.fixture
def get_test_data():
    return [
        {'date': '2018-06-30T02:08:58.425572',
         'description': 'Перевод организации',
         'from': 'Счет 75106830613657916952',
         'id': 939719570,
         'operationAmount': {'amount': '9824.07',
                             'currency': {'code': 'USD', 'name': 'USD'}},
         'state': 'EXECUTED',
         'to': 'Счет 11776614605963066702'},
        {'date': '2018-06-30T02:08:58.425572',
         'description': 'Перевод организации',
         'from': 'Счет 75106830613657916952',
         'id': 9999999,
         'operationAmount': {'amount': '9824.07',
                             'currency': {'code': 'USD', 'name': 'USD'}},
         'state': 'EXECUTED',
         'to': 'Счет 11776614605963066702'},
    ]

def test_search_for_str_success(test_transaction_descriptions,get_test_data):
    assert list(search_for_str(test_transaction_descriptions, "Перевод организации")) == get_test_data

def test_count_operations_by_category_success(test_transaction_descriptions,get_test_data):
    assert list(count_operations_by_category(test_transaction_descriptions, "Перевод организации")) == {'Перевод организации': 2}