
import os
import numpy as np
import cv2
import glob
import time


"""
    frame_bgr: 图片源路径 例: D:\\app\\algo_pic\\20231130_180931.jpg
    video_path: 输出视频文件存储路径 例: D:\\app\\algo_pic\\video\\test2.mp4
    video_length:  视频长度 秒/s * 帧数
    fps: 帧数
"""
def frame2video(frame_bgr, video_path, video_length, fps=25):
    # frames: list[bgr]
    frame_size = frame_bgr.shape[:2][::-1]
    """ 
        filename: 文件名
        fourcc: 视频的编码类型  ('M', 'P', '4', '2')  ('X','2','6','4') ('H','2','6','4')
        fps:  帧速率,比如录制视频每秒30帧,或者60帧等。
        frameSize:  帧的长宽(分辨率)
        isColor:  是否为彩色图像
    """
    vid_writer = cv2.VideoWriter(filename=video_path, fourcc=cv2.VideoWriter_fourcc('M', 'P', '4', '2'), fps=fps, frameSize=frame_size)
    start_time = time.time()
    for i in range(video_length):
        vid_writer.write(frame_bgr)
    vid_writer.release()
    print(f'Consume time: {time.time()-start_time}')


if __name__ == '__main__':
    # 图片存储路径
    img_root = r'D:\app\algo_pic'
    # 视频存储路径
    video_root = r'D:\app\algo_pic\video'
    # glob.glob 函数 获取目录下文件   enumerate()迭代器 ,包含数据和数据下标的序列
    for i, img_path in enumerate(glob.glob(os.path.join(img_root, '*jpg'))):
        """
            np.fromfile()  将文本或二进制文件中数据构造成数组,加载到内存
            cv2.imdecode() 图片解码   
        """
        img_bgr = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        # 定义视频文件名称
        video_path = os.path.join(video_root, f'{os.path.basename(img_path).split(".")[0]}.mp4')
        print(video_path)
        frame2video(img_bgr, video_path, 25*30)
