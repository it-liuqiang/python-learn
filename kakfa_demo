'''
Author: liuq liuq03@ehualu.com
Date: 2023-09-19 11:57:04
LastEditors: liuq liuq03@ehualu.com
LastEditTime: 2023-09-21 17:39:11
FilePath: \python-learn\kakfa_demo
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from kafka import KafkaProducer





# kafka server
server = "10.20.5.9:9092"
# kafka topic
topic_name = "my_topic"
# 消费组id
group_id = "test2"
# 消息体
message = "今天真美丽"

producer = KafkaProducer(bootstrap_servers=[server])
record = {"title": "今天真美丽", "url": "http://123123.jewr.com"}
future = producer.send(topic_name,  value=bytes(f'{record}', encoding='utf-8'), partition=0)
result = future.get(timeout=10)
print(result)




