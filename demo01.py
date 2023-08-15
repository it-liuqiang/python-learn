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

print("jerry的类型是： %s" %type(name))
#-------------------------------------------------------------------
