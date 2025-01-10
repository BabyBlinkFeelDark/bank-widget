import logging
import os

from src.decorators import log


card_logger = logging.getLogger('utils.parser')
account_logger = logging.getLogger('utils.transactions_summary')
if not os.path.isdir("../log"):
    os.mkdir("../log")
file_handler = logging.FileHandler('../log/utils.log', 'w')
card_logger.addHandler(file_handler)
account_logger.addHandler(file_handler)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(name)s %(message)s')
file_handler.setFormatter(file_formatter)
card_logger.addHandler(file_handler)
account_logger.addHandler(file_handler)
card_logger.setLevel(logging.DEBUG)
account_logger.setLevel(logging.DEBUG)


@log()
def get_mask_card_number(card_num: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя видимыми только первые 6 и последние 4 цифры.
    :param card_num: Номер кредитной карты в виде строки.
    :return: Маскированный номер карты
    """
    if len(card_num) != 16:
        card_logger.error("Несуществующий номер карты")
        raise TypeError("Invalid number")
    else:
        card_logger.info("Карта успешно замаскирована")
        return card_num[:4] + " " + card_num[4:6] + "XX XXXX " + card_num[-4:]


@log("file1.txt")
def get_mask_account(card_num: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.
    :param card_num: Номер счета в виде строки.
    :return: Маскированный номер счета
    """
    if len(card_num) != 20:
        raise TypeError("Invalid account")
    return f"**{card_num[-4:]}"
