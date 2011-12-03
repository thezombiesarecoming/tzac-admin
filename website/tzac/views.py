from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView as DjangoDetailView
import json

from .models import Page


class JsonListView(ListView):
    model = Page

    def render_to_response(self, context):
        return HttpResponse(self.convert_to_json(context),
                content_type="application/json")

    def convert_to_json(self, context):
        object_list = []
        for obj in context["object_list"]:
            object_list.append({
                "title": obj.title,
                "url": obj.get_absolute_url(),
            })

        return json.dumps({"object_list": object_list})


class DetailView(DjangoDetailView):
    model = Page
