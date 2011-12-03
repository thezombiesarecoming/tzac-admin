from armstrong.core.arm_sections.models import Section
from armstrong.core.arm_sections.managers import SectionSlugManager
from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    sections = models.ManyToManyField(Section, null=True, blank=True,
            related_name="%(app_label)s_%(class)s_alternates")

    with_section = SectionSlugManager(section_field="sections")

    objects = models.Manager()

    def __unicode__(self):
        return self.title
