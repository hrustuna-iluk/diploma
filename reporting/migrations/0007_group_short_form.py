# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0006_class_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='short_form',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
