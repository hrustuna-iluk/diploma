# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='group',
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher'},
        ),
        migrations.RemoveField(
            model_name='class',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
