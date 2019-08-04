"""cookies & session"""

import requests

def getHeader():
    headers = {
        "Referer": "http://www.renren.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    }
    return  headers

data = {
    "email":"18797815816",
    "icode":"",
    "origURL":"http://www.renren.com/home",
    "domain":"renren.com",
    "key_id":1,
    "captcha_type":"web_login",
    "password":"6b69ae46a1c78265f722380ac31b9d5e94204a364e309f8adca6f18713540b26",
    "rkey":"be9f4755aa7fd0fc3ca8d3f46599b2b8",
    "f":"http%3A%2F%2Fwww.so.com%2Flink%3Furl%3Dhttp%253A%252F%252Fwww.renren.com%252F%26q%3D%25E4%25BA%25BA%25E4%25BA%25BA%25E7%25BD%2591%26ts%3D1547910931%26t%3D8f97a40b328ad0db6b6c80359da7a8b"
}

def login():
    s = requests.Session()
    re = s.post(
        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019062317996",
        data = data,
        headers = getHeader()
    )
    return s

def getPeofile():
    re = login().get(url = "http://www.renren.com/969120248")
    print(re.text)

getPeofile()