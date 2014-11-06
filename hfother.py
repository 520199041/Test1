__author__ = 'zhenjiao.su'
# -*- coding: utf-8 -*-
class choosecity():
    def __init__(self,driver):
        self.driver=driver
    def searchcity(self):   #判断搜索，搜索5次都没结果，报错
        from selenium.webdriver.support.ui import WebDriverWait
        searexit=1
        for i in range(5):
            try:
                WebDriverWait(self.driver,10).until(lambda a:a.find_element_by_id("flightToCompanyFilter").is_displayed())
                return True
            except:
                    from random import randint
                    gcity=[]
                    ecity=[]
                    #获取去程城市热门列表
                    self.driver.find_element_by_id("depCity").click()
                    citys1=self.driver.find_elements_by_css_selector(".crl_group>*:first-of-type .search_hotList .js-hotcitylist")
                    for cityi in citys1:
                        if cityi.get_attribute("text") !="":
                            gcity.append(cityi.get_attribute("text"))
                    lengcity=len(gcity)
                    #driver.find_elements_by_css_selector(".crl_group>*:first-of-type .btn_close").click
                    #获取回程城市热门列表
                    self.driver.find_element_by_id("arrCity").click()
                    citys2=self.driver.find_elements_by_css_selector(".crl_group>*:last-of-type .search_hotList .js-hotcitylist")
                    for cityy in citys2:
                        if cityy.get_attribute("text") !="":
                            ecity.append(cityy.get_attribute("text"))
                    lenecity=len(ecity)
        #driver.find_elements_by_css_selector(".crl_group>*:last-of-type .btn_close").click
                    gcitys=gcity[randint(1,lengcity-1)]
                    ecitys=ecity[randint(1,lenecity-1)]
                    self.driver.find_element_by_id("depCity").clear()
                    self.driver.find_element_by_id("depCity").send_keys(gcitys)
                    self.driver.find_element_by_id("arrCity").clear()
                    self.driver.find_element_by_id("arrCity").send_keys(ecitys)
                    self.driver.find_element_by_id("j_submit").click()
                    searexit=searexit+1
                    if searexit==5:
                        print("搜索5次都没结果")
                        raise NameError
from selenium import webdriver
alw=webdriver.Firefox()
alw.get("http://l-tts3.vc.beta.cn6.qunar.com:9090/user/freeCombine/fcbMainPackageList.jsp?depCity=%E5%8C%97%E4%BA%AC&"
        "fromDate=2014-08-21&arrCity=%E4%B8%BD%E6%B1%9F&toDate=2014-08-23&adult=1&child=0&room=1&tm=fh_list_search")
a=choosecity(alw)
print(a.searchcity())














