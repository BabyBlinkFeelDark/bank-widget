# from src.widget import mask_account_card

def get_mask_card_number(card_num: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя видимыми только первые 6 и последние 4 цифры.
    :param card_num: Номер кредитной карты в виде строки.
    :return: Маскированный номер карты
    """
    return card_num[:4] + " " + card_num[4:6] + "XX XXXX " + card_num[-4:]


def get_mask_account(card_num: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.
    :param card_num: Номер счета в виде строки.
    :return: Маскированный номер счета
    """
    return f"**{card_num[-4:]}"

