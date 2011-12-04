from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# API set
from tastypie.api import Api
from tzac.api import *
v1_api = Api(api_name="v1")
v1_api.register(ListResource())
v1_api.register(ListItemResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^page/', include('tzac.urls')),
    url(r'^section/', include('tzac_sections.urls')),
    url(r'^contacts/', include('tzac_contacts.urls')),
    url(r'^api/', include(v1_api.urls)),

    # TODO: move this to S3 or some such
    url(r'^static/(?P<path>.*)$',
        'django.contrib.staticfiles.views.serve')
)
