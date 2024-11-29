import pytest

from src.widget import mask_account_card

# @pytest.mark.parametrize("input_data, expected_output",
#     [
#         ("Счет 64686473678894779589","Счет **9589"),
#         ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79XX XXXX 6361")
#     ])
#
# def test_correct_mask_account(input_data, expected_output):
#     assert mask_account_card(input_data) == expected_output
