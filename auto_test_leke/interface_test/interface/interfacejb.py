# coding:utf-8
import requests                #可以使用代码发送http请求
import json                    #用来处理json数据

class interface():
    def __init__(self):
        self.base_url='https://www.gjfax.com/toLogin'
    def login(self,username,password):
        p={
            'mobilePhone':username,
            'password':password,
            'userType':'1',
            'yzm':'',
            'referrerURL':'',
            'hasLease':'',
            'gjfax_token_name':'D0UNX0N90GPDUMVGAIX1TY07BDKSMTUV',
            'protocolTag':'0'
        }
        try:
            r=requests.post(self.base_url+'login',params=p)
            rd=json.loads(r.text)             #将接口返回数据转换为字典
            return rd
        except:
            print('登录接口访问失败')
    def oauthAccount(self,username):
        p={
            'username':username
        }
        try:
            r=requests.get(self.base_url+'oauthAccount?',params=p)
            rd=json.loads(r.text)             #将接口返回数据转换为字典
            return rd
        except:
            print('接口访问失败')
    def allCommunityId(self,username,password):
        if self.login(username,password)['success']==True:
            token=self.login(username,password)['content']['token']
            p={
            'username':username,
            'token':token
            }
        else:
            p={
                'username':username,
                'token':'aaaaaaaaaa'
            }
        try:
            r=requests.get(self.base_url+'allCommunityId?',params=p)
            rd=json.loads(r.text)             #将接口返回数据转换为字典
            return rd
        except:
            print('接口访问失败')
    def taskInfoListByCondition(self,username,password):
        if self.login(username,password)['success']==True:
            token=self.login(username,password)['content']['token']
            p={
                'username':username,
                'token':token,
                'communityId':1,
                'pageNum':1,
                'pageSize':2
            }
        else:
            p={
                'username':username,
                'token':'aaaaaaaaaa',
                'communityId':1,
                'pageNum':1,
                'pageSize':2
            }
        try:
            r=requests.get(self.base_url+'taskInfoListByCondition?',params=p)
            rd=json.loads(r.text)             #将接口返回数据转换为字典
            return rd
        except:
            print('接口访问失败')
    def buildingInfoList(self,username,password):
        if self.login(username,password)['success']==True:
            token=self.login(username,password)['content']['token']
            p={
            'username':username,
            'token':token,
            'communityId':1
            }
        else:
            p={
                'username':username,
                'token':'aaaaaaaaaa',
                'communityId':1
            }
        try:
            r=requests.get(self.base_url+'buildingInfoList?',params=p)
            rd=json.loads(r.text)             #将接口返回数据转换为字典
            return rd
        except:
            print('接口访问失败')
    def buildingHouseList(self,username,password):
        if self.login(username,password)['success']==True:
            token=self.login(username,password)['content']['token']
            p={
            'token':token,
            'communityId':1
            }
        else:
            p={
                'token':'aaaaaaaaaa',
                'communityId':1
            }
        try:
            r=requests.get(self.base_url+'buildingHouseList?',params=p)
            rd=json.loads(r.text)             #将接口返回数据转换为字典
            return rd
        except:
            print('接口访问失败')
if __name__=='__main__':
    a=interface()
    b=a.login('18513600235','a123456')
