# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_auto_20150324_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parents',
            old_name='fullname',
            new_name='fullName',
        ),
    ]
