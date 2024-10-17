import json


def parse_level(file: str):
    with open(file) as file:
        return json.load(file)
