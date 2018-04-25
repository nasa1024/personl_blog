from ..models import Article,Classify,Tag
from django import template
register = template.Library()
@register.simple_tag
def get_recent_post(num=5):
    return Article.objects.all().order_by('-create_time')[:num]
@register.simple_tag
def archives():
    return Article.objects.dates('create_time','month',order='DESC')
@register.simple_tag
def get_categories():
    return Classify.objects.all()
@register.simple_tag
def get_tag():
    return Tag.objects.all()