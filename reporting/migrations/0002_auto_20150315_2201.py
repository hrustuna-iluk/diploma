# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='student',
            field=models.ForeignKey(to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='reporting.Teacher', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='reporting.Department', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pass',
            name='class_passed',
            field=models.ForeignKey(to='reporting.Class', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pass',
            name='student',
            field=models.ForeignKey(to='reporting.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='event',
            field=models.ForeignKey(to='reporting.Event', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplan',
            name='responsive',
            field=models.ForeignKey(to='reporting.Teacher', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='event',
            field=models.ForeignKey(to='reporting.Event', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='reporting.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='language',
            field=models.ForeignKey(to='reporting.Language', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentwork',
            name='group',
            field=models.ForeignKey(to='reporting.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(to='reporting.Department', null=True),
            preserve_default=True,
        ),
    ]
