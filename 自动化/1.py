import pyqrcode
import os

path=os.path.dirname(__file__)

s='{}/1.mp3'.format(path)

url=pyqrcode.create(s)
url.png('{}/1.png'.format(path),scale=8,background=[0xff,0xff,0xff])
