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



"""
    组装sql文件

    video_folder: 视频文件源文件
"""
def insert_sql(video_path):


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
    
    sql = 'INSERT INTO t_video_file_upload (device_id, name, md5, path, upload_time) values (%s,%s,%s,%s,%s)'
    # values = [('device_id',device_id),('name',name),('md5',md5),('path',path)]

    # sql = "select * from t_server";
    db = pymysql.connect(host='10.20.5.11',
                          port=3306, 
                          user='root', 
                          password='cwovEll__', 
                          database='ai_middle_station', 
                          charset="utf8",
                          autocommit=True)
    
    cursor = db.cursor()  #         
    cursor.execute(sql, (device_id,name,md5,path,time.localtime()))

    # cursor.execute(sql);
    # result = cursor.fetchone()
    # print(result)

    cursor.close()
    db.close()
    return cursor.rowcount



if __name__ == '__main__':
    #本地视频文件存储目录
    video_root = r'D:\app\algo_pic\video'
    for i, video_path in enumerate(glob.glob(os.path.join(video_root, '*.mp4'))):
        insert_sql(video_path=video_path)