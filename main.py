from src.processing import filter_by_state
from src.utils import parser
from src.widget import get_date, mask_account_card

def choose_operation():
    answers = {}
    print("""Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")
    answers["choose_operation"] = input().lower()
    return answers

def choose_status(answers):
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    answers['choose_status'] = input().lower()
    return answers

def choose_data_sort(answers):
    print("""Отсортировать операции по дате? Да/Нет""")
    answers['choose_data_sort'] = input().lower()
    return answers

def choose_data_sort_cur(answers):
    print("""Отсортировать по возрастанию или по убыванию?""")
    answers['choose_data_sort_cur'] = input().lower()
    return answers

def choose_currency(answers):
    print("""Выводить только рублевые тразакции? Да/Нет""")
    answers['choose_currency'] = input().lower()
    return answers

def choose_filt(answers):
    print("""Отфильтровать список транзакций по определенному слову 
    в описании? Да/Нет""")
    answers['choose_filt'] = input()
    return answers

def start():
    d = choose_operation()

    if int(d['choose_operation']) < 1 or int(d['choose_operation']) > 3:
        print("Некорректная операция")
        start()
    else:
        choose_status(d)

    while d['choose_status'].lower() not in ['executed', 'canceled', 'pending']:
        print("Некорректный статус")
        choose_status(d)

    choose_data_sort(d)
    while d['choose_data_sort'].lower() not in ['да', 'нет']:
        print("Некорректный статус")
        choose_data_sort(d)

    choose_data_sort_cur(d)
    while d['choose_data_sort_cur'].lower() not in ['по возрастанию', 'по убыванию']:
        print("Некорректный статус")
        choose_data_sort_cur(d)

    choose_currency(d)
    while d['choose_currency'].lower() not in ['да', 'нет']:
        print("Некорректный статус")
        choose_currency(d)

    choose_filt(d)
    while d['choose_filt'].lower() not in ['да', 'нет']:
        print("Некорректный статус")
        choose_filt(d)

    return d

answers = start()
match answers['choose_operation']:
    case '1':
        print(filter_by_state(parser('/home/babyblinkfeeldark/PycharmProjects/homework/data/operations.json'), answers['choose_status'].upper()))
    case '2':
        print("hello word")
    case '3':
        print("hello word")

