from django.db import models

# Create your models here.
class Notification(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
