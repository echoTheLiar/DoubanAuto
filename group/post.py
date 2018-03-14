# -*- coding: utf-8 -*-
import requests

from config import doubanurl
from util import doubanutil, tools
from verifycode import wordrecognition


def post_new_topic(group_url, topic_dict):
    # 在指定的小组发帖

    r = requests.post(group_url, cookies=doubanutil.get_cookies(),
                      data=topic_dict)
    doubanutil.logger.info("in func post_new_topic(), " +
                           str(group_url) + ", status_code: " + str(r.status_code))
    return r


def make_topic_dict(group_id, rev_title, rev_text):
    # 组装发帖需要的参数

    topic_new_url = doubanurl.DOUBAN_GROUP + str(group_id) + "/new_topic"
    pic_url, pic_id = doubanutil.get_verify_code_pic(topic_new_url)
    verify_code = ""
    if len(pic_url):
        pic_path = tools.save_pic_to_disk(pic_url)
        verify_code = wordrecognition.get_word_in_pic(pic_path)
    topic_dict = {
        "ck": doubanutil.get_form_ck_from_cookie(),
        "rev_title": rev_title,
        "rev_text": rev_text,
        "captcha-solution": verify_code,
        "captcha-id": pic_id,
        "rev_submit": "好了，发言"
    }
    return topic_dict
