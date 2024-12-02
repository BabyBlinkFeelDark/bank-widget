import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# @pytest.mark.parametrize(
#     "input_data",
#     (
#         [(1,5), (0,1000)]
#     ),
# )
def test_card_generator():
    assert card_number_generator(1,5) == 1
