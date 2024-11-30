import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_data",
    [
        "12121",
        "Счет",
        "",
        None,
    ],
)
def test_correct_data_mask_number(input_data):
    with pytest.raises(TypeError):
        get_mask_card_number(input_data)


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        ("7000792289606361", "7000 79XX XXXX 6361"),
        ("7790006063922861", "7790 00XX XXXX 2861"),
    ],
)
def test_correct_output_mask_number(input_data, output_data):
    assert get_mask_card_number(input_data) == output_data


@pytest.mark.parametrize(
    "input_data",
    [
        "12121",
        "Счет",
        "",
        None,
    ],
)
def test_correct_data_account(input_data):
    with pytest.raises(TypeError):
        get_mask_account(input_data)


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        ("64686473678894779589", "**9589"),
        ("77900061922861063434", "**3434"),
    ],
)
def test_correct_output_mask_account(input_data, output_data):
    assert get_mask_account(input_data) == output_data
