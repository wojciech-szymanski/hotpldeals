# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_auto_20150608_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='votes_down',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deal',
            name='votes_up',
            field=models.IntegerField(default=0),
        ),
    ]
