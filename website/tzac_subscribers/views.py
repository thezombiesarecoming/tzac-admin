# Create your views here.
from .forms import *
from .models import *
import pdb
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

def create_subscribers(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for (k,v) in cd.iteritems():
                if v:
                    Subscriber.objects.get_or_create(type=k, value=v)
            return HttpResponseRedirect('')
    else:
        form = SubscriberForm()
    return render_to_response('tzac_subscribers/create_subscribers.html',
                              dict(form=form),
                              context_instance=RequestContext(request))
