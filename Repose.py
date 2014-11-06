def testhttp():
    #coding=utf-8
    import requests
    from excelrw import readxls
    readpg=readxls("f:/jikou.xls")
    readpg.readrc()
    testhttptype=readpg.readnumber(0,0)  #获取请求类型
    testhttpurl=readpg.readnumber(0,4)   #获取请求url
    testhttplen=readpg.readrow   #获取表行数
    testhttphi=readpg.readcols   #获取表列数
    testft=readpg.readnumber(0,5)   #获取是否需要输出自定义key的值
    key=[]
    value=[]
    httpexit=readpg.readnumber(0,3)
    print(u"。。。。。。请等待。。。。。。。。")
    if httpexit==1:
        for i in range(testhttplen):     #获取输入的自定义请求参数，转化成字典
            ukey=readpg.readnumber(i,1)
            uvalue=readpg.readnumber(i,2)
            if isinstance(uvalue,float)==True:
                uvalue=int(uvalue)
            key.append(ukey)
            value.append(uvalue)
        httppar=dict(zip(key,value))
    else:
        httppar=False
    if testhttptype=="get":      #判断请求类型
        if httppar==False:
            testhttp=requests.get(testhttpurl)
            testtext=testhttp.json()   #获取返回值，为一个字典
            print(testhttp.url)   #打印所请求的最后url
            if testft==1:     #判断是否需要输出自定义key的值
                testpkey=[]
                for i1 in range(6,testhttphi):    #获取输入的key
                    keyc=readpg.readnumber(0,i1)
                    testpkey.append(keyc)
                for i2 in testpkey:     #输出自定义key的值
                    testvalue1=testtext[i2]
                    testvalue=testvalue1
                    testtext=testvalue1
                print(testvalue)
            else:
                print(testhttp.text)    #不想输出自定义Key值，则打印全部返回结果
        else:
            testhttp=requests.get(testhttpurl,params=httppar)
            print(testhttp.url)
            if testft==1:
                testpkey=[]
                testtext=testhttp.json()    #获取返回值，为一个字典
                for i1 in range(6,testhttphi):    #获取输入的key
                    keyc=readpg.readnumber(0,i1)
                    testpkey.append(keyc)
                for i2 in testpkey:     #输出自定义key的值
                    testvalue1=testtext[i2]
                    testvalue=testvalue1
                    testtext=testvalue1
                print(testvalue)
            else:
                print(testhttp.text)
    elif testhttptype=="post":
        if httppar==False:
            testhttp=requests.post(testhttpurl)
            testtext=testhttp.json()   #获取返回值，为一个字典
            print(testhttp.url)
            if testft==1:
                testpkey=[]
                for i1 in range(6,testhttphi):    #获取输入的key
                    keyc=readpg.readnumber(0,i1)
                    testpkey.append(keyc)
                for i2 in testpkey:     #输出自定义key的值
                    testvalue1=testtext[i2]
                    testvalue=testvalue1
                    testtext=testvalue1
                print(testvalue)
            else:
                print(testhttp.text)
        else:
            testhttp=requests.post(testhttpurl,data=httppar)
            testtext=testhttp.json()   #获取返回值，为一个字典
            print(testhttp.url)
            if testft==1:
                testpkey=[]
                for i1 in range(6,testhttphi):    #获取输入的key
                    keyc=readpg.readnumber(0,i1)
                    testpkey.append(keyc)
                for i2 in testpkey:     #输出自定义key的值
                    testvalue1=testtext[i2]
                    testvalue=testvalue1
                    testtext=testvalue1
                print(testvalue)
            else:
                print(testhttp.text)





