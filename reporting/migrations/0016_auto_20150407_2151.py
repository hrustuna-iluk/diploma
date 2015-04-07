# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0015_faculty_dean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(blank=True, null=True, max_length=255),
            preserve_default=True,
        ),
    ]
