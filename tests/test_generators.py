import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.mark.parametrize(
    "input_spoint,input_enpoint, expected_output",
    [
        (1,  5, ['0000 0000 0000 0001',
                '0000 0000 0000 0002',
                '0000 0000 0000 0003',
                '0000 0000 0000 0004',
                '0000 0000 0000 0005']),
        (9, 10, ['0000 0000 0000 0009',
                  '0000 0000 0000 0010', ]),
    ],
)
def test_card_generator(input_spoint,input_enpoint, expected_output):
    assert card_number_generator(input_spoint,input_enpoint) == expected_output


@pytest.mark.parametrize(
    "input_spoint,input_enpoint",
    (
        [
            ("0",1),
            ("1","2")
        ]
    ),
)
def test_incorrect_date(input_spoint,input_enpoint):
    with pytest.raises(TypeError):
        card_number_generator(input_spoint,input_enpoint)


@pytest.mark.parametrize(
    "input_spoint,input_enpoint",
    (
        [
            (2,1),
            (109,9)
        ]
    ),
)
def test_incorrect_date(input_spoint,input_enpoint):
    with pytest.raises(IndexError):
        card_number_generator(input_spoint,input_enpoint)