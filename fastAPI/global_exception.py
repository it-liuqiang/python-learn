
#coding:utf-8
#error
from flask import Flask,jsonify

app = Flask(__name__)
# 全局异常处理中间件
@app.exception_handler(Exception)
async def http_exception_handler(exc: Exception):
    print(f"全局异常处理中间件: {exc.message}")

    return exc.message
    

