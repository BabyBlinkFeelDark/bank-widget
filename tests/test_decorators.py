import pytest, os
from src.mask import get_mask_card_number,get_mask_account

def test_log_without_log_param(capsys):
    get_mask_card_number("1234567812345678")

    captured = capsys.readouterr()
    assert "get_mask_card_number ok" in captured.out


def test_log_err(capsys):
    with pytest.raises(Exception, match="Invalid number"):
        get_mask_card_number("")


def test_log_file_creation():
    get_mask_account("12345678123456781234")
    log_path = '/home/babyblinkfeeldark/PycharmProjects/homework/logs/log_decorators.txt'
    assert os.path.exists(log_path)
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()
        assert "get_mask_account ok" in log_content


def test_log_error_in_file():
    with pytest.raises(TypeError, match="Invalid account"):
        get_mask_account("")

    log_path = '/home/babyblinkfeeldark/PycharmProjects/homework/logs/log_decorators.txt'
    assert os.path.exists(log_path)
    with open(log_path, 'r') as log_file:
        log_content = log_file.read()
        assert "get_mask_account error:" in log_content


