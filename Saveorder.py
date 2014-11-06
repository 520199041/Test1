__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
class saveorder():
    def __init__(self,driver):
        self.driver=driver
    def saveordersults(self):
        savepayorder=self.driver.find_element_by_css_selector(".total.c6>.pr").text
        self.savepayorder=(savepayorder.encode('utf-8')).strip("¥")
    def saveorderexit(self): #判断是否进入saveorder
        try:
            WebDriverWait((self.driver),10).until(lambda a:a.find_element_by_id("goPaying"))
            return True
        except:
            return False
    def saveoverexit(self):   #是否提示产品售磬
        try:
            saveorverexits=self.driver.find_element_by_class_name("cancel").is_displayed()
            if saveorverexits==True:
                return
            else:
                return
        except:
            return False
    def savepaychangeexit(self): #判断是否有变价提示
        try:
            WebDriverWait(self.driver,3).until(lambda a:a.find_element_by_css_selector(".b_pop_wrap.js_p_tip").is_displayed())
            return True
        except:
            return False
    def savepaychange(self): #有变价提示的操作
        paychangestate=self.driver.find_element_by_id("check").get_attribute("checked")
        #if paychangestate=="None":
        self.driver.find_element_by_id("check").click()
        self.driver.find_element_by_class_name("ok").click()
    def saveorderpay(self): #提交支付
        self.driver.find_element_by_id("goPaying").click()
    def saveorderstate(self):  #是否已跳到支付中心，根据前端是否弹出支付状态提示
        try:
            WebDriverWait(self.driver,10).until(lambda a:a.find_element_by_css_selector(".success.js_successbox").is_displayed())
            return True
        except:
            return False
