import redis
import datetime

redis_host = '10.20.5.9'
redis_port = 7001


redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)


# 连接redis     

# reids 示例
def redis_demo():
    r = redis_client
    r.set('name', 'zhangsan')
    print(r.get('name'))

    # bitmap 适合存储大量的二进制数据
    # 指令 SETBIT key offset value
    # 返回值：指定偏移量原来储存的位
    r.setbit('A', 1, 1)
    r.setbit('A', 2, 1)
    r.setbit('A', 3, 1)

    print(r.getbit('A', 1))
    print(r.getbit('A', 2))
    print(r.getbit('A', 3))

    print(r.bitcount('A'))  




# 场景一 ：用户签到，记录签到时间
def sign_demo1(uid=1001,start_date='2024-08-01'):
    
    
    today_data = datetime.datetime.now().timestamp()
    start_time = datetime.datetime.strptime(start_date,'%Y-%m-%d').timestamp()

    offset = int((today_data - start_time)/86400)
    print(f'今天是第{offset}天')
    r = redis_client
    r.setbit(uid,offset,1)

# 订阅key过期事件
pubsub = redis_client.pubsub()
pubsub.subscribe('__keyevent@0__:expired')
 
print(f"Starting to listen for expired keys on db 0...")
for message in pubsub.listen():
    if message['type'] == 'message':
        expired_key = message['data']
        print(f"Key {expired_key} has expired.")

if __name__ == '__main__':
    # redis_demo()
    sign_demo1()
    