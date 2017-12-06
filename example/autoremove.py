# -*- coding: utf-8 -*-
import random
import time
import requests
from lxml import etree

from group import remove
from config import doubanurl
from util import doubanutil

if __name__ == "__main__":
    user_id = "170612630"
    group_url = doubanurl.DOUBAN_GROUP_MY + str(user_id) + "/publish"
    group_topics = []
    to_delete_topics_set = set()
    while True:  # 一直轮询
        doubanutil.logger.info("检测是否有新发的帖子... ...")
        while len(group_topics) == 0:  # 检测是否有新发的帖子
            r = requests.get(group_url, cookies=doubanutil.get_cookies())
            group_topics_html = etree.HTML(r.text)
            group_topics = group_topics_html.xpath(
                "//table[@class='olt']/tr/td[@class='title']/a/@href")
            time.sleep(10)  # 每隔10秒检测一次
        for topic_url in group_topics:
            to_delete_topics_set.add(topic_url)  # 将获取到的所有帖子挪到待删除set中
        doubanutil.logger.info("to_delete_topics_set中的帖子链接如下：")
        doubanutil.logger.info(to_delete_topics_set)
        group_topics = []  # 将获取到的帖子置空
        doubanutil.logger.info("group_topics中的帖子链接如下(理论上应为空)：")
        doubanutil.logger.info(group_topics)
        random_sleep = random.randint(180, 300)
        doubanutil.logger.info("sleep for " + str(random_sleep) + " seconds...让帖子存活一段时间")
        time.sleep(random_sleep)  # 获取到帖子后，先休眠一段时间，让帖子存活一段时间
        for topic_url in to_delete_topics_set:
            remove.auto_remove_topic(remove.get_remove_topic_url(topic_url))  # 删掉刚才加入待删除set中的帖子
            doubanutil.logger.info("sleep for 10 seconds...删除间隙休眠")
            time.sleep(10)  # 删除间隙休眠
        to_delete_topics_set = set()  # 待删除set置空
        doubanutil.logger.info("to_delete_topics_set中的帖子链接如下(理论上应为空)：")
        doubanutil.logger.info(to_delete_topics_set)
