__author__ = 'zhenjiao.su'
# class Package():
#     def __init__(self,driver):
#         self.driver=driver
#     def hotellistclick(self):
#         self.driver.find_element_by_class_name("js_h_more").click
#     def flightlistclick(self):
#         self.driver.find_element_by_class_name("js_f_more").click
#     def packageclick(self):
#         self.driver.find_element_by_class_name("btn js_book_btn").click
#     def package(self):
#         self.packsumprice=self.driver.find_element_by_xpath("")
from selenium import webdriver
alw=webdriver.Firefox()
alw.get("http://l-tts3.vc.beta.cn6.qunar.com:9090/user/freeCombine/fcbPackageDetail.jsp?departureId=536593138&destinationId=126713771&"
        "departureCabin=P&destinationCabin=Z&depCabinType=%E7%BB%8F%E6%B5%8E%E8%88%B1&arrCabinType=%E7%BB%8F%E6%B5%8E%E8%88%B1&"
        "totalPrice=MjQwMA==&fromDate=2014-08-10&toDate=2014-08-11&hotelId=852259915&roomTypeId=10755a&depCity=%E5%8C%97%E4%BA%AC&room=1&"
        "arrCity=%E4%B8%8A%E6%B5%B7&departureId=536593138&adult=2&child=0&hp=Mjcw&fp=MjEzMA==")
#alw.find_element_by_css_selector("a[class=\"js_f_more\"]").click()
a=alw.find_element_by_css_selector("li[class=\"pack\"]:last")
print(a.text)





