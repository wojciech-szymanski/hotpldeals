import datetime

from django.db import models
from django.utils import timezone

class Deal(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title