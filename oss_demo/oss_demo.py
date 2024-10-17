
from util import oss_uitils 
from util.oss_uitils import bucket



if __name__ == '__main__':
    # redis_demo()
    oss = oss_uitils.oss(bucket)
    data = "/home/kali/Pictures/jk.jpeg"
    file_url = oss.upload_file(bucket,'back/jk.jpeg',data)
    print(file_url)

    is_success = oss.del_file(bucket,["xusong.jpeg"])
    print(is_success)
