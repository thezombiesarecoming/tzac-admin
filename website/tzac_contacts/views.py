from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic import DetailView
import json

from tzac_sections.views import JsonMixin
from .models import *


class AllCityJsonListView(JsonMixin, ListView):
    queryset = City.objects.all()

    def convert_to_json(self, context):
        object_list = []
        for obj in context["object_list"]:
            object_list.append({
                "city": obj.title,
                "resource_uri": reverse("tzac_contacts_type_list",
                        kwargs={"pk": obj.pk}),
            })
        return json.dumps({"object_list": object_list})


class JsonDetailView(JsonMixin, DetailView):
    model = City

    def convert_to_json(self, context):
        types = {}
        city = City.objects.get(pk=self.kwargs["pk"])
        for obj in city.contacts.all().order_by("type"):
            if obj.type.title not in types:
                types[obj.type.title] = []
            types[obj.type.title].append(obj.to_dict())
        return json.dumps({"object_list": types})

