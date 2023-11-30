'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-11-29 17:07:55
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-11-29 18:00:54
FilePath: \python-learn\sql\db_config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE:
'''

from configparser import ConfigParser
import os

class DBConfig:

    host: None
    port: 3306
    username: None
    password: None
    database: None

    

    def __init__(self):
        # 初始化配置文件
        cfg = ConfigParser()
        cfg.read(os.path.abspath('./config/config.ini'),encoding='utf-8') 
        # 赋值
        self.host = cfg.get('localdb','host')
        self.port = cfg.getint('localdb','port') 
        self.username = cfg.get('localdb','user') 
        self.password = cfg.get('localdb','password') 
        self.database = cfg.get('localdb','database') 
        
        
        

