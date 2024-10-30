import src.mask


def mask_account_card(card_data: str) -> str:
    """
    Маскирует номер кредитной карты или счета
    :param card_data: Номер кредитной карты или счета в виде строки.
    :return: Тип вводимых данных (счет или карта) и маскированный номер карты или счета
    """
    if " ".join(card_data.split()[:-1]) == "Счет":
        return " ".join(card_data.split()[:-1]) + " " + src.mask.get_mask_account(card_data.split()[-1])
    return " ".join(card_data.split()[:-1]) + " " + src.mask.get_mask_card_number(card_data.split()[-1])


def get_date(current_time: str) -> str:
    """
    Приводит дату к формату DD.MM.YYYY
    :param current_time: Текущее время
    :return: Время в формате DD.MM.YYYY
    """
    return current_time[8:10] + "." + current_time[5:7] + "." + current_time[:4]
