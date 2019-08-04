# import  requests
#
# url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1133058157172-ems.html"
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Cookie": "UM_distinctid=168517f91751f4-0abb1ecd4-4349052c-100200-168517f917631c; sid=s6t8pmhrnisa45vq0b6ma9qov6; CNZZDATA1254194234=793473636-1547553066-%7C1548251235; lang=zh-cn; theme=default",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",\
#     "Referer":"http://www.kuaidi.com/",
#     "X-Requested-With":"XMLHttpRequest",
#     "Origin":"http://www.kuaidi.com",
#     "Accept-Encoding":"gzip, deflate"
#
# }
#
# data = {
#     "geetest_challenge":"6313656bb7ed45d59797530526582a93cw",
#     "geetest_validate":"48e32e86389c2bf3b03a5ef231486b35",
#     "geetest_seccode":"48e32e86389c2bf3b03a5ef231486b35|jordan"
# }
# s = requests.session()
# r = s.post(url=url,headers=headers,data=data,verify=False)
# print(r.text)
# print(r.json())


# coding:utf-8
import requests
# 请求头
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0)Gecko/20100101 Firefox/44.0"
}
s = requests.session()
# 打开我的随笔
r = s.get('https://i.cnblogs.com/EditPosts.aspx?opt=1',
headers=headers,
allow_redirects=True,
verify=False)
# 打印状态码，自动处理重定向请求
print (r.status_code)
# new_url = r.headers["Location"]
# print (new_url)
print(r.text)
print(r.content)
print(r.headers)