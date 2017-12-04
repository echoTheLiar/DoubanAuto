# -*- coding: utf-8 -*-
import requests

import util.logmodule as logmodule
import util.doubanurl as doubanurl
import util.doubanutil as doubanutil


def comment_topic(topic_url, comment_dict):
    # 在一个帖子下发表回复

    r = requests.post(topic_url, cookies=doubanutil.get_cookies(),
                      data=comment_dict)
    doubanutil.logger.info("in func comment_topic(), " +
                           str(comment_dict) + ", status_code: " + str(r.status_code))
