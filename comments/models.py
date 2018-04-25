# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Comments(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=300)
    url = models.URLField(blank=True,null=True)
    comment = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('news.Article')

    def __str__(self):
        return self.comment[:20]
