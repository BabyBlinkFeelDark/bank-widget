import re
from collections import defaultdict
from typing import List, Dict

from numpy.ma.core import count

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
            "description": "Перевод организации",
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

def count_operations_by_category(data: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    if not categories:
        categories = set(item.get("description") for item in data if item.get("description"))

    category_count = defaultdict(int)
    for item in data:
        description = item.get("description")
        if description and description in categories:
            category_count[description] += 1

    return dict(category_count)

# print(count_operations_by_category(test_data, []))