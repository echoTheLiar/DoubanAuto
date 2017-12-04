# -*- coding: utf-8 -*-
import requests
from lxml import etree

import util.logmodule as logmodule
import util.doubanurl as doubanurl
import util.doubanutil as doubanutil


def auto_join_group(join_group_url):
    # 自动加入小组

    r = requests.get(join_group_url, cookies=doubanutil.get_cookies())
    doubanutil.logger.info("in func auto_join_group(), " + str(join_group_url) + ", status_code: " + str(r.status_code))


def get_join_group_url(group_id):
    # 获取加入小组的链接

    group_url = doubanurl.DOUBAN_GROUP + str(group_id) + "/"
    r = requests.get(group_url, cookies=doubanutil.get_cookies())
    if r.status_code == 200:
        join_group_url = get_bn_join_group(r.text)
        if len(join_group_url):
            doubanutil.logger.info(str(join_group_url))
        else:
            doubanutil.logger.warning("the join_group_url is empty:" + str(join_group_url))
        return join_group_url
    else:
        doubanutil.logger.warning(str(group_url) + ", status_code: " + str(r.status_code))
        return ""


def get_bn_join_group(text):
    # 通过html提取自动加入小组的链接

    html = etree.HTML(text)
    join_group_url = html.xpath("//a[@class='bn-join-group']/@href")

    if len(join_group_url):
        return join_group_url[0]
    else:
        return ""
