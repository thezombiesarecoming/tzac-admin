from django.db import models

# Create your models here.
class Subscriber(models.Model):
    '''Represents a service subscriber to be notified'''
    type = models.CharField(max_length=200)
    value = models.TextField()
