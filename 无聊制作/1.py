import pyqrcode
import os

path=os.path.dirname(__file__)

s='I Love You'

url=pyqrcode.create(s)
url.png('{}/2.png'.format(path),scale=8,background=[0xff,0xff,0xff])
