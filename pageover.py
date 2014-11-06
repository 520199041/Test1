
#coding=utf-8
class choosecity():
    def city(self,driver):
        driver.find_element_by_id("depCity").click()
        gocitys=driver.find_elements_by_css_selector(".crl_sp2_1.cf:nth-of-type(1) .search_hotList .js-hotcitylist")
        gocity=gocitys[randint(1,len(gocitys))].text
        driver.find_element_by_css_selector(".crl_sp2_1.cf:nth-of-type(1) .btn_close").click()
        driver.find_element_by_id("depCity").clear()
        driver.find_element_by_id("depCity").send_keys(gocity)
        sleep(2)
        driver.find_element_by_id("arrCity").click()
        backcitys=driver.find_elements_by_css_selector(".crl_sp2_1.cf:nth-of-type(2) .search_hotList .js-hotcitylist")
        backty=backcitys[randint(1,len(backcitys))].text
        driver.find_element_by_css_selector(".crl_sp2_1.cf:nth-of-type(2) .btn_close").click()
        driver.find_element_by_id("arrCity").clear()
        driver.find_element_by_id("accCity").send_keys(backty)
        driver.find_element_by_id("j_submit").click()
a=choosecity()
a.city(alw)
