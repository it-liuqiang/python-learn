'''
Author: liuq liuq03@ehualu.com
Date: 2023-11-07 21:18:00
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-12-04 21:50:11
FilePath: \python-learn\sql\insert.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pymysql
import json
from pymysql import cursors


def open():
    """
    建立数据库连接
    :return: 数据数据
    """
    db = pymysql.connect(host="10.20.5.29", port=3326, user="root", password="Cvsehl1234__", database="test", charset="utf8",autocommit=True,cursorclass=cursors.DictCursor)
    return db

def query(sql, *keys):
    """
    带参数查询数据库数据
    :return:
    """
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql, keys)  # 执行查询sql 语句
    result = cursor.fetchall()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果


def insert(sql, values):
    """
    向数据库插入数据,插入的values是一个tuple
    :param sql: 运行sql插入语句
    :return: 返回插入结果
    """
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor（）方法获取游标
    cursor.executemany(sql, values)
    # db.commit()
    cursor.close()
    db.close()
    return cursor.rowcount

def create(database, sql):
    db = open()
    #选择数据库
    db.select_db(database)
    cur = db.cursor()
    #执行sql
    cur.execute(sql)
    db.close()
    cur.close()
    



if __name__ == "__main__":
    try:
        # sql = "create table user_info(id int NOT NULL AUTO_INCREMENT, name varchar(255) , age int, gender varchar(2), PRIMARY KEY (id) USING BTREE) COMMENT='用户表'";
        # sql = "drop table user_info"
        # create(database="test",sql=sql)

        # sql = "insert into user_info (name,age,gender) value(%s,%s,%s)"
        # values = [("东方月初",31,"男"),("涂山雅雅",29,"女")]
        # insert(sql , values)

        sql = "select id,name,age,gender from user_info "
        result = query(sql)
        print(f"{json.dumps(result,ensure_ascii=False)}")
        # print(result, '\n', type(result[0]))


    except Exception as ex:
        ex.with_traceback()
        print("数据操作错误！")
