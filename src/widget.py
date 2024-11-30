import re

import src.mask


def mask_account_card(card_data: str) -> str:
    """
    Маскирует номер кредитной карты или счета
    :param card_data: Номер кредитной карты или счета в виде строки.
    :return: Тип вводимых данных (счет или карта) и маскированный номер карты или счета
    """
    if card_data is None:
        raise AttributeError("Enter your card/account details")
    if card_data.split()[:-1] == []:
        raise TypeError("Check the correctness of the entered data")

    if " ".join(card_data.split()[:-1]) == "Счет":
        return " ".join(card_data.split()[:-1]) + " " + src.mask.get_mask_account(card_data.split()[-1])
    return " ".join(card_data.split()[:-1]) + " " + src.mask.get_mask_card_number(card_data.split()[-1])


def get_date(current_time) -> str:
    """
    Приводит дату к формату DD.MM.YYYY
    :param current_time: Текущее время
    :return: Время в формате DD.MM.YYYY
    """

    pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:.\d{1,6})?$"

    # Проверка соответствия
    if not re.fullmatch(pattern, current_time):
        raise TypeError("Incorrect date!")
        return None
    return current_time[8:10] + "." + current_time[5:7] + "." + current_time[:4]
