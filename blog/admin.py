from django.contrib import admin
from .models import Author_massage
from .models import Artical

# Register your models here.

class Author_inroduce(admin.ModelAdmin):
    show_display = ('my_property',)

admin.site.register(Artical)
admin.site.register(Author_massage,Author_inroduce)