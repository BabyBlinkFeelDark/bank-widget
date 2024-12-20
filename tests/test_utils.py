import pytest, os
from src.utils import parser,transactions_summary
import json
from unittest.mock import Mock



def test_parser():
    mock_json = Mock(return_value=[{"data":"value"}])
    parser = mock_json
    assert parser("/home/babyblinkfeeldark/PycharmProjects/homework/data/operations.json") == [{"data":"value"}]

def test_transactions_summary():