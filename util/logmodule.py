# -*- coding: utf-8 -*-
import datetime
import logging
import os

from config import filepath


class LogModule:
    def __init__(self, cmd_level=logging.DEBUG, file_level=logging.DEBUG):
        # Todo:split the log file by day
        now = datetime.datetime.now()
        log_file = str(now.strftime("%Y-%m-%d")) + ".log"
        if not os.path.exists(filepath.log_path):
            os.mkdir(filepath.log_path)
        os.chdir(filepath.log_path)
        if not os.path.exists(log_file):
            open(log_file, "a+")
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # set cmd log info
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(cmd_level)
        # set file log info
        fh = logging.FileHandler(log_file)
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
