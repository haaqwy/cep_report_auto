#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time: 2018/7/2 17:14
@Author: Yun.Wu1
@File: base_page.py
@Software: PyCharm
"""

from selenium import webdriver


class BasePage(object):
    """
        定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver
