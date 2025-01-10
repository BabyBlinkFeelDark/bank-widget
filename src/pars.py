import csv, pandas as pd

def pars_csv(file_path: str):
    try:
        with open(file_path) as file:
            reader = csv.reader(file)
            return list(reader)
    except:
        raise FileNotFoundError("Файл не найден")

def pars_xlsx(file_path: str):
    try:
        reader = pd.read_excel(file_path)
        return reader.head()
    except:
        raise FileNotFoundError("Файл не найден")

# print(pars_csv('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions.csv'))
# print(pars_xlsx('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions_excel.xlsx'))