'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-11-18 15:52:17
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-11-29 15:53:15
FilePath: \python-learn\video\demo22.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import whisper




whisper_model = whisper.load_model("large")

result = whisper_model.transcribe(r"d:\\python\\a.mp3")

print(", ".join([i["text"] for i in result["segments"] if i is not None]))