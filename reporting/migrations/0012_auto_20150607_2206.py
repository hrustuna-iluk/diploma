# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0011_auto_20150527_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='subject',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
