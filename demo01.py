'''
Descripttion: 
version: 
Author: HuangJunren
Date: 2023-02-14 17:21:52
LastEditors: liuq_wb liuq_wb@ehualu.com
LastEditTime: 2023-02-16 11:31:26
'''
import math
from turtle import *
from TurtleWorld import *
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


square(bob())