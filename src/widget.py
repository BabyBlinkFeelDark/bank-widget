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
