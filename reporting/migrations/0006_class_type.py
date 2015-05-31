# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_teacher_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='type',
            field=models.CharField(choices=[('lecture', 'Лекція'), ('practice', 'Практика')], default='lecture', max_length=50),
            preserve_default=False,
        ),
    ]
