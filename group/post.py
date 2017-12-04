# -*- coding: utf-8 -*-
import requests

import util.logmodule as logmodule
import util.doubanurl as doubanurl
import util.doubanutil as doubanutil

def post_new_topic(group_url, topic_dict):
    # 在指定的小组发帖

    r = requests.post(group_url, cookies=doubanutil.get_cookies(),
                      data=topic_dict)
    doubanutil.logger.info("in func post_new_topic(), " +
                           str(group_url) + ", status_code: " + str(r.status_code))
