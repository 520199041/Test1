__author__ = '520'
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from Shouye import *
from Search import *
from Detaill import *
from Confing import *
alw=webdriver.Firefox()
alw.maximize_window()
alw.get("http://fh.dujia.qunar.com/?tf=package")
shouyes=shouye(alw)
if shouyes.shouyeexit()==True:
    shouyes.b2ccitypeople()
    shouyes.b2cclick()
else:
    print(u"进入首页失败")
    alw.quit()
    raise SystemError
searchs=search(alw)
if searchs.listpageexit()==True:
    if searchs.searchexit()==True:
        searchs.searchclick()
    else:
        print(u"搜索页没有结果")
        alw.quit()
        raise SystemError
else:
    print(u"进入list页失败")
    alw.quit()
    raise SystemError
listhandl=alw.current_window_handle
detalhandls=alw.window_handles
for detalhandl in detalhandls:
    if detalhandl !=listhandl:
        detalhandl=detalhandl
alw.close()
alw.switch_to_window(detalhandl)
details=detail(alw)
sleep(5)
if details.detailpageexit()==True:
    if details.detailpageover()==False:
        if details.hotelexit()==False and details.flightexit()==False:
            details.detailattribute()
            details.detailclick()
        else:
            print(u"机票或酒店售卖完")
            raise SystemError
    else:
        print(u"产品售卖完")
        raise SystemError
else:
    print(u"进入detail失败")
    raise SystemError
confings=confing(alw)
if confings.confingexit()==True:
    confings.peopletrval()
    confings.messagepeople()
else:
    print(u"进入confing失败")
    raise SystemError
