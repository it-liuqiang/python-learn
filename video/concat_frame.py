
import os
import numpy as np
import cv2
import glob
import time
from util.common_util import *

class concat_frame:
    
 
    def frame2video(frame_bgr, video_path, video_length, fps=25):
        # frames: list[bgr]
        frame_size = frame_bgr.shape[:2][::-1]
        vid_writer = cv2.VideoWriter(filename=video_path, fourcc=cv2.VideoWriter_fourcc('M', 'P', '4', '2'), fps=fps, frameSize=frame_size)
        start_time = time.time()
        for i in range(video_length):
            vid_writer.write(frame_bgr)
        vid_writer.release()
        print('视频转换耗时： %0.2f %s' %(time.time()-start_time ,' #秒'))




    if __name__ == '__main__':
        # 图片存储路径
        img_root = r'D:\app\algo_pic'
        # 视频存储路径
        video_root = r'D:\app\algo_pic\video'
        # glob.glob 函数 获取目录下文件   enumerate()迭代器 ,包含数据和数据下标的序列
        for i, img_path in enumerate(glob.glob(os.path.join(img_root, '*jpg'))):
            img_bgr = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            # 定义视频文件名称
            video_path = os.path.join(video_root, f'{os.path.basename(img_path).split(".")[0]}.mp4')
            print(video_path)
            frame2video(img_bgr, video_path, 25*30)
            # 上传服务器
            tar_file = str("/data/volume/ry/video/"+os.path.basename(video_path))
            print(tar_file)
            # common_util().upload_video_file(source_file=video_path ,tar_file=tar_file)
            # 添加sql
            common_util().insert_sql(video_path=video_path)

