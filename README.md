# DoubanAuto V1.1
Automatic Robot for Douban 

## 功能概览

- [加入小组](group/join.py)
- [退出小组](group/quit.py)
- [在已加入小组发帖](group/post.py)
- [删除已发帖子](group/remove.py)
- [在已加入小组回帖](group/comment.py)
- [识别验证码](verifycode/wordrecognition.py)

## 如何使用

- 替换config目录下的相关配置信息，包括：
    - [baiconfig.py](config/baiconfig.py)配置文件存放百度开发者账号相关信息，申请好账号后，在个人中心的控制台下可以找到；
    - [doubanCookies.txt](config/doubanCookies.txt)配置文件存放豆瓣登录的Cookie信息，获取方式可参考[CSDN博客文章](http://blog.csdn.net/doleria/article/details/78733899)；
    - [filepath.py](config/filepath.py)配置文件存放一些本地文件目录信息，按照文件提示进行替换；
- example目录下的代码仅是调用示例，具体可按个人需求进行修改替换；
    
## 调用示例

- [自动加入小组](example/autojoin.py)
    - 演示自动加入豆瓣小组；
- [自动退出小组](example/autoquit.py)
    - 演示自动退出已加入的小组
    - 会退出所有已加入小组，谨慎使用！！！
- [自动在已加入小组发帖](example/autopost.py)
    - 演示需要验证码才能发帖的调用方式
- [自动删除已发帖子](example/autoremove.py)
    - 演示如何删除已发送的帖子
    - 这个例子会一直检测是否有新帖子，然后删除，如果不是自动删广告帖子，谨慎使用！！！
- [自动在已加入小组回帖](example/autocomment.py)
    - 演示需要验证码才能在已加入小组回帖的调用方式
    
## 其他

- 验证码识别模块调用百度AI平台提供的接口，具体见：[百度OCR技术文档](https://cloud.baidu.com/doc/OCR/index.html)   
- [auig_name_id.txt](./data/auig_name_id.txt)为豆瓣小组的名称与id映射文件，因为部分小组有个性域名，统一为id
- 如果需批量调用某项操作，所有操作之间控制好频率，以防止豆瓣账号被封禁
- 验证码识别模块自测识别率不高，后续考虑使用深度学习自己实现验证码识别功能，敬请期待
- 项目持续更新中，更多信息请见[CSDN博客文章](http://blog.csdn.net/doleria/article/details/78733899)

## 版本历史
- [V1.0](version/V1.0.md)
