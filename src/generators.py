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


def filter_by_currency(transactions:list,currency:str) -> list:
    if transactions == []:
        raise TypeError("There are no transactions!")
    return [transaction for transaction in transactions if transaction.get("operationAmount",{}).get("currency",{}).get("code",{}) == currency]


def transaction_descriptions(transactions:list) -> list:
    if not isinstance(transactions, list) or transactions==[] or transactions==[{}] :
        raise TypeError("Incorrect dataset")
    if not all(isinstance(item, dict) for item in transactions):
        raise TypeError("The list contains incorrect data")
    return [transaction.get("description") for transaction in transactions if transaction.get("description")!=None]