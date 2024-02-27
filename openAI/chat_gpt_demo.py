'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-08-28 11:38:19
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-27 17:00:00
FilePath: \python-learn\openAI\chat_gpt_demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%A
'''
from openai import OpenAI

import os
os.environ["OPENAI_API_KEY"] = "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"



# # 提问代码
# def chat_gpt(prompt):
#     # 你的问题
#     prompt = prompt
    
#     # 调用 ChatGPT 接口
#     model_engine = "text-davinci-003"
#     completion = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     response = completion.choices[0].text
#     print(response)

# print(chat_gpt("冒泡排序"))



client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url


print(image_url)