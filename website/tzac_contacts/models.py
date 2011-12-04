from django.contrib.gis.db import models
import json

from tzac.models import TitleMixin


class Type(TitleMixin, models.Model):
    pass


class City(TitleMixin, models.Model):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, related_name="contacts")
    type = models.ForeignKey(Type)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    lon = models.FloatField()
    lat = models.FloatField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "city": str(self.city),
            "type": str(self.type),
            "address": self.address,
            "phone": self.phone,
        }