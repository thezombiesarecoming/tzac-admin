from tastypie import fields
from tastypie.resources import ModelResource
from .models import *


class ListResource(ModelResource):
	class Meta:
		queryset = List.objects.all()
		resource_name = "list"

	items = fields.ToManyField("tzac.api.ListItemResource", "items")


class ListItemResource(ModelResource):
	class Meta:
		queryset = ListItem.objects.all()
		resources = "list_item"
