# -*- coding: utf-8 -*-
import requests

from config import doubanurl
from util import doubanutil


def auto_quit_group(quit_group_url):
    # 自动退出小组

    r = requests.get(quit_group_url, cookies=doubanutil.get_cookies())
    doubanutil.logger.info("in func auto_quit_group(), " + str(quit_group_url) + ", status_code: " + str(r.status_code))
    return r


def get_quit_group_url(group_id):
    # 获取退出小组的链接

    group_url = doubanurl.DOUBAN_GROUP + str(group_id) + "/"
    return doubanutil.get_value_from_group_url(group_url, get_link_quit_group)


def get_link_quit_group(text):
    # 通过html提取自动退出小组的链接

    quit_group_url_xpath = "//a[@class='j a_confirm_link']/@href"
    return doubanutil.get_value_from_html(text, quit_group_url_xpath)
