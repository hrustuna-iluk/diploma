# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0007_group_short_form'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pass',
            unique_together=set([('date', 'class_passed')]),
        ),
    ]
