# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20150315_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='student',
            field=models.ForeignKey(to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='group',
            field=models.ForeignKey(to='reporting.Group', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='reporting.Teacher', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='headOfDepartment',
            field=models.ForeignKey(related_name='head', blank=True, to='reporting.Teacher', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='culturalWork',
            field=models.ForeignKey(related_name='cultural', blank=True, to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='reporting.Department', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='deputyHeadman',
            field=models.ForeignKey(related_name='deputy', blank=True, to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='editorialBoard',
            field=models.ManyToManyField(blank=True, related_name='editorial', to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='healthWork',
            field=models.ForeignKey(related_name='health', blank=True, to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(related_name='leader', blank=True, to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='organizer',
            field=models.ForeignKey(related_name='organiser', blank=True, to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='otherTasks',
            field=models.ManyToManyField(blank=True, related_name='other', to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pass',
            name='class_passed',
            field=models.ForeignKey(to='reporting.Class', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pass',
            name='student',
            field=models.ForeignKey(to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='event',
            field=models.ForeignKey(to='reporting.Event', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='responsive',
            field=models.ForeignKey(to='reporting.Teacher', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='event',
            field=models.ForeignKey(to='reporting.Event', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='reporting.Group', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentwork',
            name='group',
            field=models.ForeignKey(to='reporting.Group', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(to='reporting.Department', blank=True, null=True),
            preserve_default=True,
        ),
    ]
