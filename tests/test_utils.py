import pytest, os
from src.utils import parser,transactions_summary
import json
from unittest.mock import Mock, patch



def test_parser():
    mock_json = Mock(return_value=[{"data":"value"}])
    parser = mock_json
    assert parser("/home/babyblinkfeeldark/PycharmProjects/homework/data/operations.json") == [{"data":"value"}]


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