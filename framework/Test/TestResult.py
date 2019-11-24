import json
from unitcase.public import *
from unitcase.excel_data import *
from unitcase.oprationExcel import *
from unitcase.oprationjson import *
from page.Lagou import *
from xlutils.copy import copy
import unittest
from base.Model import Model,IsAssces

class Lagou(unittest.TestCase):
    def setUp(self):
        self.obj = Model()
        self.opp = IsAssces()
        self.operationExcel = OprationExcel()
        self.operationJson = OprationJson()

    def stautscode(self,r):
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)

    def iscontent(self,r,row):
        self.stautscode(r=r)
        self.assertTrue(self.opp.isText(row=row,str2=r.text))

    def test_lagou_01(self):
        """测试拉勾翻页"""
        r = self.obj.post1(row=1,data=self.operationJson.getRequestDatas(1))
        self.iscontent(r=r,row=1)
        self.operationExcel.writeRuselt(1,"text")

    def test_lagou_02(self):
        """测试拉勾关键词职位搜索"""
        r = self.obj.post1(row=1,data=setSo("性能测试工程师"))
        #self.iscontent(r=r,row=1)
        print(r.text)
        list = []
        for item in range(0,15):
            positionId = r.json()['content']['positionResult']['result'][i]['positionId']
            list.append(positionId)
            writePositionId(json.dumps(list))
        print(positionId)
       # self.assertTrue(self.opp.isText(1,r.text))

    def test_lagou_02(self):
        """测试查看性能测试工程师的详细信息&招聘信息
            测试关键字的职位搜索
        """


if __name__ == '__main__':
    unittest.main(verbosity=2)

