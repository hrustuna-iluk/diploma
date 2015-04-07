# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0014_department_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='dean',
            field=models.ForeignKey(to='reporting.Teacher', null=True, blank=True),
            preserve_default=True,
        ),
    ]
