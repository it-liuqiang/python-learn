'''
Descripttion: 
version: 
Author: HuangJunren
Date: 2023-02-14 17:21:52
LastEditors: liuq liuq03@ehualu.com
LastEditTime: 2023-08-14 16:51:25
'''
import math
from turtle import *
import logging
import random
import requests
import time
import my_module
import json
degrees = 45
x= math.sin(degrees / 360.0 * 2 * math.pi)
print(1+x)


#def 定义一个函数
#import 导入外部依赖包
def print_lyrics():
    print(math.pi)
    print('hello world')


print(print_lyrics) 
print(print_lyrics())
print_lyrics()

print("---------------------------------------")
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

print("---------------------------------------")

#形参和实参
def print_twice(name , age , sex ,like, merit,dict):
    print(name)
    print(age)
    print(sex)
    print(like[0]) #数组
    print(merit[1]) #元数据
    print(dict['degree']) #元数据

like = ['读书', '学python','学java']
merit=('高','富','帅')
dict={"degree":"大学"}
print_twice("jerry",27,"男",like , merit, dict)
print("like的长度：%s "%len(like))

print("---------------------------------------")
def square(t):
    for i in range(4):
        fd(t, 10)
        lt(t)




def count(r):
    logging.info('半径为r的球体积是43πr3。半径为5的球体积是多少？')
    a = 4 /3 *3.14*(r**3)
    return a

print(count(5))

def buyBook(n):
    b = 24.95
    y = 3
    if n <= 1:
         y = 3
    else:
        y = 3+(n-1)*0.75

    total = (n*b)*0.4
    return total+y
print("购买60本书的价格为： %s" %buyBook(60) )

#----------------------------字符串的拼接--------------------------
name = 'jerry'
age = 27
sg = 168.57
#错误示范 无法并接非str类型
#print("打印： "+  name + age)

# %s 将内容转换为字符串，放入占位位置
# %d 将内容转换为整数，放入占位位置
# %f 将内容转换为浮点型，放入占位位置   *.m 控制长度（设置宽度小于自身不生效）  *.n 控制精度
print('名称：%10s 年龄：%2d 身高：%0.2f' %(name ,age , sg))

# f "{变量1}{变量2}"  快速格式化方法
print(f'名称：{name}  年龄：{age}  身高：{sg}')
#表达式的格式化
print("jerry的类型是： %s" %type(name))
#-------------------------------------------------------------------
# age = input("请输入你的年龄：")

# print("我是谁：%s" %age)
# if int(age) > 30:
#     print("你已经成年了！！")


# feshu = input("请输入你的分数，然后评等级")

# if int(feshu) <60:
#     print("及格")
# elif int(feshu) <90:
#     print("中等")
# elif int(feshu) < 100:
#     print("优秀")
# else:
#     print("垃圾")

# end=”“  不换行
print("不",end='')
print("换行")

# \t 多个字符串变量对齐 相当与tab
print("hello world")
print("hi    jerry")

print("hello\tworld")
print("hi\tjerry")

#-----------------------------------------------------------------------
#range 语法 1  
for x in range(10):
    print(x)

#range 语法 2 不含num2本身
for x in range(5,10):
    print(x)
#range 语法 3 不含num2本身 step代表间隔
for x in range(5,10,3):
    print(x)

num = random.randint(1,100)
count = 0
for x in range(1,num):
    if x%2 == 0:
        count+=1

print(f"从1-{num}（不含num）共计出现偶数{count}次")

#---------------------------------------------------------------
# 函数的注释
def bool(x,y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
#-----------------------------------------------------------------
# 数据容器
# 列表 list 可变数组 []
list = [1,2,3]
print(f"切片： {list[0:1]}") 
# 元组 tuple 只读数组 () 单个数据（元读,)否则就是str
t1 = ((1,2,3),(4,5,6))
print(f"类型是： {type(t1)}   取值6：{t1[1][2]}")
# 字符串 str  不可修改的数据容器
s1 = " hello world "
print(s1.replace('hello','hi')) #替换
print(f"{s1.split(' ')}") # 切割
print("%s"%{s1.strip()}) #去除前后空格
print(f"h出现的次数：{s1.count('l')}")
 
# 集合 set 不支持重复 {}  不支持下标索引访问
set1={1,2,3,3}
set2={1,2,3,34,5,6}
print(f"{set}")
print("%s" %set2.difference(set1))
print(f"{set1.union(set2)}")

#字典 {} json 

d1 = {
    name: 'jerry',
    age: 27
}
#----------------------------------------------------------------
# 函数的传惨 *age tuple 类型        **ages dict类型
def test1():
    print("方法1")

def test2(x,y):
    test1()

#-------------------------------------------------------------------
# 文件读取
# open(name,mode,encoding) 
# name 打开的文件名（包含路径）
# mode 打开文件的模式（访问模式） r 只读   w 写入  a 追加
# 编码格式 通常 TF-8
file_name = '/home/kali/Downloads/del.sql'
mode = 'r'
encoding = 'UTF-8'
f = open(file_name , mode=mode , encoding=encoding) 
# print(type(f))
# 读取文件 - read() 
# print(f.read())

# 读取文件readLines()  按行读取
# fs = f.readlines(); # 和read 命令冲突
# print(type(fs))
# print("文件内容： %s " %fs )

# 读取文件readLine()  按行读取
# print(f"第1行{f.readline()}")
# print(f"第2行{f.readline()}")

# 关闭文件
# time.sleep(3)
f.close

# whth open()  带自动close功能
with open(file_name , mode='r' , encoding='UTF-8')  as file:
    for f in file.readlines():
        print(f"{f}")

# write() 文件写入 
# flush() 刷新缓存 从内存刷新到硬盘
file_path = '/home/kali/Downloads/python.text' 
file = open(file=file_path, mode="w", encoding="UTF-8") #w模式文件自动创建
file.write("我爱学python！！！")
file.flush()
#time.sleep(10) # 休眠
file.close # 文件关闭会自动持久化到硬盘

# 追加写入

file_path = '/home/kali/Downloads/python.text' 
with open(file=file_path , mode="a" , encoding="UTF-8") as file:
    file.write("\n我爱学java！！！")

#-------------------------------------------------------------------------------

#异常处理
try:
    open("/homme/kali/demo.text",mode="r" , encoding="UTF-8")
except:
    print("error")
#捕获指定异常
try:
    1/0
except Exception as e:
    print(e)
finally:
    print("结束")


#---------------------------------------------------------------------------------
#模块的导入
print(f"当前时间： {my_module.str_time(time.localtime())}")

#main 函数的使用  if __name__ == '__main__':

# 科学计算 numpy包
# 数据分析 pandas包
# 打数据计算 pyspark ， apache-flink包
# 图形可视化 matplotlib ， pyecharts
# 人工智能 tensorflow

#---------------------------------------------------------------------------------\
#json数据格式

#列表转json
data = [{"name":"jery","age":17 },{"name":"tom","age":18},{"name":"乔丹","age":18}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)
#字典转json
dict = {'name':'科比','age':15,'address':"阿拉斯加"}
json_str = json.dumps(dict,ensure_ascii=False)
print(json_str)

#json转列表list
str_json_array = '[{"name": "jery", "age": 17}, {"name": "tom", "age": 18}, {"name": "乔丹", "age": 18}]'
list = json.loads(str_json_array)
print(type(list))
print(list)
#json转字典dict
str_json = '{"name": "科比", "age": 15, "address": "阿拉斯加"}'
dict = json.loads(str_json)
print(type(dict))
print(dict)