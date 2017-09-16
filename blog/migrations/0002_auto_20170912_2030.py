# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='distribute_date',
            field=models.DateField(auto_now_add=True, verbose_name='发表时间'),
        ),
        migrations.AlterField(
            model_name='artical',
            name='main_body',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='artical',
            name='title',
            field=models.CharField(max_length=300, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='author_massage',
            name='join_date',
            field=models.DateField(auto_now_add=True, verbose_name='加入日期'),
        ),
        migrations.AlterField(
            model_name='author_massage',
            name='self_introduce',
            field=models.CharField(max_length=240, verbose_name='个性签名'),
        ),
    ]
