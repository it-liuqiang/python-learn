'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-08-24 16:01:12
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-12-07 22:55:43
FilePath: \python-learn\crawler\excel_crawler_requests.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# file_name: excel_crawler_requests.py
import requests
import pandas as pd


def get(url):
    	
    # 发起请求
	res = requests.get(url=url)

	# 获取响应数据
	text = res.text
	# 持久化数据到文件
	with open('./crawler/gjtjj.html','w',encoding=res.encoding) as fp:
		fp.write(text)
	
	# print(text)	
def input(url,keyword):
    #搜索参数
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
	params = {"qt":keyword}
	res = requests.get(url=url,params=params,headers=headers)
	print(res.url)
	# 获取响应数据
	text = res.text
	# 持久化数据到文件
	with open('./crawler/gjtjj2.html','w',encoding=res.encoding) as fp:
		fp.write(text)

if __name__ == '__main__':
    # 定义请求url
	url= "https://www.stats.gov.cn/search/s?"
	# 获取响应数据
	get(url)

	keyword = '2023'
	input(url=url,keyword=keyword)



	
	
