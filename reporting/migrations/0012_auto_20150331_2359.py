# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0011_auto_20150331_2243'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.AddField(
            model_name='publicplan',
            name='group',
            field=models.ForeignKey(null=True, blank=True, to='reporting.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='amount_hours',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='amount_present',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='responsive',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='semester',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
