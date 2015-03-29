# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0008_auto_20150325_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='classRoom',
            new_name='classroom',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='number_of_week',
            new_name='numberOfWeek',
        ),
    ]
