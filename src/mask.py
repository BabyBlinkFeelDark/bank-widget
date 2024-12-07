from src.decorators import log


@log("log_file_mask")
def get_mask_card_number(card_num: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя видимыми только первые 6 и последние 4 цифры.
    :param card_num: Номер кредитной карты в виде строки.
    :return: Маскированный номер карты
    """
    if len(card_num) != 16:
        raise TypeError("Invalid number")
    else:
        return card_num[:4] + " " + card_num[4:6] + "XX XXXX " + card_num[-4:]

@log("log_file_mask")
def get_mask_account(card_num: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.
    :param card_num: Номер счета в виде строки.
    :return: Маскированный номер счета
    """
    if len(card_num) != 20:
        raise TypeError("Invalid account")
    return f"**{card_num[-4:]}"

get_mask_card_number("123467815135678")
get_mask_account("6468647367889779589")