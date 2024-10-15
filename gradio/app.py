import gradio as gr
import hello_qwen as hq
import json


# export DASHSCOPE_API_KEY="sk-3861114a97444b498b0f08741ec4dc45" 


def greet(name):
    rsp_output = hq.sample_async_call(name);
    # rsp_output = {"task_id": "be78ca4d-2a58-494b-8d5e-3b60d3a6b15f", "task_status": "SUCCEEDED", "results": [{"url": "https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/1d/cb/20241009/12ebb447/29b03009-1823-4d0e-b7dc-ecf410ca173a-1.png?Expires=1728550415&OSSAccessKeyId=LTAI5tQZd8AEcZX6KZV4G8qL&Signature=BpJFC2cyJGfEb9DPwc6WbCyLg7w%3D"}], "submit_time": "2024-10-09 16:53:06.443", "scheduled_time": "2024-10-09 16:53:06.464", "end_time": "2024-10-09 16:53:35.853", "task_metrics": {"TOTAL": 1, "SUCCEEDED": 1, "FAILED": 0}}
    # rsp_json = json.loads(rsp_output);
    return rsp_output['results'][0]['url'];

demo = gr.Interface(fn=greet, inputs="text", outputs="image")
demo.launch()   