from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world !  django ~~")
def yoyo(request):
    return HttpResponse("yoyo!  django ~~ ")
