import paramiko
import traceback
import configparser
import time
import os
import cv2
import glob
import pymysql
from toollib.guid import SnowFlake
import hashlib
import json
from datetime import datetime



class common_util:

    """
        图片转视频

        frame_bgr: 图片源路径 例: D:\\app\\algo_pic\\20231130_180931.jpg
        video_path: 输出视频文件存储路径 例: D:\\app\\algo_pic\\video\\test2.mp4
        video_length:  视频长度 (秒/s * 帧数)
        fps: 帧数
    """
    def frame2video(frame_bgr, video_path, video_length, fps=25):
        # frames: list[bgr]
        frame_size = frame_bgr.shape[:2][::-1]
        """ 
            filename: 文件名
            fourcc: 视频的编码类型  ('M', 'P', '4', '2')  ('X','2','6','4') ('H','2','6','4')
            fps:  帧速率
            frameSize:  帧的长宽(分辨率)
            isColor:  是否为彩色图像
        """
        vid_writer = cv2.VideoWriter(filename=video_path, fourcc=cv2.VideoWriter_fourcc('M', 'P', '4', '2'), fps=fps, frameSize=frame_size)
        start_time = time.time()
        for i in range(video_length):
            vid_writer.write(frame_bgr)
        vid_writer.release()
        print('视频转换耗时： %0.2f %s' %(time.time()-start_time ,' #秒'))


    """
        上传文件到服务器

        source_file: 源文件
        tar_folder: 服务器目录
    """
    def upload_video_file(self, source_file , tar_file):
        try:
            start_time = time.time()
            ssh_client=paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=self.server_host, port=self.server_port, username=self.server_username, password=self.server_password)

            # 使用SFTP传输文件
            sftp = ssh_client.open_sftp()
            sftp.put(source_file, tar_file)  
            print('上传服务器成功， 耗时： %0.2f %s' %(time.time()-start_time ,'#秒'))

        except Exception as ex:
            # traceback.print_exc()
            print("上传服务器失败 ",str(ex))
        finally:
            sftp.close()
            ssh_client.close() 


    """
        组装sql文件

        video_folder: 视频文件源文件
    """
    def build_data(video_root):
        values = []
        for i, video_path in enumerate(glob.glob(os.path.join(video_root, '*.mp4'))):

            name = os.path.basename(video_path)
            device_id= SnowFlake().gen_uid()

            if os.path.isfile(video_path):
                fp=open(video_path,'rb')
                contents=fp.read()
                fp.close()
                md5= hashlib.md5(contents).hexdigest()
            else:
                print('file not exists')
                md5= None
            path="/data/volume/ry/video/"+name;

            data = (device_id, name, md5, path, datetime.now())
            values.append(data)
        print(f'参数：{json.dumps(values,default=str,ensure_ascii=False)}')

        return values

    if __name__ == '__main__':
        #本地视频文件存储目录
        video_root = r'D:\app\algo_pic\video'
   
        db = pymysql.connect(host="10.20.5.11",
                            port=3306, 
                            user="root", 
                            password="cwovEll__", 
                            database="ai_middle_station", 
                            charset="utf8",
                            autocommit=True)
        
        values = build_data(video_root=video_root)
        sql = 'INSERT INTO t_video_file_upload (device_id, name, md5, path, upload_time) values (%s,%s,%s,%s,%s)'
        
        cursor = db.cursor()          
        cursor.executemany(sql,values)

        cursor.close()
        db.close()
