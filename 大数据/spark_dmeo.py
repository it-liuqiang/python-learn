'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-12-06 18:59:55
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-12-06 21:31:02
FilePath: \python-learn\大数据\spark_dmeo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pyspark import SparkConf,SparkContext
import pandas
import os

#设置环境变量
os.environ["PYSPARK_PYTHON"]="D:\ProgramData\Anaconda3\envs\whisper\pythonw.exe"

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

#基于SparlConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

#打印pyspark 运行版本
print(f'spark version is : {sc.version}')
# content = pandas.read_excel(r"D:\\home\\2023111616393032009.xls")

# # 读取字符串
# rdd = sc.parallelize("abcdefg")
# #读取数组
rdd = sc.parallelize([1,2,3,4,5])
# #读取元祖
# rdd = sc.parallelize((1,2,3,4,5))
# #读取set
# rdd = sc.parallelize({1,2,3,4,5})
# #读取字典
# rdd = sc.parallelize({"key1":"value1" , "key2":"value2"})


#读取文件
rdd = sc.textFile("C:\\unintall.log")
print(rdd.collect())


# def x10(data):
#     return data*10;

# map算子 通过map 方法处理一条条数据
# rdd = rdd.map(x10)
# rdd = rdd.map(lambda x: x * 10).map(lambda x: x+5)
# print(rdd.collect())

# # flatMap 算子 对数据解除嵌套操作（深层嵌套转单层）
# rdd2 = sc.parallelize(["a,b,c","d,eg"])
# rdd2 = rdd2.flatMap(lambda x: x.split(","))
# print(rdd2.collect())

# # reduceByKey算子 对二元元组 进行分组+聚合
# rdd3 = sc.parallelize([("a" , 1),("b" , 1),("c" , 2),("a" , 4),("a" , 1),("c" , 2)])
# rdd3 = rdd3.reduceByKey(lambda a,b: a+b)
# print(rdd3.collect())


#停止SparkContext对象的运行
sc.stop()

