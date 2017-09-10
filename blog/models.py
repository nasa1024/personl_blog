from django.db import models

# Create your models here.


class Author_massage(models.Model):
    name = models.CharField(max_length=50)
    join_date = models.DateField(u'加入日期', auto_now_add=True, editable = True)
#    head_portrait = models.ImageField()
    self_introduce = models.CharField(u'个性签名',max_length=240)

    def __str__(self):
        return self.name

    def my_property(self):
        return self.name + '  ' + self.self_introduce
    my_property.short_description = "author_massage"

    person_introduce = property(my_property)


class Artical(models.Model):
    author = models.ForeignKey(Author_massage)
    title = models.CharField(u'标题',max_length=300)
    main_body = models.TextField(u'内容')
    distribute_date = models.DateField(u'发表时间', auto_now_add=True, editable = True)

    def __str__(self):
        return self.title

