import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79XX XXXX 6361"),
        ("Visa Gold 7000792289606361", "Visa Gold 7000 79XX XXXX 6361"),
        ("Visa 7000792289606361", "Visa 7000 79XX XXXX 6361"),
    ],
)
def test_correct_mask_account(input_data, expected_output):
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize("input_data", ["12121", "Счет", ""])
def test_correct_data_account(input_data):
    with pytest.raises(TypeError):
        mask_account_card(input_data)


def test_absence_data_account():
    with pytest.raises(AttributeError):
        mask_account_card(None)


@pytest.mark.parametrize("input_data", ["12121", "дата", "24-03-11T02", "", None])
def test_exec_date_time(input_data):
    with pytest.raises(TypeError):
        get_date(input_data)


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2001-20-11T02:26:18.67", "11.20.2001"),
    ],
)
def test_correct_date_transcript(input_data, expected_output):
    assert get_date(input_data) == expected_output