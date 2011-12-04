from django.db import models

from tzac.models import TitleMixin


class Type(TitleMixin, models.Model):
    pass


class City(TitleMixin, models.Model):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    type = models.ForeignKey(Type)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name
