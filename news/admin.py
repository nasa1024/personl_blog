# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article,Classify,Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','update_time','excerpt','auth','classifies']
admin.site.register(Article,ArticleAdmin)
admin.site.register(Classify)
admin.site.register(Tag)

# class MyAdminSite(admin.AdminSite):
#     site_header = '长春工业大学3+1信息发布'
#     site_title = '信息发布管理'

# admin_site = MyAdminSite(name='management')
# admin_site.register(MyAdminSite)
# admin_site.register(Article,ArticleAdmin)
# admin_site.register(Classify)
# admin_site.register(Tag)