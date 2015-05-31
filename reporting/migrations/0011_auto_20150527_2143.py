# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0010_group_master'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicplan',
            old_name='amount_hours',
            new_name='amountHours',
        ),
        migrations.RenameField(
            model_name='publicplan',
            old_name='amount_present',
            new_name='amountPresent',
        ),
    ]
