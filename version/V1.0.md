# DoubanAuto V1.0
Automatic Robot for Douban 

## 功能介绍

- [加入小组](./group/join.py)
- [在已加入小组发帖](./group/post.py)
- [在已加入小组回帖](./group/comment.py)
- [识别验证码](./verifycode/wordrecognition.py)

## 调用示例

- [自动加入小组](./group/autojoin.py)
    - 演示加入豆瓣活跃小组（成员超过10000人），其中用到的活跃小组id文件（[active_group_id.txt](http://download.csdn.net/download/doleria/10143962)）此处未提供；
- [自动在已加入小组发帖](./group/autopost.py)
    - 演示需要验证码才能发帖的调用方式
- [自动在已加入小组回帖](./group/autocomment.py)
    - 演示在已加入小组回帖（未考虑验证码识别）
    - 需要验证码的版本，请参考[自动在已加入小组发帖](./group/autopost.py)的调用方式
    
## 其他

- 验证码识别模块调用百度AI平台提供的接口，具体见：[百度OCR技术文档](https://cloud.baidu.com/doc/OCR/index.html)   
- [auig_name_id.txt](./data/auig_name_id.txt)为豆瓣小组的名称与id映射文件，因为部分小组有个性域名，统一为id
- 更多信息请见[CSDN博客文章](http://blog.csdn.net/doleria/article/details/78707982)

## 交流建议
- 欢迎批评指正，提出意见：liu_yuning@foxmail.com 
