from django.views.generic import DetailView as DjangoDetailView
# Create your views here.

from .models import Page


class DetailView(DjangoDetailView):
    model = Page
