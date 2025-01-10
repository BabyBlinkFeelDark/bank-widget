import json
import logging
import os

from dotenv import load_dotenv

from src.external_api import convert

parser_logger = logging.getLogger("utils.parser")
ts_logger = logging.getLogger("utils.transactions_summary")
if not os.path.isdir("../log"):
    os.mkdir("../log")
file_handler = logging.FileHandler("../log/utils.log", "w")
parser_logger.addHandler(file_handler)
ts_logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(name)s %(message)s")
file_handler.setFormatter(file_formatter)
parser_logger.addHandler(file_handler)
ts_logger.addHandler(file_handler)
parser_logger.setLevel(logging.DEBUG)
ts_logger.setLevel(logging.DEBUG)


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
            if not isinstance(data, list):
                parser_logger.warning("Некорректные данные")  # Проверяем, что это список
                return []
            parser_logger.info("Парсинг успешен")
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        parser_logger.warning("Файл не найден")  # Проверяем, что это список
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
        parser_logger.error("Транзакция должна быть словарём")  # Проверяем, что это список
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
