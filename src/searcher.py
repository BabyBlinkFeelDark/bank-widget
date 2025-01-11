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


def search_for_str(data: List[Dict], target: str):
    for i in range(len(data)):
        for k, v in test_data[0].items():
            if isinstance(v,dict):
                print(v.values())
            trans = re.findall(target, str(v))
            if trans != []:
                print(trans," i = ", i)
                return data[i]

print(search_for_str(test_data, "руб."))

# print(test_data[0])
#
# for k,v in test_data[0].items():
#     print(k, " ", v)

