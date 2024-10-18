import json


def parse_level(file: str):
    with open(file) as file:
        data = json.load(file)

        if len(data['map']) > 7:
            raise ValueError('level can have max 7 lines of bricks')

        for row in data['map']:
            if len(row) > 10:
                raise ValueError('row can have maximum 10 bricks')

        return data
