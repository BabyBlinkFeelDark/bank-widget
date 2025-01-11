from src.generators import filter_by_currency
from src.pars import pars_xlsx, pars_csv
from src.processing import filter_by_state, sort_by_date
from src.searcher import search_for_str, count_operations_by_category
from src.utils import parser, transactions_summary
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

    if d['choose_data_sort'].lower() == 'да':
        choose_data_sort_cur(d)
        while d['choose_data_sort_cur'].lower() not in ['по возрастанию', 'по убыванию']:
            print("Некорректный ответ на сортировку по дате")
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
        operations = filter_by_state(parser('./data/operations.json'), answers['choose_status'].upper())
    case '2':
        operations = pars_csv('./data/transactions.csv')
    case '3':
        operations = pars_xlsx('./data/transactions_excel.xlsx')

if answers['choose_data_sort'].lower() == 'да':
    if answers['choose_data_sort_cur'].lower() == 'по возрастанию':
        operations = sort_by_date(operations)
    elif answers['choose_data_sort_cur'].lower() == 'по убыванию':
        operations = sort_by_date(operations, "DESC")

if answers['choose_currency'].lower() == 'да':
    operations = filter_by_currency(operations, 'RUB')

if answers['choose_filt'].lower() == 'да':
    keyword = input("Введите категорию: ")
    operations = search_for_str(operations, keyword)

if operations == []:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    for oper in operations:
        if str(oper.get('description', '')).lower() == 'открытие счета':
            print(f"""{get_date(oper.get('date', {}))} {oper.get('description', {})}
            {mask_account_card(oper.get('to', {}))}""")  # Сумма не выводится
        if str(oper.get('description', '')).lower() == 'открытие вклада':
            print(f"""{get_date(oper.get('date', {}))} {oper.get('description', {})}
                    {mask_account_card(oper.get('to', {}))}""")  # Сумма не выводится
        else:
            from_account = str(oper.get('from', {})) if oper.get('from', {}) else ''
            to_account = str(oper.get('to', {}))

            if from_account:
                if to_account == ";;;;;;;;" or not to_account:
                    continue
                if 'operationAmount' in oper:
                    print(f"""{get_date(oper.get('date', {}))} {oper.get('description', {})}
                    {from_account} {mask_account_card(from_account)} -> {mask_account_card(to_account)}
                    Сумма: {transactions_summary(oper)}""")
                else:
                    print(f"""{get_date(oper.get('date', {}))} {oper.get('description', {})}
                    {from_account} {mask_account_card(from_account)} -> {mask_account_card(to_account)}""")
            else:
                if to_account == ";;;;;;;;" or not to_account:
                    continue
                if 'operationAmount' in oper:
                    print(f"""{get_date(oper.get('date', {}))} {oper.get('description', {})}
                    {mask_account_card(to_account)}
                    Сумма: {transactions_summary(oper)}""")
                else:
                    print(f"""{get_date(oper.get('date', {}))} {oper.get('description', {})}
                    {mask_account_card(to_account)}""")

