#coding:utf-8
import xlrd                 #导入读取excel的工具
# wb=xlrd.open_workbook(r'D:\python_work\auto_test\data\user.xlsx')     #打开excel文件
# # table=wb.sheet_by_index(0)        #通过索引的方式大开页签
# table=wb.sheet_by_name('Sheet1')        #通过名字打开页签
# r=table.row_values(1)                    #通过索引读取指定的行
# print(r[0])
# # c=table.col_values(0)                           #通过索引读取指定的列
# g=table.cell(1,1)                         #读取指定的格
#
#



#coding:utf-8
from TestCase.auto_test_leke.web_test.config import param
import xlrd
class excle_data():
    def __init__(self):
        # url='D:\\python_work\\auto_test\\data\\'
        self.wb=xlrd.open_workbook(param.data_path+'user.xlsx')
    def get_sheet1(self,n):
        try:
            table=self.wb.sheet_by_index(0)
            r=table.row_values(n-1)
            return r
        except:
            print('获取第一个页签失败')
    def get_sheet2(self,n):
        try:
            table=self.wb.sheet_by_index(1)
            r=table.row_values(n-1)
            return r
        except:
            print('获取第二个页签失败')
    def get_sheet3(self,n):
        try:
            table=self.wb.sheet_by_index(2)
            r=table.row_values(n-1)
            return r
        except:
            print('获取第三个页签失败')
if __name__ =='__main__':
    quzhi=excle_data()
    print(quzhi.get_sheet1(1))












