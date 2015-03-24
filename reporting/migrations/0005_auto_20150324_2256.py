# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20150317_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional',
            name='student',
        ),
        migrations.AddField(
            model_name='publicplan',
            name='semester',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='additional',
            field=models.ManyToManyField(null=True, to='reporting.Additional', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='date',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
