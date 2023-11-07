import json
from pprint import pprint

from configparser import ConfigParser
import os

import yaml
# 读取json 格式配置文件（无法写备注）
def read_json_file(file):
    with open(file) as config:
        cfg = json.load(config)
    return cfg



# 读取ini 格式配置文件
def read_ini_file(file):
   
    cfg = ConfigParser()
    cfg.read(file,encoding='utf-8') 
    cfg.items("localdb")
    print(cfg)
    print(cfg.get('localdb','host'))
    return cfg


# 读取yml 格式配置文件
def read_yml_file(file):
    with open(file) as config:
        cfg = yaml.safe_load(config)
    print(cfg)
    return cfg

if __name__ == "__main__":
    print(os.path.abspath('./config/config.ini'))
    read_ini_file(os.path.abspath('./config/config.ini'))