from yaml1.readyaml import read_yaml
from csv1.readcsv import read_csv
from excal1.readexcal import read_excal
from json1.readjson import read_json

def pri():
     dir1 = read_yaml('UI.yaml')
     for dict_yaml in dir1:
          print(dir1[dict_yaml]['username'])
          print(dir1[dict_yaml]['password'])
          print(dir1[dict_yaml]['result'])

     dir2 = read_csv('data.csv')
     for dict_csv in dir2:
          print(dict_csv['username'])
          print(dict_csv['password'])
          print(dict_csv['result'])

     dir3 = read_excal('data.xlsx')
     # for i in range(0,3):
     #      for dict_xls in dir3:
     #           print(dict_xls[i])
     for dict_xls in dir3:
          for i in range(0,3):
               print(dict_xls[i])

     dir4 = read_json('UI.json')
     for dict_json in dir4:
          print(dir4[dict_json]['username'])
          print(dir4[dict_json]['password'])
          print(dir4[dict_json]['result'])

pri()