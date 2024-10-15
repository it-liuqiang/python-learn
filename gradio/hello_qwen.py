from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis

# export DASHSCOPE_API_KEY="sk-3861114a97444b498b0f08741ec4dc45"

model = "flux-schnell"
prompt = "Eagle flying freely in the blue sky and white clouds"
prompt_cn = "水边吃草的牛"


def sample_block_call(input_prompt):
    rsp = ImageSynthesis.call(model=model,
                              prompt=input_prompt,
                              size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
        # save file to current directory
        for result in rsp.output.results:
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            with open('./%s' % file_name, 'wb+') as f:
                f.write(requests.get(result.url).content)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


def sample_async_call(input_prompt):
    rsp = ImageSynthesis.async_call(model=model,
                                    prompt=input_prompt,
                                    size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    status = ImageSynthesis.fetch(rsp)
    if status.status_code == HTTPStatus.OK:
        print(status.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (status.status_code, status.code, status.message))

    rsp = ImageSynthesis.wait(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    return rsp.output


if __name__ == '__main__':
    # sample_block_call(prompt)
    sample_async_call(prompt_cn)
