import json, os
from src.external_api import convert
from dotenv import load_dotenv

def parser(file_path):
    with open(file_path, 'r') as f:
        return list(json.load(f))

def transactions_summary(transaction):
    if transaction.get("code")!='RUB':
        load_dotenv()
        rez = convert(transaction.get("operationAmount", {}).get("currency", {}).get("code", {}), transaction.get("operationAmount", {}).get("amount", {}), os.getenv("API_TOKEN"))
    else:
        rez = float(transaction.get("operationAmount", {}).get("currency", {}).get("amount", {}))
    return rez


