from django.conf.urls.defaults import patterns, include, url
from .views import DetailView


urlpatterns = patterns('',
    url(r'^(?P<pk>[\d]+)/$', DetailView.as_view())
)