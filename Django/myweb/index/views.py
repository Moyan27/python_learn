from django.shortcuts import render
from django.http import HttpResponse

#与浏览器互交的文件
#网站上有登入 支付功能 都是在views实现
#可以在浏览器显示想要显示的内容
# Create your views here.

#视图函数
def index(request):
    return HttpResponse('hallo django')