# -*- coding: utf-8 -*-
import hashlib
import os
import requests

from util import doubanutil
from config import filepath


def save_pic_to_disk(pic_url):
    # 将链接中的图片保存到本地，并返回文件名

    try:
        if not os.path.exists(filepath.image_path):
            os.mkdir(filepath.image_path)
        res = requests.get(pic_url)
        if res.status_code == 200:
            # 求取图片的md5值，作为文件名，以防存储重复的图片
            md5_obj = hashlib.md5()
            md5_obj.update(res.content)
            md5_code = md5_obj.hexdigest()
            file_name = filepath.image_path + str(md5_code) + ".jpg"
            # 如果图片不存在，则保存
            if not os.path.exists(file_name):
                with open(file_name, "wb") as f:
                    f.write(res.content)
            return file_name
        else:
            doubanutil.logger.warning("in func save_pic_to_disk(), fail to save pic. pic_url: " + pic_url +
                                      ", res.status_code: " + res.status_code)
            return ""
    except Exception as e:
        doubanutil.logger.error(e.message)
