import json
import random
from pojo.Student import *

#创建一个对象

stu = Student("jerry" , 22,"天津市")
print(type(stu))

#class 转 json
print(json.dumps(stu.__dict__,ensure_ascii=False))
print(str(stu.__str__))
#成员方法
stu.say()
stu.say_2("我很牛")

#打印私有的成员方法和成员变量
# print(stu.__spec)
# print(stu.__play())

# for i in range(1,10):
#     print('当前录入第%d位学生信息'%i)
#     name = input("请输入学生姓名：")
#     age = input("请输入学生年龄：")
#     address = input("请输入学生地址：")
#     stu = Student(name,age,address)
#     print(f"学生{i}信息录入完毕 ，信息为[学生姓名：{stu.name} 学生年龄：{stu.age} 学生地址：{stu.address}]")



