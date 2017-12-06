# -*- coding: utf-8 -*-
import random
import time

from group import quit
from util import doubanutil

if __name__ == "__main__":
    user_id = "71623092"
    doubanutil.init_func()
    group_joins_sets = doubanutil.get_group_joins(user_id)
    for group_id in group_joins_sets:
        quit.auto_quit_group(quit.get_quit_group_url(group_id))
        random_int = random.randint(1, 5)
        time.sleep(random_int)

