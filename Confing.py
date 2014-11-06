__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from excelrw import readxls
class confing():
    def __init__(self,driver):
        self.driver=driver
        self.peoples=readxls("f:/abc.xls")
        self.elreadc=readxls("f:/element1.xls")
    def confingexit(self):   #是否进入confing页
        try:
            WebDriverWait(self.driver,30).until(lambda a:a.find_element(self.elreadc(1,1),self.elreadc(1,2)))
            return True
        except:
            return False
    def peopletrval(self):
        adultcount=len(self.driver.find_elements(self.elreadc(2,1),self.elreadc(2,2)))
        for adults in range(1,adultcount+1):    #成人旅客信息填写
            adultname=self.peoples(adults,5)
            self.driver.find_element(self.elreadc(3,1),self.elreadc(3,2)%adults).send_keys(adultname)       #成人姓名
            self.driver.find_element(self.elreadc(4,1),self.elreadc(4,2)%adults).click()     #点击成人证件类型选择下拉框
            adultpapework=self.peoples(adults,6)
            for papeworks in range(1,9):      #证件类型选择
                adultpapename=self.driver.find_element(self.elreadc(5,1),self.elreadc(5,2)%(adults,papeworks)).text
                if adultpapename==adultpapework:
                    self.driver.find_element(self.elreadc(5,1),self.elreadc(5,2)%(adults,papeworks)).click()
            adultnumber=int(self.peoples(adults,7))
            self.driver.find_element(self.elreadc(6,1),self.elreadc(6,2)%adults).send_keys(adultnumber)         #成人证件信息填写
        #开始判断是否有儿童，若有儿童，则填写儿童相关信息
        childexit=1
        try:
            childcount=len(self.driver.find_elements(self.elreadc(7,1),self.elreadc(7,2)))
            childexit=2
        except:
            pass
        if childexit==2:
            for childs in range(1,childcount+1):
                childname=self.peoples(childs,8)
                self.driver.find_element(self.elreadc(8,1),self.elreadc(8,2)%childs).send_keys(childname)
                self.driver.find_element(self.elreadc(9,1),self.elreadc(9,2)%childs).click()
                childwork=self.peoples(childs,9)
                for papeworks in range(1,9):      #证件类型选择
                    childpapework=self.driver.find_element(self.elreadc(10,1),self.elreadc(10,2)%(childs,papeworks)).text
                    if childwork==childpapework:
                        self.driver.find_element(self.elreadc(10,1),self.elreadc(10,2)%(childs,papeworks)).click()
                childnumber=str(int(self.peoples(childs,10)))
                if childwork==u"身份证":
                    self.driver.find_element(self.elreadc(11,1),self.elreadc(11,2)%childs).send_keys(childnumber)
                else:
                    self.driver.find_element(self.elreadc(11,1),self.elreadc(11,2)%childs).send_keys(childnumber)         #儿童证件信息填写
                    self.driver.find_element(self.elreadc(12,1),self.elreadc(12,2)%childs).click()   #儿童性别
                    self.driver.find_element(self.elreadc(13,1),self.elreadc(13,2)%childs).click()  #儿童性别选择男
                    self.driver.find_element(self.elreadc(15,1),self.elreadc(15,2)%childs).send_keys(u"2011")
                    self.driver.find_element(self.elreadc(16,1),self.elreadc(16,2)%childs).send_keys(u"12")
                    self.driver.find_element(self.elreadc(17,1),self.elreadc(17,2)%childs).send_keys(u"13")
    def messagepeople(self):    ##联系信息填写
        messagename=self.peoples(1,11)
        self.driver.find_element(self.elreadc(18,1),self.elreadc(18,2)).send_keys(messagename)
        messagephone=str(int(self.peoples(1,12)))
        self.driver.find_element(self.elreadc(19,1),self.elreadc(19,2)).send_keys(messagephone)
        usermessages=self.peoples(1,13)
        self.driver.find_element(self.elreadc(20,1),self.elreadc(20,2)).send_keys(usermessages)
        try:    #判断是否登陆
            self.driver.find_element(self.elreadc(23,1),self.elreadc(23,2)).click()
            from Other import login
            confinglogin=login(self.driver)
            confinglogin.logins()
        except SystemError:
            raise SystemError
        except:
            pass
    def messagesubmit(self):
        self.driver.find_element(self.elreadc(22,1),self.elreadc(22,2)).click()
    def confingothenfail(self):  #判断10s内否出现提交失败，若出现则True,没则false
        try:
            WebDriverWait(self.driver,20).until(lambda a:a.find_element(self.elreadc(21,1),self.elreadc(22,2)))
            return True
        except:
            return False




