from typing import Any, List, Dict


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
