from django.conf.urls.defaults import patterns, include, url
from .views import AllCityJsonListView
from .views import JsonDetailView


urlpatterns = patterns('',
    url(r'^$', AllCityJsonListView.as_view(),
            name="tzac_contacts_city_list"),
    url(r'^(?P<pk>[\d]+)/$', JsonDetailView.as_view(),
            name="tzac_contacts_type_list"),
)
