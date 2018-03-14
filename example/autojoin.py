# -*- coding: utf-8 -*-
from group import join
from util import doubanutil

if __name__ == "__main__":
    doubanutil.init_func()
    user_id = "替换为你的user id"
    join.auto_join_group(join.get_join_group_url("替换为你想加入的小组id"))
