from django.conf.urls import url
from gustbook import views
#from django.conf.urls.static import static
#from django.conf import settings


urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^save/$', views.save, name='save'),
]#+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)