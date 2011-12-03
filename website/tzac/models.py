from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __unicode__(self):
        return self.title
