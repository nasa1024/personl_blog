# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别'


class Classify(models.Model):
    name = models.CharField(max_length=100,verbose_name='公司名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '公司名称'

class Article(models.Model):

    title = models.CharField('标题',max_length=10000)
    body = models.TextField('正文')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    excerpt = models.CharField('摘要',max_length=200,blank=True)
    classifies= models.ForeignKey(Classify)
    tags = models.ManyToManyField(Tag)
    auth = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('news:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self,*args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '咨询列表'






    def __str__(self):
        return self.title
