from django.shortcuts import render
from blog.models import Artical,Author_massage

def index(request):
    return render(request, 'index.html')

def examples(request):
    return render(request, 'examples.html')
def a_page(request):
    product = Artical.objects.all()
    return render(request, 'page.html',{'product':product})

# Create your views here.http:/
# /127.0.0.1:8000/index/examples.html
