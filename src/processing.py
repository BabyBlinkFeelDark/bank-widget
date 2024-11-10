def filter_by_state(in_dicts: list, state="EXECUTED") -> list:
    out_dicts = []
    for d in in_dicts:
        if d.get("state") == state:
            out_dicts.append(d)
    return out_dicts


def sort_by_date(in_dicts: list, sort_by="ASC") -> list:
    return sorted(in_dicts, key=lambda x: x["date"], reverse=[True if sort_by == "DESC" else False])
