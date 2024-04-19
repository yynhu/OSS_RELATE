#! /usr/bin/env/python
# -*- coding=utf-8 -*-
"""
======================模块功能描述=========================    
       @File     : oss_upload.py
       @IDE      : PyCharm
       @Author   : 陈虎
       @Date     : 2024/4/19 上午9:12
       @Desc     : 
=========================================================   
"""
import oss2


def upload_picture(bucket, object_key, file_path):
    try:
        bucket.put_object_from_file(object_key, file_path)
        print(f"File {file_path} uploaded successfully.")
    except oss2.exceptions.RequestError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Permission error: {e}")


# 配置阿里云账号的Access Key ID和Access Key Secret
# auth = oss2.Auth('<your-access-key-id>', '<your-access-key-secret>')
auth = oss2.Auth('LTAI5tD5h2zjqy8KbuUq9h15', '1eDoL4LvssL18cBQra1gycUOJtyK4u')

# 创建OSS客户端
# bucket = oss2.Bucket(auth, '<your-endpoint>', '<your-bucket-name>')
bucket1 = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'bucket-cyn')

# 上传图片


# 使用示例
upload_picture(bucket1, 'photo_folder/text.jpg', r"C:\Users\kim\Pictures\ios共享\IMG_20221125_073624.JPG")