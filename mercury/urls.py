from django.conf.urls import patterns, include, url

from nexus.views import ContactIndexView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mercury.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ContactIndexView.as_view(), name='index'),
    url(r'^contacts/', include('nexus.urls', namespace="nexus")),
    url(r'^contact/', include('nexus.urls', namespace="nexus")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'nexus/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),
)
