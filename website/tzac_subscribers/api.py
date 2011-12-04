from tastypie import fields
from tastypie.resources import ModelResource
from .models import *

class SubscriberResource(ModelResource):
    class Meta:
        queryset = Subscriber.objects.all()
        resources = "subscriber"
