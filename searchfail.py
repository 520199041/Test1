__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
class productfail():
    def __init__(self,driver):
        self.driver=driver
    def productfailexit(self):
        try:
            self.driver.find_element_by_class_name("cancel js_p_s_btn")
            return True
        except:
            return False
    def productfailclick(self):
        self.driver.find_element_by_class_name("cancel js_p_s_btn").click()
