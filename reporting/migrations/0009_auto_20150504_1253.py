# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0008_auto_20150504_1252'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pass',
            unique_together=set([('student', 'date', 'class_passed')]),
        ),
    ]
