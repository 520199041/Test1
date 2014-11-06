__author__ = 'zhenjiao.su'
#-*- coding: utf-8 -*-
import Other
class payserver():
    def __init__(self,driver):
        self.driver=driver
    def payserverresults(self):
        #self.paymomey=self.driver.find_element_by_css_selector("#pay_count_detail .price_change").text  #支付金额
        #self.driver.find_element_by_class_name("show").click()
        #peoplecount=self.driver.find_element_by_css_selector(".order_sub_name_details td:nth-child(1)").text  #出行人数
        #self.peoplecounts=other.splittext(peoplecount,1,"：")
        messagepeople=self.driver.find_element_by_css_selector(".order_sub_name_details td:nth-child(2)").text #联系人
        self.messagepeoples=Other.splittext(messagepeople,1,"：")
        #self.payhotelname=self.driver.find_element_by_css_selector("#detail_more_ctn_box>div>div>div:nth-child(3)").text  #酒店名称
