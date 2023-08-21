import random
import time

name='ehl'
stock_price=19.99
stock_code="300212"
stock_price_daily_growth_fator=1.2

#计算经过growth_day天的增长后，股价达到了多少钱



def countPrice(growth_day):
    print(f"公司：{name} 股票代码：{stock_code} 当前股价：{stock_price}")
    price = stock_price*stock_price_daily_growth_fator**growth_day
    print("每日增长系数：%0.1f，经过%d天的增长后，股价达到了：%0.2f"%(stock_price_daily_growth_fator,growth_day,price))

countPrice(7)



#定义一个数字1 ——10 ，随机产生，通过3次判断来猜出数字。
# num = random.randint(1,10)
# flag = True
# while flag:
#     u_num = int(input("你猜啊？   "))
#     if u_num == num:
#         print("猜对咯！ 这个数字是：  %s" %u_num)
#         flag=False
#     elif u_num > num:
#         print("大了")
#     else:
#         print("小了")

# 通过while 循环，输出99乘法表格
i=1
while i <= 9:
    j= 1
    while j<=i:
        if j ==i:
            print("%s*%s=%s"%(j,i,i*j))
        else:
            print(f"{j}*{i}={i*j}\t",end="")
        j+=1
    i +=1
    print()
        
# for循环的冒泡排序 倒序
array = []
while len(array) < 10:
    array.append(random.randint(1,100))
print("%s"%array)
def int_sort(array):
    for i in range(1,len(array)):
         for j in range(0,len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
print(int_sort(array))

## 通过for 循环，输出99乘法表格
for i in range(1,10):
    for j in range(1,10):
        #打印口诀
        if j == i:
            print(f"{j}*{i}={i*j}")
            break
        else:
            print(f"{j}*{i}={i*j}",end="\t")
    #输出玩1列换行
    print()

# python 冒泡排序 
list = []
for x in range(1,10):
    list.append(random.randint(1,100))
print("%s"%list)
temp = 0
def f_sort(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)): 
            if list[j]<list[i]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    return list;
print("%s" %f_sort(list))

# 统计某个文件中单词出现的数量
def countDict(file_name ,key_words):
    file = open(file=file_name , mode= 'r' , encoding= 'UTF-8')
    file_content = file.read(); 
    return file_content.count(key_words)
    
file_name = '/home/kali/Downloads/del.sql'
key_words= 'kubectl'
print(countDict(file_name, key_words))

# 备份账单并删除测试数据

def write(file_name , content):
    """_summary_

    Args:
        file_name (_type_): _description_ 文件路径
        content (_type_): _description_ 文件内容
    """
    with open(file_name ,mode="w",encoding="UTF-8") as file:
        file.writelines(content)
content = []

for i in range(1 , 10):
    content.append(str(i) +"\t")
    content.append("jerry\t")
    # time.sleep(1)
    content.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\t")
    if i%2 == 0:
        content.append("测试\n")
    else:
        content.append("正式\n")


file_name2 = '/home/kali/Downloads/bill.text'
write(file_name2,content)

def delete_content(file_name2, key_words):
    newContent = []
    with open(file_name2, mode="r",encoding="UTF-8") as file:
        content = file.readlines()
        for line in content:
            if line.count(key_words) != 1:
                newContent.append(line)
    print(f"{newContent}")

    with open(file_name2, mode="w",encoding="UTF-8") as newF:
        newF.writelines(newContent)

key_words = "测试"
delete_content(file_name2,key_words)