# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0012_auto_20150607_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['lastName', 'firstName'], 'verbose_name': 'Student'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['lastName', 'firstName'], 'verbose_name': 'Teacher'},
        ),
    ]
