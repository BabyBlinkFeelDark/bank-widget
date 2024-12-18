import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "input_spoint, input_enpoint, expected_output",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9,
            10,
            [
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
            ],
        ),
    ],
)
def test_card_generator(input_spoint, input_enpoint, expected_output):
    result = list(card_number_generator(input_spoint, input_enpoint))
    assert result == expected_output


@pytest.mark.parametrize(
    "input_spoint,input_enpoint",
    ([("0", 1), ("1", "2")]),
)
def test_incorrect_data_card(input_spoint, input_enpoint):
    with pytest.raises(TypeError):
        list(card_number_generator(input_spoint, input_enpoint))


@pytest.mark.parametrize(
    "input_spoint,input_enpoint",
    ([(2, 1), (109, 9), (9999999999999998, 10000000000000000)]),
)
def test_wrong_points(input_spoint, input_enpoint):
    with pytest.raises(ValueError):
        list(card_number_generator(input_spoint, input_enpoint))


@pytest.mark.parametrize(
    "transactions, currency_code, expected_output",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                },
                {
                    "id": 9999999,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 9999999,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions, currency_code, expected_output):
    assert list(filter_by_currency(transactions, currency_code)) == expected_output


def test_incorrect_list(empty_lists):
    with pytest.raises(TypeError):
        list(test_filter_by_currency(empty_lists))


def test_correct_output_transaction_descriptions(test_transaction_descriptions):
    assert list(transaction_descriptions(test_transaction_descriptions)) == [
        "Перевод организации",
        "Перевод организации",
    ]


def test_incorrect_list_transaction_descriptions(empty_lists):
    with pytest.raises(TypeError):
        list(transaction_descriptions(empty_lists))
