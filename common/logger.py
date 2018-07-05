#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time: 2018/7/4 17:11
@Author: Yun.Wu1
@File: logger.py
@Software: PyCharm
"""

import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        else:
            pass
        log_file_name = log_path + ct + '.log'
        fh = logging.FileHandler(log_file_name)
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def ge_log(self):
        return self.logger


if __name__ == '__main__':
    log = Logger('test').ge_log()
    log.info('info')
    log.debug('debug')
    log.warning('warning')
    log.error('error')
