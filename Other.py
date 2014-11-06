__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
def splittext(text,loc,str):  #自定义切分
    return (text.split(str))[loc]
class pageother():
    def __init__(self,driver):
        self.driver=driver
    def pageoverexit(self):
        try:
            self.driver.find_element_by_css_selector(".cancel js_p_s_btn")
            return True
        except:
            return False
    def pageoverclick(self):
        self.driver.find_element_by_css_selector(".cancel.js_p_s_btn").click()
class login():
    def __init__(self,driver):
        self.driver=driver
    def logins(self):
        self.driver.find_element_by_name("username").clear
        self.driver.find_element_by_name("username").send_keys("13603068412")
        self.driver.find_element_by_name("password").clear
        self.driver.find_element_by_name("password").send_keys("520041")
        self.driver.find_element_by_css_selector(".login_submit>button").click()
        sleep(4)
        try:
            WebDriverWait(self.driver,10).until(lambda a:a.find_element_by_class_name("q_header_uname"))
            print(u"登陆成功")
        except:
            print(u"登陆异常")
            raise SystemError









