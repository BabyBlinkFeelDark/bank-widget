import pytest, os
from src.mask import get_mask_account, get_mask_card_number

def test_log(capsys):
    get_mask_card_number("1234567812345678")
    captured = capsys.readouterr()
    assert captured.out == "get_mask_card_number ok\n"


def test_log_err(capsys):
    with pytest.raises(Exception, match="Invalid number"):
        get_mask_card_number("")


def test_log_file_creation(clean_log_file):
    get_mask_card_number("1234567812345678")
    log_path = '/home/babyblinkfeeldark/PycharmProjects/homework/logs/log_decorators.txt'
    assert os.path.exists(log_path)
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()
        assert "get_mask_card_number ok" in log_content


def test_log_error_in_file():
    with pytest.raises(TypeError, match="Invalid number"):
        get_mask_card_number("")

    log_path = '/home/babyblinkfeeldark/PycharmProjects/homework/logs/log_decorators.txt'
    assert os.path.exists(log_path)
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()
        assert "get_mask_card_number error: Invalid number" in log_content