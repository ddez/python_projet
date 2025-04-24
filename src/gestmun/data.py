import json

DATAPATH = 'assets/data.json'

def get_data():
    with open(DATAPATH, 'r') as f:
        data = json.load(f)
    return data

