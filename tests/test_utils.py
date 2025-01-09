import pytest, os
from src.utils import parser,transactions_summary
import json
from unittest.mock import Mock, patch, mock_open


def test_parser():
    mock_json = Mock(return_value=[{"data":"value"}])
    parser = mock_json
    assert parser("/home/babyblinkfeeldark/PycharmProjects/homework/data/operations.json") == [{"data":"value"}]


def test_parser_file_not_found():
    result = parser("non_existent_file.json")
    assert result == []


def test_parser_invalid_json():
    with patch("builtins.open", mock_open(read_data="{тут ничего нет}")):
        result = parser("invalid_file.json")
        assert result == []


def test_parser_not_a_list():
    with patch("builtins.open", mock_open(read_data=json.dumps({"key": "value"}))):
        result = parser("not_a_list.json")
        assert result == []


def test_parser_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        result = parser("empty_file.json")
        assert result == []


def test_transactions_summary_rub():
    transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    result = transactions_summary(transaction)
    assert result == 31957.58


def test_transactions_summary():
    with patch('requests.get') as mock_get, patch('os.getenv', return_value="mock_token"):
        mock_get.return_value.json.return_value = {'result': 100.5}
        transaction = {
            "code": "USD",
            "operationAmount": {
                "currency": {
                    "code": "USD"
                },
                "amount": 100
            }
        }
        result = transactions_summary(transaction)
        assert result == 100.5


def test_transactions_summary_invalid_transaction():
    with pytest.raises(ValueError, match="Транзакция должна быть словарём"):
        transactions_summary("invalid_transaction")