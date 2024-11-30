from typing import Any, Dict, List


def filter_by_state(in_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param in_dicts: Список словарей, которые необходимо отфильтровать.
    :param state: Значение ключа 'state', по которому будет производиться фильтрация.
                  По умолчанию 'EXECUTED'.
    :return: Новый список словарей, содержащий только те словари,
             у которых значение ключа 'state' соответствует указанному значению.
    """
    out_dicts = []
    for d in in_dicts:
        if d.get("state") == state:
            out_dicts.append(d)
    return out_dicts


def sort_by_date(in_dicts: List[Dict[str, Any]], sort_by: str = "ASC") -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по значению ключа 'date'.

    :param in_dicts: Список словарей, который необходимо отсортировать.
    :param sort_by: Порядок сортировки. Может быть 'ASC' для сортировки по возрастанию
                    или 'DESC' для сортировки по убыванию. По умолчанию 'ASC'.
    :return: Новый список словарей, отсортированный по дате (ключ 'date')
             в указанном порядке.
    """
    return sorted(in_dicts, key=lambda x: x["date"], reverse=(sort_by == "DESC"))

dat = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(dat))