# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article,Classify,Tag
from django.shortcuts import get_object_or_404
from comments.forms import CommentsForm
import markdown
from django.views.generic import ListView
from django.db.models import Q

from django.http import HttpResponse

# Create your views here.
#主页
class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 3

#文章详情
def detail(request,pk):
    post = get_object_or_404(Article,pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentsForm()
    comment_list = post.comments_set.all()
    context = {'post':post,
               'form':form,
               'comment_list':comment_list
               }

    return render(request,'blog/detail.html',context=context)
#归档
def archives(request,year,month):
    post_list = Article.objects.filter(update_time__year=year,
                                       update_time__month=month,
                                       ).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
#分类
def classifies(request,pk):
    cate = get_object_or_404(Classify,pk=pk)
    post_list = Article.objects.filter(classifies=cate).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
class TagView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)
def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入想要查找的关键词'
        return render(request,'blog/index.html',{'error_msg':error_msg})
    post_list = Article.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg,
                                               'post_list': post_list})



