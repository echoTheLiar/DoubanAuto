# -*- coding: utf-8 -*-
import sys
import time
import random

import post
import util.doubanutil as doubanutil
import util.doubanurl as doubanurl
import util.tools as tools
import verifycode.wordrecognition as wordrecg

if __name__ == "__main__":
    group_id = "583132"
    group_url = doubanurl.DOUBAN_GROUP + str(group_id) + "/new_topic"
    pic_url, pic_id = doubanutil.get_verify_code_pic(group_id)
    verify_code = ""
    if len(pic_url):
        pic_path = tools.save_pic_to_disk(pic_url)
        verify_code = wordrecg.get_word_in_pic(pic_path)
    topic_dict = {
        "ck": doubanutil.get_form_ck_from_new_post(group_url),
        "rev_title": doubanurl.REDBAG_TITLE,
        "rev_text": doubanurl.REDBAG_TOKEN,
        "captcha-solution": verify_code,
        "captcha-id": pic_id,
        "rev_submit": "好了，发言"
    }
    post.post_new_topic(group_url, topic_dict)
