from src.mask import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
