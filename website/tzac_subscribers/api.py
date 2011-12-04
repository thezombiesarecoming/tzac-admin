from tastypie import fields
from tastypie.resources import ModelResource
from .models import *

class SubscriberResource(ModelResource):
    class Meta:
        queryset = Subscriber.objects.all()
        resources = "subscriber"
        excludes = ['id']
        include_resource_uri = False

    def dehydrate(self, bundle):
        bundle.data['key'] = bundle.data['type']
        bundle.data['type'] = 'endpoint'
        return bundle
