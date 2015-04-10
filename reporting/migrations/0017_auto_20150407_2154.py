# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0016_auto_20150407_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='amountOfWeekInFirstSemester',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='amountOfWeekInSecondSemester',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='endFirstSemester',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='endSecondSemester',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='startFirstSemester',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='startSecondSemester',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
