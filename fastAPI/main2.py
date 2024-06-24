
from fastapi import FastAPI,Query,Body
from fastAPI.model.Item import Item
import uvicorn

app = FastAPI()


# resutful风格json入参
@app.post("/getItem")   
def read_root(item: Item = Body(..., embed=True)):
    
    return {"code": 200 ,'data': item }

if __name__ == '__main__':
    uvicorn.run(app='main2:app', host="127.0.0.1", port=8081)


