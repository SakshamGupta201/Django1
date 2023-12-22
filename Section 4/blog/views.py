from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog/blog.html')

def posts(request):
    pass

def detail_post(request,slug):
    pass