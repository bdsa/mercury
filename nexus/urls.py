from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

from nexus import views

urlpatterns = patterns('',
    url(r'^$', views.ContactIndexView.as_view(), name='contact_index'),
    url(r'^contacts/(?P<pk>\d+)/$', views.ContactView.as_view(), name='contact_detail'),
    url(r'^contacts/new/$', views.ContactCreate.as_view(), name='contact_create'),
    url(r'^contacts/(?P<pk>\d+)/edit/$', views.ContactUpdate.as_view(), name='contact_update'),
    url(r'^contacts/(?P<pk>\d+)/delete/$', views.ContactDelete.as_view(success_url='/contacts/'), name='contact_delete'),
    url(r'^roles/$', views.RoleIndexView.as_view(), name='role_index'),
    url(r'^roles/new/$', views.RoleCreate.as_view(success_url='/roles/'), name='role_create'),
)
