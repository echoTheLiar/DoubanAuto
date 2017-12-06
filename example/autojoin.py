# -*- coding: utf-8 -*-
import random
import time

from group import join
from util import doubanutil

if __name__ == "__main__":
    doubanutil.init_func()
    user_id = "170612630"
    group_joins_sets = doubanutil.get_group_joins(user_id)
    group_id_sets = doubanutil.get_active_group_set()
    group_id_sets_to_join = group_id_sets - group_joins_sets
    for group_id in group_id_sets_to_join:
        try:
            random_int = random.randint(1, 20)
            join.auto_join_group(join.get_join_group_url(group_id))
            time.sleep(1)
        except Exception as e:
            doubanutil.logger.error("join group_id:" + str(group_id) + " failed, exceptions info: "
                                    + str(e.message))
            time.sleep(1)
        else:
            doubanutil.logger.info("sleep for " + str(random_int) + " seconds...")
            time.sleep(random_int)
