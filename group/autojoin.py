# -*- coding: utf-8 -*-
import sys
import time
import random

import join
import util.doubanutil as doubanutil
import util.filepath as filepath

if __name__ == "__main__":
    doubanutil.init_func()
    user_id = "61659622"
    group_joins_sets = doubanutil.get_group_joins(user_id)
    group_id_sets = doubanutil.get_active_group_set()
    group_id_sets_to_join = group_id_sets - group_joins_sets
    for group_id in group_id_sets_to_join:
        try:
            random_int = random.randint(1, 20)
            with open(filepath.cjgi_txt, "a+") as f_cjgi:
                join.auto_join_group(join.get_join_group_url(group_id))
                f_cjgi.write(str(group_id) + "\n")
            time.sleep(1)
        except:
            exc = sys.exc_info()
            doubanutil.logger.error("join group_id:" + str(group_id) + " failed, exceptions info: "
                              + str(exc[0]) + " " + str(exc[1]))
        else:
            doubanutil.logger.info("sleep for " + str(random_int) + " seconds...")
            time.sleep(random_int)


