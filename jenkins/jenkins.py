import requests
# 先打开登录首页，获取部分 cookie
url1 = "http://localhost:8081/jenkins/j_acegi_security_check"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "screenResolution=1366x768; JSESSIONID=7B7F3F66948B1965ADDD332E5425A7F4; Pycharm-470d2d8b=7eb39a7e-c2b5-41ac-95f2-ee8fdf8f2188; jenkins-timestamper-offset=-28800000; csrftoken=qsBdlvEy1RoGOFiUqpvowtF9bkeP8XAXbZAhrZnOBqgwqmX3AA6TCxHFkAPSqBsN; hudson_auto_refresh=true; _ga=GA1.1.1092626020.1560260048; ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE=YWRtaW46MTU2Mjc2NjkzMTQzODo1ODAxZTNhNDExMDlkODU1ZjFkZWIzZDg1ZGQxNWY4ZjA3NDExMmY2MDJlZDg4YzhlYmQ4YWZhYzMxYTc2OWY3; Pycharm-b245d0ed=4a1ebe68-e0eb-4b41-b28d-d0edee006e77",
    "Origin": "http://localhost:8081",
    "Referer": "http://localhost:8081/jenkins/login?from=%2Fjenkins%2F",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

form_data = {
    "j_username":" xxx",
    "j_password": "xxx",
    "from": "/jenkins/",
    "Submit": "登录",
    "remember_me": "on"
}

r = requests.post(url=url1,headers=headers,data=form_data,verify=False)
# session 会话
s = requests.session()
# c = requests.cookies.RequestsCookieJar()
# c.set("ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE","YWRtaW46MTU1MTUzNzMwNTExNDoxNTAwNjk3YjlmNGYwOTllZDUxNTA3N2RhZmVjYTdmYTgwNTI1MzJiY2E5Y2I2ZWU1OGY5MGFhZjA2ZGQ2YTg3")
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# r1 = requests.get("localhost:8080",headers=headers,verify=False)
print(r.text)

# 正则表达式提取账号和登录按钮
# import re
# t = re.findall("<b>(.+?)</b>",r.content.decode("utf-8"))#由于是编码格式，所以要进行decode解码
# print(t[0])
# print(t[1])

