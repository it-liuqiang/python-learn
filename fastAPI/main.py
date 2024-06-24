from fastapi import FastAPI,Query
from fastAPI.model.Request import Request
import uvicorn


 # 创建一个app实例
app = FastAPI()

@app.get("/")   # 编写一个路径操作装饰器
async def init(): 
    return {"code": 200 , "data": None ,"msg": "响应成功"}

# 所有的数据验证都是由 Pydantic实现的.
# 你可以用同样的类型声明比如 str, float, bool 或者其他更复杂的类型.
# 声明路径参数的类型
@app.get("/demo1/{id}")
async def getItems(id:int):
    return {"code": 200 , "data": id ,"msg": "响应成功"}

@app.get("/demo2/{id}/{name}")
async def getItems(id:int, name:str):
    return {"code": 200 , "data": {"id": id, "name": name} ,"msg": "响应成功"}


# 限定路径参数有效值 返回固定参数
@app.get("/demo3/{request}")
def getItems(request: Request):
    return {"code": 200 , "data":  request.email,"msg": "响应成功"}


# 限定路径为变量    参数的名字是 file_path，:path说明参数file_path对应的类型是 path 类型    使用Path转换器就可以进行转换
@app.get('/demo4/{file_path:path}/{item_id}')
def getItems(file_path , item_id):
    return {"code": 200 , "data": {"file_path": file_path, "item_id": item_id} ,"msg": "响应成功"}  


# 默认表单类型
# 声明不属于路径参数的其他函数参数时，它们将自动解释为“Query”参数    http://127.0.0.1:8080/demo5?param1=16&param2=jerry
# 访问默认值需要 /{path}/
@app.get('/demo5/')
def getItems(param1: int=1,param2: str="hello"):
    return {"code": 200 , "data": {"param1": param1, "param2": param2} ,"msg": "响应成功"}  
    
    
    
# 参数校验
@app.get("/demo6")
def getItem(q:str = Query(None,min_length=3)):
    results = {"items": 'Big preoject'}
    print(type(results))
    if q:
        results.update({"q": q})

    return {"code": 200 , "data": results ,"msg": "响应成功"}  
 
@app.get("/demo7")
def getItem(q:str = Query("hello world",min_length=3,title="Query string",description="sha")):
    results = {"items": 'Big preoject'}
    print(type(results))
    if q:
        results.update({"q": q})

    return {"code": 200 , "data": results ,"msg": "响应成功"}  
    


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8080)

