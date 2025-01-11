from src.widget import get_date, mask_account_card

def start():
    answers = {}
    print("""Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")
    answers["choose_operation"] = input().lower()
    return answers







def choose_operation(answers):
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    answers['choose_status'] = input().lower()

def choose_data_sort(answers):
    print("""Отсортировать операции по дате? Да/Нет""")
    answers['choose_data_sort'] = input().lower()

def choose_data_sort_cur(answers):
    print("""Отсортировать по возрастанию или по убыванию?""")
    answers['choose_data_sort_cur'] = input().lower()

def choose_currency(answers):
    print("""Выводить только рублевые тразакции? Да/Нет""")
    answers['choose_currency'] = input().lower()

def choose_filt(answers):
    print("""Отфильтровать список транзакций по определенному слову 
    в описании? Да/Нет""")
    answers['choose_filt'] = input()



print(start())
