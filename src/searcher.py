import re,collections
from typing import List, Dict

test_data = [
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
            "description": "Перев0д организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def search_for_str(data: List[Dict], target: str) -> List[Dict]:
    def search_in_dict(d: Dict, target: str) -> bool:
        for key, value in d.items():
            if isinstance(value, dict):
                if search_in_dict(value, target):
                    return True
            elif isinstance(value, (list)):
                if any(search_in_dict(item, target) if isinstance(item, dict) else re.search(target, str(item)) for item in value):
                    return True
            elif re.search(target, str(value)):
                return True
        return False

    result = [item for item in data if search_in_dict(item, target)]
    return result



