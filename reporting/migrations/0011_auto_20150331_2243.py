# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0010_student_currentaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='specialization',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(max_length=255, choices=[('dean', 'Декан'), ('Head of Department', 'Завідувач кафедри'), ('Deputy Dean', 'Заступник декана'), ('teacher', 'Викладач')]),
            preserve_default=True,
        ),
    ]
