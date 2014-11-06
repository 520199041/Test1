__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
from excelrw import readxls
from selenium.webdriver.support.wait import WebDriverWait
class detail():
    def __init__(self,driver):
        self.driver=driver
        self.elread=readxls("f:/element.xls")
    def detailpageexit(self):  #判断是否在detail页
        try:
            WebDriverWait(self.driver,10).until(lambda a:a.find_element(self.elread(1,9),self.elread(1,10)))
            return True
        except:
            return False
    def detailattribute(self):    #获取detail页相关参数
        detailarepre=self.driver.find_element(self.elread(2,9),self.elread(2,10)).get_attribute("textContent")  #获得均价
        self.detailarepre=(detailarepre.encode('utf-8')).strip("¥") #均价去除金钱符号
        detailsumpre=self.driver.find_element(self.elread(3,9),self.elread(3,10)).get_attribute("textContent")
        self.detailsumpre=(detailsumpre.encode('utf-8')).strip("¥")  #总价
        self.detailhotelname=self.driver.find_element(self.elread(4,9),self.elread(4,10)).text   #酒店名称
        self.detailgoflightname=self.driver.find_element(self.elread(5,9),self.elread(5,10)).text #去程航空公司
        self.detailendflightname=self.driver.find_element(self.elread(6,9),self.elread(6,10)).text  #回程航空公司
    def overexit(self,namekey):    #自定义判断页面售罄类型
        def fhpover(by,value):
            try:
                self.driver.find_element(by,value)
                return True
            except:
                return False
        overdict={"flightexit":fhpover(self.elread(7,9),self.elread(7,10)),
                  "hotelexit":fhpover(self.elread(8,9),self.elread(8,10)),
                  "detailpageover":fhpover(self.elread(9,9),self.elread(9,10))}
        return overdict.get(namekey,u"没有此类型判断")
    def detaillogexit(self):   #判断提交载入状态
        try:
            self.driver.find_element(self.elread(10,9),self.elread(10,10))
            return True
        except:
            return False
    def detailroomsearch(self):  #随机选择房型与输入当前所选择的房间类型
        from random import uniform
        roomlen=len(self.driver.find_elements(self.elread(11,9),self.elread(11,10)))
        if roomlen>3:   #当前房间数大于3，则点击获取其它房型
            self.driver.find_element(self.elread(12,9),self.elread(12,10)).click()
        roomnumber=int(uniform(1,roomlen+1)) #生成随机整数
        roomstate=self.driver.find_element(self.elread(13,9),self.elread(13,10)%roomnumber)
        if not roomstate.get_attribute("className") =="ok":   #若当前房间已被选择，则不进行选择操作
            self.driver.find_element(self.elread(14,9),self.elread(14,10)%roomnumber).click()
        self.roomname=self.driver.find_element(self.elread(15,9),self.elread(15,10)%roomnumber).get_attribute("title")
    def detailupdate(self,updateflight=None,updatehotel=None):   #更换机票or更换酒店
        if updateflight==True:
            self.driver.find_element(self.elread(18,9),self.elread(18,10)).click()
        elif updatehotel==True:
            self.driver.find_element(self.elread(19,9),self.elread(19,10)).click()
        else:
            raise SystemError
    def detailclick(self):   #detail提交预订
        try:
            self.driver.find_element(self.elread(16,9),self.elread(16,10))    #判断立即按钮是否变灰，变灰则报错
        except:
            self.driver.find_element(self.elread(17,9),self.elread(17,10)).click()
        else:
            print(u"立即按钮变灰，报错")
            raise SystemError













