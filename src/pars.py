import csv, pandas as pd
from typing import List, Union

def pars_csv(file_path: str) -> List[List[str]]:
    """
    Считывает данные из CSV-файла и возвращает их в виде списка строк.

    :param file_path: Путь к CSV-файлу.
    :return: Данные файла в формате списка списков.
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если файл пустой.
    """
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
    """
    Считывает данные из Excel-файла и возвращает первые 5 строк.

    :param file_path: Путь к Excel-файлу.
    :return: Данные файла в формате DataFrame (первые 5 строк).
    :raises FileNotFoundError: Если файл не найден или доступ к нему невозможен.
    :raises ValueError: Если файл пустой.
    """
    try:
        reader = pd.read_excel(file_path)
        if reader.empty:
            raise ValueError("Файл пустой")
        return reader.head()
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")


# print(pars_csv('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions.csv'))
# print(pars_xlsx('/home/babyblinkfeeldark/PycharmProjects/homework/data/transactions_excel.xlsx'))