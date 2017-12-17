# -*- coding: utf-8 -*-
import requests

from util import doubanutil


def auto_remove_topic(remove_topic_url):
    # 自动删除发起的话题

    r = requests.get(remove_topic_url, cookies=doubanutil.get_cookies())
    doubanutil.logger.info(
        "in func auto_remove_topic(), " + str(remove_topic_url) + ", status_code: " + str(r.status_code))
    return r


def get_remove_topic_url(topic_url):
    # 获取删除话题的链接

    return doubanutil.get_value_from_group_url(topic_url, get_link_remove_topic)


def get_link_remove_topic(text):
    # 通过html提取自动删除话题的链接

    remove_topic_url_xpath = "//a[@class='j a_confirm_link']/@href"
    return doubanutil.get_value_from_html(text, remove_topic_url_xpath)
