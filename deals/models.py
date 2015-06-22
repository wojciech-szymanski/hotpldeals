import datetime

from django.db import models
from django.utils import timezone

class Deal(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    upload = models.FileField(upload_to="uploads/%Y/%m/%d/", default=0)

    def __unicode__(self):
        return self.title