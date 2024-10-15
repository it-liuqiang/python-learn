
from fastapi import FastAPI,Query,Body
from fastAPI.model.Item import Item
import uvicorn
from cachetools import TTLCache

app = FastAPI()



cache = TTLCache(maxsize=128, ttl=10)



# resutful风格json入参
@app.post("/saveItem")   
def read_root(item: Item):
    print(f"{item}")
    print(f"{item.name}")
    print(f"{item.price}")
    
    cache[item.name] = item
    print(f"{cache.keys()}")
    
    return {"code": 200 ,'data': item }


@app.get("/getItem/{name}")
async def getItem(name:str):
    price = cache.get(name);
    return {"code": 200 , "data": price ,"msg": "响应成功"}

if __name__ == '__main__':
    uvicorn.run(app='main2:app', host="127.0.0.1", port=8081)


