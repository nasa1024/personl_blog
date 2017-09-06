from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def examples(request):
    return render(request, 'examples.html')

def a_page(request):
    return render(request, 'page.html')

def another(request):
    return render(request, 'another.html')
# Create your views here.http:/
# /127.0.0.1:8000/index/examples.html
