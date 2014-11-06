__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
from random import uniform
from excelrw import readxls
from selenium.webdriver.support.ui import WebDriverWait
class search:
    def __init__(self,driver):
        self.driver=driver
        self.elread=readxls("f:/element.xls")
    def listpageexit(self):    #是否进入list页
        try:
            WebDriverWait(self.driver,10).until(lambda a:a.find_element(self.elread(1,5),self.elread(1,6)))
            return True
        except:
            return False
    def searchexit(self,searchid=None):  #判断有没有搜索结果，等待20s
        try:
            WebDriverWait(self.driver,20).until(lambda a:a.find_element(self.elread(2,5),self.elread(2,6)))
        except:
            return False
        else:
            searchlen=self.driver.find_elements(self.elread(8,5),self.elread(8,6))   #获取搜索页的结果数，随机生成想要选择的结果
            if searchid ==None:
                self.searchid=int(uniform(1,len(searchlen)))
            else:
                self.searchid=searchid
            return True
    def searchresults(self):
        #搜索页平均价
        self.aveprice=self.driver.find_element(self.elread(3,5),self.elread(3,6)%(self.searchid)).text
        #搜索页总价
        self.sumprice=self.driver.find_element(self.elread(4,5),self.elread(4,6)%(self.searchid)).text
        #去程航班名
        goflight=self.driver.find_element(self.elread(5,5),self.elread(5,6)%(self.searchid)).get_attribute("textContent")
        self.goflight=goflight.strip()
        #回程航班名
        backflight=self.driver.find_element(self.elread(6,5),self.elread(6,6)%(self.searchid)).get_attribute("textContent")
        self.backflight=backflight.strip()
        #酒店名称
        self.gohotel=self.driver.find_element(self.elread(7,5),self.elread(7,6)%(self.searchid)).text
    def searchclick(self):   #随机选择产品提交
        self.driver.find_element(self.elread(9,5),self.elread(9,6)%(self.searchid)).click()




