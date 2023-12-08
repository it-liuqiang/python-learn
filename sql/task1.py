'''
    读取excel 转换为 DML （insert update） 语句
'''

import pymysql
from pojo.Student import *
from DBConfig import *
import pandas
from datetime import datetime



def open(host,port,username,password,database):
    db = pymysql.connect(host=host,port=port,user=username,password=password,database=database,autocommit=True)
    return db


    


if __name__ == '__main__':
    try:
        # dbConfig = DBConfig()
        # db = open(dbConfig.host,dbConfig.port,dbConfig.username,dbConfig.password,dbConfig.database)
        # cursor = db.cursor()
        # sql = "select * from t_server"
        # count = cursor.execute(sql);
        # result = cursor.fetchall()
        # print(result)
        # cursor.close
        # db.close
        # sql = "INSERT INTO `algoplatform`.`draw_task` (`task_id`, `operator_time`, `line_drawing`, `line_drawing_out`) VALUES (%s,%s,%s,%s)"
        sql = "update draw_task set  operator_time = '{:s}', line_drawing = '{:s}', line_drawing_out = '{:s}'  where task_id ='{:s}'";
        file = "D:\home\output_yantai.xlsx";
        df = pandas.read_excel(file);

        
        for line in df.values:
            print(sql.format(str(datetime.now()),line[2],line[2],line[0]))
            # print(line)

        
        
    except Exception as ex:
        print(ex)
    