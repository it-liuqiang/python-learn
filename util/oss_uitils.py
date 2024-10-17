import oss2
import configparser
import sys

sys.argv
config = configparser.ConfigParser()
config.read('config/config.ini')
# expires = config['OSS']['EXPIRES']
bucket=config['OSS']['BUCKER_NAME']

auth=oss2.Auth(config['OSS']['OSS_ACCESS_KEY_ID'], config['OSS']['OSS_ACCESS_KEY_SECRET'])


class oss(object):
    # 阿里云对象存储
    def __init__(self,bucket):
        """
        功能：创建桶对像

        """
        self.auth = oss2.Auth(config['OSS']['OSS_ACCESS_KEY_ID'], config['OSS']['OSS_ACCESS_KEY_SECRET'])
        self.endpoint = config['OSS']['ENDPOINT']
        self.region = config['OSS']['REGION']
        self.bucket=bucket

        self.service=oss2.Service(self.auth,self.endpoint)
        try:
            self.bucket_object = oss2.Bucket(self.auth, self.endpoint, self.bucket, region=self.region)
        except Exception as e:
            print(e)
            pass

    def bucket_exists(self,bucket):
        """
        功能：判断桶是否已被自己创建
        ：param bucket:桶名
        return:存在则返回True，否则返回False及报错信息
        """

        try:
            self.bucket_object.get_bucket_info()
            return True
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return e.message
        except BaseException as e:
            print(e)
            return e

    def create_bucket(self,bucket):
        """
        功能：创建桶
        ：param bucket:桶名
        ：return:创建成功返回True，不成功返回错误信息
        """
        #自定义桶的参数
        bucketConfig = oss2.models.BucketCreateConfig(oss2.BUCKET_STORAGE_CLASS_STANDARD,
                                                      oss2.BUCKET_DATA_REDUNDANCY_TYPE_ZRS)

        try:
            #如果桶名已被自己创建过，则抛出错误，如果没有则尝试创建桶
            if self.bucket_exists(bucket)==True:
                raise Exception('%s already exists with yourself!' %(bucket))
            self.bucket_object.create_bucket(oss2.BUCKET_ACL_PUBLIC_READ, bucketConfig)
            print(f"%s is available and created."  %(bucket))
            return True
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e



    def list_bucket(self):
        """
        功能：列出所有桶
        return:成功则返回一个包含所有桶名的列表，失败则返回错误信息
        """
        bucket_list=[]
        try:
            for b in oss2.BucketIterator(self.service):
                bucket_list.append(b.name)
            return bucket_list
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e

    def get_bucket_stat(self,bucket):
        """
        功能：获取桶的存储状态
        # 获取Bucket的总存储量，单位为字节。
        print(result.storage_size_in_bytes)
        # 获取Bucket中总的Object数量。
        print(result.object_count)
        # 获取Bucket中已经初始化但还未完成（Complete）或者还未中止（Abort）的Multipart Upload数量。
        print(result.multi_part_upload_count)
        # 获取Bucket中Live Channel的数量。
        print(result.live_channel_count)
        # 此次调用获取到的存储信息的时间点，格式为时间戳，单位为秒。
        print(result.last_modified_time)
        # 获取标准存储类型Object的存储量，单位为字节。
        print(result.standard_storage)
        # 获取标准存储类型的Object数量。
        print(result.standard_object_count)
        # 获取低频存储类型Object的计费存储量，单位为字节。
        print(result.infrequent_access_storage)
        # 获取低频存储类型Object的实际存储量，单位为字节。
        print(result.infrequent_access_real_storage)
        # 获取低频存储类型的object数量。
        print(result.infrequent_access_object_count)
        # 获取归档存储类型Object的计费存储量，单位为字节。
        print(result.archive_storage)
        # 获取归档存储类型Object的实际存储量，单位为字节。
        print(result.archive_real_storage)
        # 获取归档存储类型的Object数量。
        print(result.archive_object_count)
        # 获取冷归档存储类型Object的计费存储量，单位为字节。
        print(result.cold_archive_storage)
        # 获取冷归档存储类型Object的实际存储量，单位为字节。
        print(result.cold_archive_real_storage)
        # 获取冷归档存储类型的Object数量。
        print(result.cold_archive_object_count)
        return:返回桶的存储状态
        """

        try:
            result = self.bucket_object.get_bucket_stat()
            return result
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return False,e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return False,e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return False,e

    def del_bucket(self,bucket):
        """
        功能：列出所有桶
        : param bucket:桶名称
        ：return:删除成功则返回True，删除失败则返回错误信息
        """

        try:
            # 删除Bucket。
            self.bucket_object.delete_bucket()
            return True
        except oss2.exceptions.BucketNotEmpty as e:
            print('bucket is not empty.')
            return e.message
        except oss2.exceptions.NoSuchBucket as e:
            print('bucket does not exist')
            return e.message

    def upload_file(self,bucket,key,data):
        """
        功能：上传本地文件到oss
        : param bucket:桶名称
        : param key:上传到OSS的文件名
        : param data:本地文件名
        ：return:删除成功则返回True，删除失败则返回错误信息
        """
        try:
            self.bucket_object.put_object_from_file(key,data,progress_callback=self.percentage)
            url = self.bucket_object.sign_url('GET', key,1800,slash_safe=True)
            return True,url
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return False,e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return False,e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return False,e

    def upload_object(self,bucket,key,data=''):
        """
        功能：上传文件对象到oss
        : param bucket:桶名称
        : param key:上传到OSS的文件名
        : param data:侍上付的内容（对象）,默认为空，为空时如果key的值以'/'结尾，则代表创建目录
        ：return:删除成功则返回True，删除失败则返回错误信息
        """
        try:
            self.bucket_object.put_object(key,data,progress_callback=self.percentage)
            # 获取文件的URL
            url = self.bucket_object.sign_url('GET', key, 3600, slash_safe=True)
            print(url)
            return True,url
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return False,e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return False,e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return False,e

    def percentage(self,consumed_bytes, total_bytes):
        # 进度条

        if total_bytes:
            rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
            print('\r{0}% '.format(rate), end='')
            sys.stdout.flush()

    def get_object(self,bucket,key,localFile):
        # 流式下载

        try:
            object_stream = self.bucket_object.get_object(key)
            with open(localFile,'wb') as fileObj:
                shutil.copyfileobj(object_stream,fileObj)
                return True
        except oss2.exceptions.ServerError as e:
            print('ServerError', e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError', e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e


    def get_object_file(self,bucket,key,localFile):
        """
        功能：流式下载
        : param bucket:桶名称
        : param key:OSS中的文件名
        : param data:本地文件名
        ：return:删除成功则返回True，删除失败则返回错误信息
        """

        try:
            self.bucket_object.get_object_to_file(key,localFile,progress_callback=self.percentage)
            return True
        except oss2.exceptions.ServerError as e:
            print('ServerError', e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError', e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e

    def file_exists(self,bucket,fileName):
        """
        功能：判断文件是否存在
        : param bucket:桶名称
        : param fileName:文件名
        ：return:删除成功则返回True，删除失败则返回错误信息
        """

        try:
            exists=self.bucket_object.object_exists(fileName)
            if exists:
                return True
            else:
                return False
        except oss2.exceptions.ServerError as e:
            print('ServerError', e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError', e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e

    def list_file(self,bucket,prefix='',delimiter=''):
        """
        功能：列出文件
        : param bucket:桶名称
        : param prefix:查询前缀，默认为空
        : param delimiter:目录分隔符，默认为空
        ：return:成功则返回一个包含所有文件名的列表，失败则返回错误信息
        """
        file_list=[]

        try:
            for b in oss2.ObjectIterator(self.bucket_object,prefix=prefix,delimiter=delimiter):
                file_list.append(b.key)
            return file_list
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e

    def get_dir_size(self,bucket,dirName=''):
        """
       功能：列出一个目录的大小
       : param bucket:桶名称
       : param dirName:目录名，默认为空，为空是指根目录。example:dirName='a/':根目录下的目录a
       ：return:成功则返回目录大小，失败则返回错误信息
       """

        length = 0
        try:

            for obj in oss2.ObjectIterator(self.bucket_object, prefix=dirName):
                length += obj.size
            size=int(length/1024/1024)
            return str(size)+'MB'
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e

    def del_file(self,bucket,keylist):
        """
        功能：删除文件或目录
        : param bucket:桶名称
        : param keylist:要删除的文件列表，example:['file1','file2']
        ：return:成功则返回目录大小，失败则返回错误信息
        """

        try:
            self.bucket_object.batch_delete_objects(keylist)
            return True
        except oss2.exceptions.ServerError as e:
            print('ServerError',e.message)
            return e.message
        except oss2.exceptions.ClientError as e:
            print('ClientError',e.message)
            return e.message
        except BaseException as e:
            # 其它异常
            print(e)
            return e
