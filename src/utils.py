import json

def parser(file_path):
    with open(file_path, 'r') as f:
        return list(json.load(f))
