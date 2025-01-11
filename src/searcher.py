import re,collections
from typing import List, Dict

def search_for_str(data: List[Dict], target: str):
    trans = re.findall(target,data)
