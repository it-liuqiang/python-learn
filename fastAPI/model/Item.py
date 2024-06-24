
from pydantic import BaseModel   
# 声明请求体数据模型为一个类，且该类继承 BaseModel。所有的属性都用标准Python类
from fastapi import Query 


class Item(BaseModel):
    name: str = Query(None,max_length=10,min_length=3)
    price: float = Query(...,gt=1,lt=10,description="价格超出范围")
    # 可以不传递默认值或者是可选值
    is_offer: bool = None
    