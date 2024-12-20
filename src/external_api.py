import requests, os
from dotenv import load_dotenv

load_dotenv()
# os.getenv("LOGIN_PASSWORD")

def convert(currency, amount, token):
    headers = {
        'apikey': token
    }
    r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers = headers)
    response_data = r.json()
    return response_data.get('result')

print(convert("USD", "100", os.getenv("API_TOKEN")))