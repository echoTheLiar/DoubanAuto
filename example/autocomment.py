# -*- coding: utf-8 -*-
import requests
from lxml import etree

from group import comment
from config import doubanurl
from util import doubanutil

if __name__ == "__main__":
    group_id = "beijingzufang"
    group_url = doubanurl.DOUBAN_GROUP + group_id
    r = requests.get(group_url, cookies=doubanutil.get_cookies())
    group_topics_html = etree.HTML(r.text)
    group_topics = group_topics_html.xpath(
        "//table[@class='olt']/tr/td[@class='title']/a/@href")
    group_topics = group_topics[5:]
    for topic_url in group_topics:
        comment_topic_url = topic_url + "/add_comment#last"
        comment_str = "up"
        comment_dict = comment.make_comment_dict(group_id, topic_url, comment_str)
        comment.comment_topic(comment_topic_url, comment_dict)

