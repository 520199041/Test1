__author__ = '520'
# -*- coding: utf-8 -*-
from selenium import webdriver
from Confing import confing
from excelrw import readxls
from Saveorder import saveorder
from Detaill import detail
from Search import search
from Shouye import shouye
from Saveorder import saveorder
from time import sleep
testcase1=webdriver.Firefox()
testcase1.maximize_window()
testcase1.get("http://fh.dujia.qunar.com/?tf=package")
shouyecase1=shouye(testcase1)
if shouyecase1.shouyeexit()==True:
    shouyecase1.b2ccitypeople()
    shouyecase1.b2cclick()
else:
    print(u"进入首页失败")
    raise SystemError
listcase1=search(testcase1)
if listcase1.listpageexit()==True:
    if listcase1.searchexit(searchid=1)==True:
        listhandle=testcase1.current_window_handle
        listcase1.searchclick()
    else:
        print(u"搜索失败，没有搜索结果")
else:
    print(u"进入list页失败")
allhandle=testcase1.window_handles
for detailhandle in allhandle:
    if detailhandle !=listhandle:
        testcase1.close()
        testcase1.switch_to_window(detailhandle)
detailcase1=detail(testcase1)
if detailcase1.detailpageexit()==True:
    detailcase1.detailattribute()
    sleep(10)
    if detailcase1.overexit("flightexit")==False \
            and detailcase1.overexit("hotelexit")==False \
            and detailcase1.overexit("detailpageover")==False:
         print(detailcase1.detailarepre)
         print(detailcase1.detailhotelname)
         detailcase1.detailclick()
    else:
        print(u"detail页售卖完")
        raise SystemError
else:
    print(u"进入detail页失败")
    raise SystemError
confingcase1=confing(testcase1)
if confingcase1.confingexit()==True:
    confingcase1.peopletrval()
    confingcase1.messagepeople()
    confingcase1.messagesubmit()
else:
    print(u"进入confing页失败")
    raise SystemError
saveordercase1=saveorder(testcase1)
if saveordercase1.saveorderexit()==True:
    saveordercase1.saveordersults()
    print(saveordercase1.savepayorder)
    pass
elif confingcase1.confingothenfail()==True:
    print(u"confing页提示提交失败")
    raise SystemError
else:
    print(u"confing提交异常")
    raise SystemError








