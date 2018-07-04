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
        定义一个页面基类，封装常用的页面操作
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 浏览器前进
    def forward(self):
        self.driver.forward()

    # 浏览器后退
    def back(self):
        self.driver.back()


