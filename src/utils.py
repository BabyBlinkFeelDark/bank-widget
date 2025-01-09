import json, os
from src.external_api import convert
from dotenv import load_dotenv


def parser(file_path: str) -> list[dict]:
    """
    Парсит JSON-файл по указанному пути и возвращает данные в виде списка словарей.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        list[dict]: Список транзакций, если данные корректны. Пустой список, если файл отсутствует
                    или данные не являются списком.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            if not isinstance(data, list):  # Проверяем, что это список
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def transactions_summary(transaction: dict) -> float:
    """
    Возвращает сумму операции в рублях для заданной транзакции.

    Если валюта транзакции не "RUB", выполняется конвертация через API.

    Args:
        transaction (dict): Словарь, представляющий транзакцию.
                            Ожидается структура:
                            {
                                "code": "Код валюты",
                                "operationAmount": {
                                    "amount": "Сумма операции",
                                    "currency": {"code": "Код валюты"}
                                }
                            }

    Returns:
        float: Сумма операции в рублях.

    Raises:
        ValueError: Если `transaction` не является словарём.
    """
    if not isinstance(transaction, dict):
        raise ValueError("Транзакция должна быть словарём")
    if transaction.get("code") != "RUB":
        load_dotenv()
        rez = convert(
            transaction.get("operationAmount", {}).get("currency", {}).get("code", {}),
            transaction.get("operationAmount", {}).get("amount", {}),
            os.getenv("API_TOKEN"),
        )
    else:
        rez = transaction.get("operationAmount", {}).get("currency", {}).get("amount", {})
    return float(rez)
