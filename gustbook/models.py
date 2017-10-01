from django.db import models

class words_board(models.Model):
    username = models.CharField(max_length=30)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        tpl = '<Message:[username={username}, content={content}, publish={publish}]>'
        return tpl.format(username=self.username, content=self.content, publish=self.publish)