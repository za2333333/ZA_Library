import os
import yaml

def base_dir():
    return os.path.dirname(__file__)

def read_yaml(dir_name):
    with open(os.path.join(base_dir(),dir_name),encoding='utf-8') as f:
        value = yaml.safe_load(f)
        # value = yaml.load(stream=f,Loader=yaml.FullLoader)
        # value = yaml.load(f,Loader=yaml.FullLoader)
        # print('/n')
        # print(value['loginError']['username'],type(value))
        # print('/n')
        return value

# if __name__ == '__main__':
#     a = read_yaml('UI.yaml')
#     print(type(a))