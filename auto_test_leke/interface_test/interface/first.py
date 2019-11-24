# coding:utf-8
import requests                #可以使用代码发送http请求
import json                    #用来处理json数据
#http中的get请求
base_url='http://192.168.0.111/wuye/public/index.php/index/index/'
p={
    'username':13000000000,
    'password':123456
}
r=requests.get(base_url+'login?',params=p)
# print(r.status_code)        #请求的状态码
# print(r.text)               #请求返回的数据
# print(r.url)                #请求发送的地址
text=json.loads(r.text)       #将接口的返回数据转换为字典
print(text['content']['token'])
# ['content["token"]']