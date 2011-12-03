from django.conf.urls.defaults import patterns, include, url
from .views import JsonDetailView
from .views import JsonListView


urlpatterns = patterns('',
    url(r'^all/$', JsonListView.as_view(),
            name="tzac_sections_list"),
    url(r'^(?P<pk>[\d]+)/$', JsonDetailView.as_view(),
            name="tzac_sections_detail"),
)
