from django.conf.urls.defaults import patterns, include, url
from .views import DetailView
from .views import JsonListView


urlpatterns = patterns('',
    url(r'^all/$', JsonListView.as_view()),
    url(r'^(?P<pk>[\d]+)/$', DetailView.as_view(), name="tzac_detail"),
)