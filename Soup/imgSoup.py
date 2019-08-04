from bs4 import BeautifulSoup
import requests
import os

r = requests.get("http://699pic.com/sousuo-218808-13-1-0-0-0.html")
fengjing = r.content
soup = BeautifulSoup(fengjing,"html.parser")
#print(soup.prettify())
#找出所有class标签
images = soup.find_all(class_="lazy")
print(images)
for item in images:
    try:
        jpg_url = item["data-original"]
        title = item["title"]
        print(title)
        print(jpg_url)
        print("")
        #保存图片
        with open(os.getcwd()+"\\jpg"+title+".jpg","wb") as f:
            f.write(requests.get(jpg_url).content)
    except Exception as e:
        pass

