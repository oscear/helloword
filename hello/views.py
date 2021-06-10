from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    return render(request, 'demo.html')
def home(request):
    return render(request, 'home.html')
def home1(request, year, month):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))
def home2(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home1时间标签：%s年/%s月" %(year, month))
def yoyo(request):
    context = {}
    context['name'] = '奥斯卡'
    return render(request, 'yoyo.html', context)
def page1(request):
    return render(request, 'page1.html')
def sonpage(request):
    context = {"ads": ["selenium", "appium", "requests"]
               }
    return render(request, 'sonpage.html', context)