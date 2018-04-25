from news.models import Classify,Tag
from django.db.models import Count
from django import template

register = template.Library()
@register.simple_tag
def get_categories():
    return Classify.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
@register.simple_tag
def get_tag():
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)

