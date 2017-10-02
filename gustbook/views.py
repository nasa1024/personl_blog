from django.shortcuts import render
from gustbook.models import words_board
from django.shortcuts import HttpResponseRedirect

def index(request):
    message = words_board.objects.all()
    return render(request,'index1.html',{'messages':message})

def save(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    content = request.POST.get("content")
 #   publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = words_board(content=content, username=username, e_mail=email)
    message.save()

    return HttpResponseRedirect('/gustbook/index/')

def create(request):
    return render(request, 'create.html')
