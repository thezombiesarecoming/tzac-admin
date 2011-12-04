from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from .models import *

from tastypie.api import Api
from api import SubscriberResource
v1_api = Api(api_name='v1')
v1_api.register(SubscriberResource())


urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
                      )
