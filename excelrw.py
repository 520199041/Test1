# coding=utf-8
__author__ = 'zhenjiao.su'
class readxls():
    def __init__(self,readurl):
        from xlrd import open_workbook
        self.readurl=readurl
        try:
            self.readworkbook=open_workbook(self.readurl)
        except:
            print("打开excel错误，请检查")
            assert SyntaxError
        self.readsheet=self.readworkbook.sheets()[0]
    def readrc(self):
        self.readrow=self.readsheet.nrows
        self.readcols=self.readsheet.ncols
    def __call__(self,y,f):
        return self.readsheet.cell(y,f).value
    def writesheet(self,wrow,wclow,writecontent):
        from xlutils.copy import copy
        writeset=copy(self.readworkbook)
        wsheet=writeset.get_sheet(0)
        wsheet.write(wrow,wclow,writecontent)
        writeset.save(self.readurl)

