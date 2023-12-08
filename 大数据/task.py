from pyspark import SparkConf,SparkContext
import pandas
import os

#设置环境变量
os.environ["PYSPARK_PYTHON"]="D:\ProgramData\Anaconda3\envs\whisper\pythonw.exe"

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

#基于SparlConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)


rdd = sc.textFile("C:\\unintall.log")
print(rdd.collect())

#读取所有单词


#将所有单词都加上todo 作为value


#分组求和


#打印输出结果


