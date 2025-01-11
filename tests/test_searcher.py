import pytest
from src.searcher import search_for_str

def test_pars_csv_success(test_transaction_descriptions):
    assert list(search_for_str(test_transaction_descriptions, "Перевод организации"))== 0
