# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.IntegerField(default=1, choices=[('1', 1), ('2', 2)]),
            preserve_default=False,
        ),
    ]
