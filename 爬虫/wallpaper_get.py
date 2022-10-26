import numpy as np
import requests
from lxml import etree
import threading
import os


class Wallpaper(object):
    def __init__(self, page):
        self.url_list=[]
        self.data_url_list=[]
        self.content_url_list = []
        for i in range(1,page + 1):
            url = 'https://wallhaven.cc/search?q=id%3A65348&sorting=random&ref=fp&seed=B6VgC9&page={}'.format(i)
            self.url_list.append(url)
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
            'cookie': '_pk_id.1.01b8=3c6174703146a14b.1664869689.; _pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1666706094%2C%22https%3A%2F%2Flimestart.cn%2F%22%5D; _pk_ses.1.01b8=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlRcL0VTRlhoc1R2cXI5UFc2bHJXS1ZRPT0iLCJ2YWx1ZSI6IlZHYW9XK1FSUThUcllcL0NpNkhcL3pFT2FTRHFXQVJMeTFnaGxBQ0hBc1M4S2xlWnQ3NFBuRXNWU2JVczlyV0tzSXhndzBIMUNURjludFBkeFpCRERxOStoUTJ1VFArTHIyK21ENEFjUGwwbmRpcDFBb09kU0NnOVRtaDJiY1krYXllTGdRaFhaWGRFSzR6Zkd5aUlEQ08rOVJubXY4WjBNUnJcL2V4VFZsU0dsdE1sRE1rQkpzWVM1dmpEeFZueTd1WSIsIm1hYyI6ImZjN2YyYTRjYTZmNTExYjA5NGFlZWNhZjA3MjQwNDBjYzY2MWM4NTg2Mzk5Yjk1ZTE4MjI2YWEwNWE3ZjU4OTIifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IklzdDg3cjNVeXZJcW5SeGpPR0x5ZlE9PSIsInZhbHVlIjoiUHpaT3oxQUViVWhGSkZjcklzZ1AyOEh1MG8zS244enErREEwc3NzRUkySUQ2RjdlRTZIMzhtMTkzOGlhSlhiRSIsIm1hYyI6ImEyZTk5NWUwOWNiMTc0ZmUwMzg5MWQ3MTJmZGY5NTQwNjM1ODJjNjg5NjY0MjFiOTdkNjBhYjcyOTA4NTRiZDMifQ%3D%3D; wallhaven_session=eyJpdiI6ImJQYkZJQzg1Mkl0czFVQ3Jna1g0Ymc9PSIsInZhbHVlIjoiUkFNbFBLajRzWStEY3ErZWZWVjFoME55QzhkakJvT1JFdlJoa1BxQWNjb2NOZ2lTSkxaRlNjbTZUMTQ5Y0MweiIsIm1hYyI6IjRjMjhiOTg5ZWJlNWNmN2UzZWY5Zjc4MDA4NjY5OTRkZjE1MTBjNzM2NDYwOTQxY2JhYjE1Mzk5MGJiNzhhODIifQ%3D%3D',

        }

    def build_savepath(self):
        #self.path=os.getcwd()
        self.path=os.path.dirname(__file__)
        if os.path.exists('{}/wallpaper'.format(self.path)):
            pass
        else:
            os.mkdir('{}/wallpaper'.format(self.path))
    def save_data(self,url):
        res=requests.get(url,headers=self.headers)
        xml=etree.HTML(res.content.decode('utf-8'))
        content_url= xml.xpath('//*[@id="wallpaper"]/@src')
        try:
            content_data=requests.get(content_url[0]).content
            with open('{}/wallpaper/{}'.format(self.path,content_url[0].split('/')[-1]),'wb')as f:
                f.write(content_data)
        except:
            pass

    def get_data(self):
        for url in self.url_list:
            response = requests.get(url=url,headers=self.headers)
            html=etree.HTML(response.content)
            data=html.xpath('//*[@id="thumbs"]/section/ul/li/figure/a[2]/@href')
            self.data_url_list.append(data)
        self.data_url_list=list(np.ravel(self.data_url_list))

    def built_threading(self):
        for url in self.data_url_list:
            t=threading.Thread(target=self.save_data,args=(url,))
            t.start()
    def run(self):
        self.build_savepath()
        self.get_data()
        #这是一个测试
        #self.save_data(self.data_url_list[4],1)
        self.built_threading()
if __name__ == '__main__':
    page=int(input('输入要下载的页数:'))
    Wallpaper(page).run()
