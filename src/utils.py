import json, os
from src.external_api import convert
from dotenv import load_dotenv

def parser(file_path):
    with open(file_path, 'r') as f:
        return list(json.load(f))

def transactions_summary(transaction):
    if transaction.get("code")!='RUB':
        load_dotenv()
        rez = convert(transaction.get("operationAmount", {}).get("currency", {}).get("code", {}), transaction.get("operationAmount", {}).get("currency", {}).get("amount", {}), os.getenv("API_TOKEN"))
    else:
        rez = float(transaction.get("operationAmount", {}).get("currency", {}).get("amount", {}))
    return rez


print(transactions_summary({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }))