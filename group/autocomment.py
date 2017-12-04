# -*- coding: utf-8 -*-
import sys
import time
import random

import comment
import util.doubanutil as doubanutil
import util.doubanurl as doubanurl

if __name__ == "__main__":
    topic_url = doubanurl.DOUBAN_TOPIC + "110015658" + "/add_comment#last"
    comment_str = doubanurl.REDBAG_TOKEN
    comment_dict = {
        "ck": "WHLx",
        "rv_comment": comment_str,
        "start": 0,
        "submit_btn": "加上去"
    }
    comment.comment_topic(topic_url, comment_dict)
