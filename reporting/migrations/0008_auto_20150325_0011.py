# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0007_auto_20150325_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='additionalInfo',
            new_name='additional',
        ),
    ]
