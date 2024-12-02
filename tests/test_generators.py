import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.mark.parametrize(
    "input_spoint,input_enpoint, expected_output",
    [
        (1,  5, ['0000000000000001',
                '0000000000000002',
                '0000000000000003',
                '0000000000000004',
                '0000000000000005']),
        (9, 10, ['0000000000000009',
                  '0000000000000010', ]),
        ("1","2",[0]),
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