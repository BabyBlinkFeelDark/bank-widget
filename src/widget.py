# from src.mask import get_mask_account,get_mask_card_number
import re

def mask_account_card(card_data):
    """
    Маскирует номер кредитной карты, оставляя видимыми только первые 6 и последние 4 цифры.
    :param card_num: Номер кредитной карты в виде строки.
    :return: Маскированный номер карты
    """
    bank_name = []
    bank_name = card_data.split()
    card_number = "".join(bank_name[-1])
    bank_name.remove(card_number)
    bank_name = " ".join(bank_name)
    print(bank_name,"   ",card_number)
    return re.findall(r'\d+',card_data)