# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0013_auto_20150405_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(null=True, to='reporting.Faculty', blank=True),
            preserve_default=True,
        ),
    ]
