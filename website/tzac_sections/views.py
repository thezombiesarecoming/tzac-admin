from armstrong.core.arm_sections.models import Section
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView as DjangoDetailView
import json



class JsonMixin(ListView):
    def render_to_response(self, context):
        return HttpResponse(self.convert_to_json(context),
                content_type="application/json")


class JsonListView(JsonMixin, ListView):
    model = Section

    def convert_to_json(self, context):
        object_list = []
        for obj in context["object_list"]:
            object_list.append({
                "title": obj.title,
                "url": reverse("tzac_sections_detail",
                        kwargs={"pk": obj.pk}),
            })

        return json.dumps({"object_list": object_list})



class JsonDetailView(JsonMixin, DjangoDetailView):
    model = Section

    def convert_to_json(self, context):
        object_list = []
        section = self.model.objects.get(pk=self.kwargs["pk"])

        # TODO: this may change in the future -- it's
        #       <app>_<model>_alternates for now.  It's generated
        #       on the armstrong.core.arm_sections side.
        page_list = section.tzac_page_alternates.all()
        for obj in page_list:
            object_list.append({
                "title": obj.title,
                "url": obj.get_absolute_url(),
            })
        return json.dumps({"object_list": object_list})
