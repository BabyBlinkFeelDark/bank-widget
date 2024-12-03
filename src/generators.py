max_card_number = 9999999999999999


def card_number_generator(start_point: int, end_point: int) -> list:
    """

    Генерирует список номеров карт в формате строк с разбивкой каждые 4 символа пробелом.

    :param start_point: Начальная точка генерации номеров (включительно).
    :param end_point: Конечная точка генерации номеров (включительно).
    :return: Список строк с номерами карт, разделенными пробелами каждые 4 цифры.
    :raises IndexError: Если end_point превышает лимит max_card_number или start_point >= end_point.
    """
    if end_point > max_card_number:
        raise IndexError("The card number limit has been exceeded!")
    if start_point >= end_point:
        raise IndexError("start_point must be less than end_point!")
    if start_point < end_point:
        result = [
            " ".join(number[i : i + 4] for i in range(0, len(number), 4))
            for number in (str(i).zfill(16) for i in range(start_point, end_point + 1))
        ]
    return result


def filter_by_currency(transactions: list, currency: str) -> list:
    """
    Фильтрует список транзакций, возвращая только те, где код валюты совпадает с переданным.

    :param transactions: Список транзакций, каждая из которых представлена словарем.
    :param currency: Код валюты, например "USD".
    :return: Список транзакций, соответствующих заданному коду валюты.
    :raises TypeError: Если список транзакций пуст или содержит некорректные данные.
    """
    if not isinstance(transactions, list) or not transactions:
        raise TypeError("The transaction list is empty or not a list!")
    if not all(isinstance(item, dict) for item in transactions):
        raise TypeError("The transaction list contains incorrect data!")
    return [
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency
    ]


def transaction_descriptions(transactions: list) -> list:
    """
    Извлекает описания транзакций из списка.

    :param transactions: Список транзакций, каждая из которых представлена словарем.
    :return: Список строк с описаниями транзакций.
    :raises TypeError: Если список транзакций некорректен или содержит некорректные данные.
    """
    if not isinstance(transactions, list) or not transactions:
        raise TypeError("Invalid or empty transaction list!")
    if not all(isinstance(item, dict) for item in transactions):
        raise TypeError("The transaction list contains incorrect data!")
    return [
        transaction.get("description") for transaction in transactions if transaction.get("description") is not None
    ]
