import openai

# 填你的秘钥
openai.api_key = "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"

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



response = openai.Image.create(
  prompt="搞笑",
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']

print(image_url)