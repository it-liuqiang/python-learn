
import redis
import time


redis_host = '10.20.5.9'
redis_port = 7001

pool = redis.ConnectionPool(host=redis_host, port=redis_port, password=None, decode_responses=True)

redis_client = redis.StrictRedis(connection_pool=pool)


# 订阅key过期事件
pubsub = redis_client.pubsub()
pubsub.subscribe('__keyevent@0__:expired')
 
print(f"Starting to listen for expired keys on db 0...")
for message in pubsub.listen():
    if message['type'] == 'message':
        expired_key = message['data']
        print(f"Key {expired_key} has expired.")


if __name__ == '__main__':
    redis_client.setex("AAA",10,'{"name": "AAA", "price": 2.2}')
    redis_client.setex("bbb",10,'{"name": "bbb", "price": 2.2}')
    time.sleep(10)
    redis_client.setex("ccc",10,'{"name": "ccc", "price": 2.2}')
    time.sleep(20)