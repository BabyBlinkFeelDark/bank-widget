def card_number_generator(start_point: int, end_point: int) -> list:
    """
    Генерирует список номеров карт в формате строк с разбивкой каждые 4 символа пробелом.

    :param start_point: Начальная точка генерации номеров (включительно).
    :param end_point: Конечная точка генерации номеров (включительно).
    :return: Список строк с номерами карт, разделенными пробелами каждые 4 цифры.
    :raises IndexError: Если end_point превышает лимит max_card_number или start_point >= end_point.
    """
    max_card_number = 9999999999999999  # Максимальное значение карты
    if not isinstance(start_point, int) and not isinstance(end_point, int):
        raise TypeError("start_point and end_point must be integers")
    if start_point > end_point:
        raise ValueError("start_point must be less than or equal to end_point")

    if end_point > max_card_number:
        raise ValueError(f"The end_point cannot exceed {max_card_number}")

    def infinite_sequence(start):
        point = start
        while True:
            yield point
            point += 1

    card_numbers = infinite_sequence(start_point)

    result = []
    for _ in range(end_point - start_point + 1):
        card_number = str(next(card_numbers)).zfill(16)  # Получить одно значение
        formatted_card = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
        result.append(formatted_card)

    return result



    # if end_point > max_card_number:
    #     raise IndexError("The card number limit has been exceeded!")
    # if start_point >= end_point:
    #     raise IndexError("start_point must be less than end_point!")
    # if start_point < end_point:
    #     result = [
    #         " ".join(number[i : i + 4] for i in range(0, len(number), 4))
    #         for number in (str(i).zfill(16) for i in range(start_point, end_point + 1))
    #     ]
    # return result


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
