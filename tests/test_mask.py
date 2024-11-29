import pytest

from src.mask import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("input_data",
    [
    "12121",
    "Счет",
    "",
    None,
                         ])

def test_correct_data_mask_account(input_data):
    with pytest.raises(TypeError):
        get_mask_card_number(input_data)