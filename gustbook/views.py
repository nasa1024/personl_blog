from django.shortcuts import render
from gustbook.models import words_board

def index(request):
    message = words_board.objects.all()
    return render(request,'index.html',{'messages':message})

def save(request):
    username = request.POST.get("username")
    #title = request.POST.get("title")
    content = request.POST.get("content")
 #   publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = words_board(content=content, username=username)
    message.save()

    #return HttpResponse('/gustbook/index/')
    return render(request,'save.html')

def create(request):
    return render(request, 'create.html')
