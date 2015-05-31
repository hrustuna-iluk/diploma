# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_auto_20150416_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefits',
            options={'verbose_name_plural': 'Benefits'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='parents',
            options={'verbose_name_plural': 'Parents'},
        ),
        migrations.AlterModelOptions(
            name='pass',
            options={'verbose_name_plural': 'Passes'},
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(unique=True, null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(unique=True, null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
