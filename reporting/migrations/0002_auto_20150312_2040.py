# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('group', models.ForeignKey(to='reporting.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='class',
            name='schedule',
            field=models.ForeignKey(to='reporting.Schedule', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='classRoom',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ClassRoom',
        ),
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(choices=[('Monday', 'Понеділок'), ('Tuesday', 'Вівторок'), ('Wednesday', 'Середа'), ('Thursday', 'Четвер'), ('Friday', "П'ятниця"), ('Saturday', 'Субота'), ('Sunday', 'Неділя')], max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='subject',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AlterField(
            model_name='pass',
            name='type',
            field=models.CharField(choices=[('pass', 'Без поважної причини'), ('sickness', 'По хворобі'), ('statement', 'Заява'), ('watch', 'Чергування')], max_length=50),
            preserve_default=True,
        ),
    ]
