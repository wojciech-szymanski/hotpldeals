# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='published_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
