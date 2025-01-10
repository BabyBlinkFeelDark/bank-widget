import csv, pandas as pd
from typing import List, Union

def pars_csv(file_path: str) -> List[List[str]]:
    try:
        with open(file_path) as file:
            reader = csv.reader(file)
            data = list(reader)
            if not data:
                raise ValueError("Файл пустой")
            return data
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")


def pars_xlsx(file_path: str) -> pd.DataFrame:
    try:
        reader = pd.read_excel(file_path)
        if reader.empty:
            raise ValueError("Файл пустой")
        return reader.head()
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")


# print(pars_csv('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions.csv'))
# print(pars_xlsx('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions_excel.xlsx'))