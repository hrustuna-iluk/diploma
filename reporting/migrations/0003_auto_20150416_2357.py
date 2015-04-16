# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_class_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='semester',
            field=models.CharField(max_length=2, choices=[('1', 1), ('2', 2)]),
            preserve_default=True,
        ),
    ]
