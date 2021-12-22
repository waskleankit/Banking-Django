from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def hello_world(request):
    message = " <h1>Hello World</h1>"
    return HttpResponse(message)

def index_page(request):
    message = " <h4>Welcom to  Banking Project</h4>"
    message = message + "<a href='/customer/'> CustomerApp</h4>"
    return HttpResponse(message)

def home_page(request):
    return render(request,"home.html")

class AboutUs(View):
    def get(self, request):
        # <view logic>
        message = "<h3>We provide all solutions . </h3>"
        return HttpResponse(message)