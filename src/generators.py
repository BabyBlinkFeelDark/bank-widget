from typing import Any, Dict, List


max_card_number = 9999999999999999

def card_number_generator(start_point: int , end_point : int) -> list:
    if end_point > max_card_number:
        raise IndexError("The card number limit has been exceeded!")
    if start_point < end_point:
        result = [
            ' '.join(number[i:i + 4] for i in range(0, len(number), 4))
            for number in (str(i).zfill(16) for i in range(start_point, end_point + 1))
        ]
        return result
    else:
        raise IndexError("start_point < end_point")


def filter_by_currency(transactions,currency):
    return [transaction for transaction in transactions if transaction.get("operationAmount",{}).get("currency",{}).get("code",{}) == currency]


def transaction_descriptions():
    return 1