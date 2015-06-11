# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_auto_20150608_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
