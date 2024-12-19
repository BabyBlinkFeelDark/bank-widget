import pytest, os
from src.utils import parser
import json

def test_parser():
    assert parser("/home/babyblinkfeeldark/PycharmProjects/homework/data/operations.json") == []
