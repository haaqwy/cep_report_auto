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
        log_path = os.path.dirname(os.getcwd() + '/logs')
        log_file_name = log_path + ct + '.log'
        fh = logging.FileHandler(log_file_name)
