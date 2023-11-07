'''
Author: liuq liuq03@ehualu.com
Date: 2023-11-07 21:18:00
LastEditors: liuq liuq03@ehualu.com
LastEditTime: 2023-11-07 21:20:06
FilePath: \python-learn\sql\insert.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pymysql

def open():
    """
    建立数据库连接
    :return: 数据数据
    """
    db = pymysql.connect(host="192.168.40.128", user="root", password="root123", database="student_db", charset="utf8",autocommit=True)
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
    db.commit()
    cursor.close()
    db.close()
    return cursor.rowcount



if __name__ == "__main__":
    try:
        sql = "select * from user_info where userName=%s and userPwd=%s"
        val = ("bob", "bob")
        tuple = query(sql)
        print(tuple)
        for index in range(len(tuple)):
            temp_dict = dict()
            temp_dict["userName"] = tuple[index][0]
            temp_dict["userPwd"] = tuple[index][1]
            all_user_info.append(temp_dict)
        print(all_user_info)
    except:
        print("数据读取错误！")


if __name__ == "__main__":
    try:
        sql1 = "insert into user_info (userName,userPwd) values (%s,%s)"
        val = [("bob", "bob"),("tom", "tom")]
        print(insert(sql,val),"条数据添加成功")
    except:
        print("数据操作错误！")
