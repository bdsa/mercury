from django.conf.urls import patterns, url

from nexus import views

urlpatterns = patterns('',
    url(r'^$', views.ContactIndexView.as_view(), name='contact_index'),
    url(r'^(?P<pk>\d+)/$', views.ContactView.as_view(), name='contact_detail'),
)
