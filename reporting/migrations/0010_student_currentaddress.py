# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0009_auto_20150325_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='currentAddress',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
