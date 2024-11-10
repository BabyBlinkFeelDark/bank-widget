def filter_by_state(in_dicts: list, state = "EXECUTED") -> list:
    out_dicts = []
    for d in in_dicts:
        if d.get("state") == state:
            out_dicts.append(d)
    return out_dicts

def sort_by_date(in_dicts: list, sort_by = 'ASC') -> list:
    print(f"""
origin:
    {in_dicts}
    
    
sorted:
    {sorted(in_dicts, key=lambda x: x["date"])}
    
    """)
# 'date': '2018-06-30T02:08:58.425572'
# 'date': '2018-09-12T21:27:25.241689'
# 'date': '2018-10-14T08:21:33.419441'
# 'date': '2019-07-03T18:35:29.512364'}]


    for d in in_dicts:
        print(d.get("date"))


dat = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419442'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(filter_by_state(dat))
print(f"""

{dat}

""")
sort_by_date(dat)

