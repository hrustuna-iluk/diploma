# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20150312_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='group',
        ),
        migrations.RemoveField(
            model_name='class',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AddField(
            model_name='class',
            name='group',
            field=models.ForeignKey(null=True, to='reporting.Group'),
            preserve_default=True,
        ),
    ]
