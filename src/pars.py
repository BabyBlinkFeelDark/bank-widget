import csv, pandas as pd
from typing import List, Dict

def pars_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает данные из CSV-файла и возвращает их в виде списка словарей.
    Первая строка файла используется как ключи для словарей.

    :param file_path: Путь к CSV-файлу.
    :return: Данные файла в формате списка словарей.
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если файл пустой или первая строка отсутствует.
    """
    try:
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            data = list(reader)
            if not data:
                raise ValueError("Файл пустой или не содержит данных")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except Exception as e:
        raise RuntimeError(f"Ошибка при обработке файла: {e}")


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
        return reader.to_dict(orient='records')
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")

