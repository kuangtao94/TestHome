import xlrd
import os
from xlutils.copy import copy
from unitcase.public import *
from unitcase.excel_data import *

class OprationExcel:
    def getExcel(self):
        db = xlrd.open_workbook(get_dir("data","data.xls"))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        """获取excel的行数"""
        return self.getExcel().nrows

    def get_row_col(self,row,col):
        """获取工作表的内容"""
        return self.getExcel().cell_value(row,col)

    def getCaseID(self,row):
        """获取测试用例的编号"""
        return self.get_row_col(row,getCaseID())

    def getUrl(self,row):
        """获取测试用例Url"""
        return self.get_row_col(row,getUrl())

    def getTitle(self,row):
        """获取测试用例Title"""
        return self.get_row_col(row,getTitle())

    def getDate(self,row):
        """获取测试用例参数"""
        return self.get_row_col(row,getData())

    def getExpect(self,row):
        """获取测试用例预期结果"""
        return self.get_row_col(row,getExptct())

    def getResult(self,row):
        """获取测试用例实际结果"""
        return self.get_row_col(row,getResult())

    def getHeaders(self):
        """获取请求头"""
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Cookie": "JSESSIONID=ABAAABAAAIAACBI2438D04CF91400F1FF0A2B38358AFFA5; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550930753; _ga=GA1.2.193872554.1550930753; _gat=1; user_trace_token=20190223220617-301cdfdc-3774-11e9-af96-525400f775ce; LGSID=20190223220617-301ce139-3774-11e9-af96-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190223220617-301ce2a8-3774-11e9-af96-525400f775ce; _gid=GA1.2.1796885419.1550930753; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=a0ad1593bd14438d8a205a17a17f95c1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550930826; LGRID=20190223220730-5b9c7593-3774-11e9-af96-525400f775ce; TG-TRACK-CODE=search_code",
            "Referer": "https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput="
        }
        return headers

    def writeRuselt(self,row,content):
        """把测试结果写入到文件当中"""
        col = getResult()
        work = xlrd.open_workbook(get_dir("data","data.xls"))
        old_work = copy(work)
        ws = old_work.get_sheet(0)
        ws.write(row,col,content)

    def get_success(self):
        """获取执行用例通过数"""
        pass_list = []
        fail_list = None
        for item in range(1,self.get_rows()):
            #print(item)
            if self.getResult(item) == "Yes":
                pass_list.append(item)
        return int(len(pass_list))

    def get_fail(self):
        """获取执行用例失败数"""
        return int(self.get_rows()-1)-int(self.get_success())

    def run_case_rate(self):
        """用例执行通过率"""
        rate = ""
        if self.get_fail() == 0:
            rate = "100%"
        elif self.get_fail()!=0:
            rate = str(int(self.get_success()/int(self.get_rows()-1)*100)) + "%"
        return rate



operation = OprationExcel()
print(operation.get_success())
print(operation.get_fail())
print(operation.run_case_rate())











