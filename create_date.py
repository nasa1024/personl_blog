# -*- coding: utf-8 -*-
from news.models import Tag,Article,Classify
from blog.wsgi import *

def main():
    classify_list = [
        'python 学习',
        'djanog 学习',
        '计算机技巧学习',
    ]
    user_list = [
        'root',
        'jin',
        'song',
    ]
    for classify in classify_list:
        c = Classify.objects.get_or_create(name = classify)[0]
        for i in range(1,5):
            for user in user_list:
                    article = Article.objects.get_or_create(
                        title='{}_[}'.format(classify, i),
                        body='教程内容：{}'.format(classify),
                        brief = 'article_{}'.format(i),
                        author = '{}'.format(user),
                    )[0]
    tag_list = [
        'python',
        'django',
        'computer',
    ]
    for tag in tag_list:
        b = Tag.objects.get_or_create(name = tag)[0]


if __name__ == '__main':
    main()
    print ("done")

