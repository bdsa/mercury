from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

from nexus import views

urlpatterns = patterns('',
    url(r'^$', views.ContactIndexView.as_view(), name='contact_index'),
    url(r'^(?P<pk>\d+)/$', views.ContactView.as_view(), name='contact_detail'),
    url(r'^new/$', views.ContactCreate.as_view(), name='contact_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.ContactUpdate.as_view(), name='contact_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ContactDelete.as_view(success_url='/contacts/'), name='contact_delete'),
)
