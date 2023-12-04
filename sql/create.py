'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-11-29 16:05:12
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-12-04 20:46:46
FilePath: \python-learn\sql\create.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import pymysql
from pojo.Student import *
from DBConfig import *



def open(host,port,username,password,database):
    db = pymysql.connect(host=host,port=port,user=username,password=password,database=database,autocommit=True)
    return db


    


if __name__ == '__main__':
    try:
        dbConfig = DBConfig()
        db = open(dbConfig.host,dbConfig.port,dbConfig.username,dbConfig.password,dbConfig.database)
        cursor = db.cursor()
        sql = "select * from t_server"
        count = cursor.execute(sql);
        result = cursor.fetchall()
        print(result)
        cursor.close
        db.close
    except Exception as ex:
        print(ex)
    