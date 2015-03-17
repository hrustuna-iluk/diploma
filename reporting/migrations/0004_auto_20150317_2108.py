# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_auto_20150315_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parents',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='test@test.ru', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='father',
            field=models.ForeignKey(to='reporting.Parents', blank=True, null=True, related_name='father'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='mother',
            field=models.ForeignKey(to='reporting.Parents', blank=True, null=True, related_name='mother'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='event',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='event',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
