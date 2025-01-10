import csv, pandas as pd

def pars_csv(file_path: str):
    try:
        with open(file_path) as file:
            reader = csv.reader(file)
            return list(reader)
    except:
        raise FileNotFoundError("Файл не найден")

def pars_xlsx(file_path: str):
    with open(file_path) as file:
        reader = csv.reader(file)
        return list(reader)

# print(pars_csv('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions.csv'))
print(pars_csv('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions.csv'))