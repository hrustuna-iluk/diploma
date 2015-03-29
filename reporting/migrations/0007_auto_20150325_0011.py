# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0006_auto_20150324_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='additional',
        ),
        migrations.DeleteModel(
            name='Additional',
        ),
        migrations.AddField(
            model_name='student',
            name='additionalInfo',
            field=models.CharField(blank=True, null=True, max_length=255),
            preserve_default=True,
        ),
    ]
