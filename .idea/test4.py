__author__ = 'zhenjiao.su'
#-*- coding: utf-8 -*-
from selenium import webdriver
alw=webdriver.Firefox()
alw.get("http://www.baidu.com")
print(alw.find_element(by="class name",value="s_ipt").send_keys("adsfsdf"))