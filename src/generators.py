from typing import Any, Dict, List


def card_number_generator(start_point, end_point):
    result = [str(i) for i in range(start_point,end_point+1)]
    map_result = list(map(real_card_number,result))
    # return "".join((16-len(str(result[4])))*"0"+str(result[4]))
    return map_result

def real_card_number(card_list):
     for card in card_list:
         return "".join((16-len(card))*"0"+card)

def filter_by_currency():
    return 1


def transaction_descriptions():
    return 1