import requests, os
from dotenv import load_dotenv

load_dotenv()
# os.getenv("LOGIN_PASSWORD")

# transaction={
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }

def convert(currency, amount, token):
    headers = {
        'apikey': token
    }
    r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers = headers)
    response_data = r.json()
    return response_data.get('result')
# print(transaction.get("operationAmount", {}).get("amount", {}), {})
# print(convert(transaction.get("operationAmount", {}).get("currency", {}).get("code", {}), transaction.get("operationAmount", {}).get("amount", {}), os.getenv("API_TOKEN")))