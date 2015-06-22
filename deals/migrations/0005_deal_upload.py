# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_auto_20150615_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='upload',
            field=models.FileField(default=0, upload_to=b'uploads/%Y/%m/%d/'),
        ),
    ]
