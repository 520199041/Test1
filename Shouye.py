# __author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
class shouye():
    def __init__(self,driver):  #初始化配置
      from excelrw import readxls
      self.driver=driver
      self.b2cread=readxls("f:/abc.xls")
      self.elread=readxls("f:/element.xls")
    def shouyeexit(self):  #判断是否进入首页
        try:
            WebDriverWait(self.driver,10).until(lambda a:a.find_element(self.elread(1,1),self.elread(1,2)))
            return True
        except:
            return False
    def b2ccitypeople(self):  #信息输入
        #从excel中取数据
        self.b2cqcity=self.b2cread(1,0)
        self.b2chcity=self.b2cread(1,1)
        self.b2cpeople=self.b2cread(1,2)
        self.b2cchild=self.b2cread(1,3)
        godatejs=str(self.b2cread(1,14))
        backdatejs=str(self.b2cread(1,15))
        # self.b2croom=self.b2cread(1,4)
        #城市输入
        self.driver.find_element(self.elread(1,1),self.elread(1,2)).clear()
        self.driver.find_element(self.elread(1,1),self.elread(1,2)).send_keys(self.b2cqcity)
        self.driver.find_element(self.elread(2,1),self.elread(2,2)).send_keys(self.b2chcity)
        #人数输入
        self.driver.find_element(self.elread(3,1),self.elread(3,2)).click()
        peoples1=self.driver.find_elements(self.elread(4,1),self.elread(4,2))
        peoples1[int(self.b2cpeople)].click()
        self.driver.find_element(self.elread(5,1),self.elread(5,2)).click()
        peoples2=self.driver.find_elements(self.elread(6,1),self.elread(6,2))
        peoples2[int(self.b2cchild)].click()
        #出发与回程日期输入
        # print(godatejs)
        # print(backdatejs)
        # godatejs=("document.getElementById(\"js_fromdate\").value=%s"%godatejs)
        # batedatejs=("document.getElementById(\"js_todate\").value=%s"%backdatejs)
        # self.driver.execute_script(godatejs)
        # self.driver.execute_script(batedatejs)
        #房间选择
        # self.driver.find_element_by_css_selector(".b_select_wrap.cr3_group_x3").click()
        # room1=self.driver.find_elements_by_css_selector(".b_select_wrap.cr3_group_x3 .yselector_suggest a")
        # room1[int(self.b2croom)].click()
    def b2cclick(self): #请求点击
        self.driver.find_element(self.elread(7,1),self.elread(7,2)).click()






