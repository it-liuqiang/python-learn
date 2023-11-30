
import pymysql 

def open():
    """
    建立数据库连接
    :return: 数据数据
    """
    db = pymysql.connect(host="10.20.5.29", user="root", password="Cvsehl1234__", database="smart_inciden", charset="utf8",autocommit=True)
    return db


def query1(sql):
    """
    不带参数查询
    :param sql:
    :return:
    """
    db = open()
    cursor = db.cursor()  # 使用cursor（）方法获取游标
    cursor.execute(sql)  # 执行sql查询语句
    result = cursor.fetchall()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果

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
        sql2 = "select * from user_info"
        tuple = query1(sql2)
        print(tuple)
        all_user_info= []
        for index in range(len(tuple)):
            temp_dict = dict()
            temp_dict["userName"] = tuple[index][0]
            temp_dict["userPwd"] = tuple[index][1]
            all_user_info.append(temp_dict)
        print(all_user_info)
    except:
        print("数据读取错误！")






