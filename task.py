
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