# -*- coding: utf-8 -*-
from group import post
from config import doubanurl
from util import doubanutil

if __name__ == "__main__":
    user_id = "170612630"
    g_id = "beijingzufang"
    doubanutil.init_func()
    group_url = doubanurl.DOUBAN_GROUP + str(g_id) + "/new_topic"
    topic_dict = post.make_topic_dict(g_id, "title", "content")
    post.post_new_topic(group_url, topic_dict)
    doubanutil.logger.info("post in group: " + doubanurl.DOUBAN_GROUP + g_id)
