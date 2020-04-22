import json
from attrdict import AttrDict
import os

def init():
    print("config initialization")

connection_string = r'DRIVER={SQL Server};SERVER=DESKTOP-BBG3ONK\SQLEXPRESS;DATABASE=TestData;Trusted_Connection=yes'

def read_reference(filename):
    with open(filename) as f:
        data = json.load(f)
    return AttrDict(data)


ref_data = [read_reference(f'./config/serverconfig/{filename}') for filename in os.listdir('./config/serverconfig') if '.server.json' in filename]
references = AttrDict({x.reference:x for x in ref_data})



