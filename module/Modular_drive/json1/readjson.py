import json
import os

def dir_name():
    return os.path.dirname(__file__)

def read_json(name):
    return json.load(open(os.path.join(dir_name(),name),encoding='utf-8'))

