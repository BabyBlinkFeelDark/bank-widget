import pytest
from src.mask import get_mask_account, get_mask_card_number

def test_log(capsys):
    get_mask_card_number("1234567812345678")
    captured = capsys.readouterr()
    assert captured.out == 'Вызов функции: get_mask_card_number\n'


def test_log_err(capsys):
    with pytest.raises(Exception, match="Invalid number"):
        get_mask_card_number("")