from django.conf.urls import url
from . import views
app_name = 'news'

urlpatterns = [
    url(r'^massage/$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^classifies/(?P<pk>[0-9]+)/$', views.classifies, name='classifies'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.search, name='search'),
]