import pyqrcode
import os

path=os.path.dirname(__file__)

s=input('输入url或字符串：')
url=pyqrcode.create(s)
url.png('{}/hailong.png'.format(path),scale=8,background=[0xff,0xff,0xff])
