from django.conf.urls import patterns, url

from nexus import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
