import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert(currency, amount, token):
    """
    Конвертирует сумму из одной валюты в рубли через внешний API.

    Args:
        currency (str): Код валюты исходной суммы (например, "USD").
        amount (str): Сумма для конвертации.
        token (str): Токен для авторизации в API.

    Returns:
        float: Сконвертированная сумма в рублях, полученная из API.

    Raises:
        requests.RequestException: Если запрос к API завершился ошибкой.
    """
    headers = {"apikey": token}
    r = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers=headers
    )
    response_data = r.json()
    return response_data.get("result")
