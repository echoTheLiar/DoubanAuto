# -*- coding: utf-8 -*-
import random

import config.doubanurl as doubanurl
import group.post
import util.doubanutil as doubanutil

if __name__ == "__main__":
    g_id = "519193"
    random_i = random.randint(0, 9)
    random_j = random.randint(0, 4)
    random_sleep = random.randint(60, 300)
    group_url = doubanurl.DOUBAN_GROUP + str(g_id) + "/new_topic"
    topic_dict = group.post.make_topic_dict(g_id, doubanurl.REDBAG_TITLE_LIST[random_i],
                                            doubanurl.REDBAG_TOKEN_LIST[random_j])
    group.post.post_new_topic(group_url, topic_dict)
    doubanutil.logger.info("post in group: " + doubanurl.DOUBAN_GROUP + g_id)
