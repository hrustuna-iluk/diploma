# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0012_auto_20150331_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='amountOfWeekInFirstSemester',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='amountOfWeekInSecondSemester',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='endFirstSemester',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='faculty',
            name='endSecondSemester',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='faculty',
            name='startFirstSemester',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='faculty',
            name='startSecondSemester',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
