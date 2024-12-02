from typing import Any, Dict, List


def card_number_generator(start_point: int , end_point : int) -> list:

    result = [str(i).zfill(16) for i in range(start_point, end_point + 1)]
    return result

def filter_by_currency():
    return 1


def transaction_descriptions():
    return 1