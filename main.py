from src.widget import get_date, mask_account_card

def start():
    print("""Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")
    answer: str
    choose_operation = input()
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    choose_status = input()


start()