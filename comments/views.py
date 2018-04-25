# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from news.models import Article
from django.shortcuts import render,redirect,get_object_or_404
from .models import Comments
from .forms import CommentsForm
# Create your views here.
def post_comment(request,post_pk):
    post = get_object_or_404(Article,pk=post_pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comments_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list,
                       }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)
