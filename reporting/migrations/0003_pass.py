# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20150211_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=50, choices=[('pass', 'Без поважної причини'), ('sickness', 'По хворобі'), ('statement', "За'ява"), ('watch', 'Чергування')])),
                ('class_passed', models.ForeignKey(to='reporting.Class')),
                ('student', models.ForeignKey(to='reporting.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
