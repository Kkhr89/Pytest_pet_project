import json


def parse_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
