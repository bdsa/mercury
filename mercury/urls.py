from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mercury.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('nexus.urls', namespace="nexus")),
    url(r'^contact/(?P<contact_id>\d+)/$', 'nexus.views.contact_detail', name='contact_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
