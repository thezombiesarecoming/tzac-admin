import json

from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
import requests


# Create your models here.
class Notification(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.subject

    def post_to_couch(self):
        if not hasattr(settings, "NOTIFICATION_ENDPOINT"):
            print "settings does not have NOTIFICATION_ENDPOINT?"
            return

        payload = json.dumps({
            "text": self.body,
            "title": self.subject,
        })
        response = requests.put(settings.NOTIFICATION_ENDPOINT, data=payload)
        print response


def post_to_couch_signal(sender, instance=None, created=None, **kwargs):
    print "signal fired"
    print "instance: %s" % instance
    print "created: %s" % created
    if instance and created:
        instance.post_to_couch()


post_save.connect(post_to_couch_signal, sender=Notification)
