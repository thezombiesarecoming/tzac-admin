from armstrong.core.arm_sections.models import Section
from armstrong.core.arm_sections.managers import SectionSlugManager
from django.core.urlresolvers import reverse
from django.db import models


class TitleMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=250, default="")

    def __unicode__(self):
        return self.title

# Create your models here.
class Page(TitleMixin, models.Model):
    body = models.TextField()

    sections = models.ManyToManyField(Section, null=True, blank=True,
            related_name="%(app_label)s_%(class)s_alternates")

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("tzac_detail", kwargs={"pk": self.pk})


class List(TitleMixin, models.Model):
    pass


class ListItem(TitleMixin, models.Model):
    list = models.ForeignKey(List, related_name="items")
