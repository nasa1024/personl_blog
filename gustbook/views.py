from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

def index(request):
    message = models.words_board.objects.all()
    return render(request,'guestbook/index.html',{'message':message})

def save(request):
    username = request.POST.get("username")
    title = request.POST.get("title")
    content = request.POST.get("content")
 #   publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = models.Message(title=title, content=content, username=username, publish=publish)
    message.save()

    return HttpResponseRedirect('/guestbook/index/')