# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20150421_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='test@test.ru', max_length=255),
            preserve_default=False,
        ),
    ]
