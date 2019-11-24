import requests
from lxml import etree

class  Spider(object):
    def __init__(self):
        self.offset=1
    def start_request(self,next_page):
         print('正在爬取第%d张......'% self.offset)
         self.offset+=1
         response=requests.get(next_page)
         text=response.text
         html = etree.HTML(text)
         video_src = html.xpath('//div[@class="video-play"]/video/@src')
         video_title = html.xpath('//span[@class="video-title"]/text()')
         next_page = 'http:' + html.xpath('//a[@class="next"]/@href')[0]
         self.start_request(next_page)
         self.write(video_src, video_title)
    def write(self,text):
        for src,title in zip(video_src,video_title):
              response=requests.get('http://'+src)
              filename=title+'.mp4'
              filename=''.join(filename.split('/'))
              print('正在抓取%d......' %filename)
              with open(filename,'wb') as f:
                  f.write(response.content)
spider=Spider()
spider.start_request('https://ibaotu.com/shipin/7-0-0-0-0-1.html')










Fad = "FinshC"
for i in Fad:
    print(i,end=" ")

    print("\n")

for i in range(10):
    if i % 2 != 0 :
        print(i)
        continue
    i += 2
    print(i)


n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        print(n)
        continue
    print(n)

