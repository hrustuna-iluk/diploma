# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=25)),
                ('classRoom', models.CharField(max_length=25)),
                ('day', models.CharField(choices=[('Monday', 'Понеділок'), ('Tuesday', 'Вівторок'), ('Wednesday', 'Середа'), ('Thursday', 'Четвер'), ('Friday', "П'ятниця"), ('Saturday', 'Субота'), ('Sunday', 'Неділя')], max_length=20)),
                ('number_of_week', models.CharField(choices=[('1', 1), ('2', 2)], max_length=2)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.CharField(max_length=25)),
                ('yearStudy', models.IntegerField()),
                ('tuition', models.CharField(choices=[('stationary', 'Стаціонар'), ('extramural', 'Заочна форма')], max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fullname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('pass', 'Без поважної причини'), ('sickness', 'По хворобі'), ('statement', 'Заява'), ('watch', 'Чергування')], max_length=50)),
                ('class_passed', models.ForeignKey(to='reporting.Class')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicPlan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=255, blank=True)),
                ('amount_hours', models.FloatField()),
                ('amount_present', models.IntegerField()),
                ('event', models.ForeignKey(to='reporting.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateField()),
                ('event', models.ForeignKey(to='reporting.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('firstName', models.CharField(max_length=255, blank=True)),
                ('lastName', models.CharField(max_length=255, blank=True)),
                ('middleName', models.CharField(max_length=255, blank=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('isProcurement', models.BooleanField(default=False)),
                ('dateBirth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('maritalStatus', models.CharField(choices=[('single', 'Не одружений'), ('married', 'Одружений')], max_length=50)),
                ('sex', models.CharField(choices=[('male', 'Чоловіча'), ('female', 'Жіноча')], max_length=50)),
                ('school', models.CharField(max_length=255)),
                ('benefits', models.ManyToManyField(null=True, blank=True, to='reporting.Benefits')),
                ('group', models.ForeignKey(to='reporting.Group')),
                ('language', models.ForeignKey(to='reporting.Language')),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentWork',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('text', models.TextField()),
                ('year', models.CharField(max_length=10)),
                ('group', models.ForeignKey(to='reporting.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('firstName', models.CharField(max_length=255, blank=True)),
                ('lastName', models.CharField(max_length=255, blank=True)),
                ('middleName', models.CharField(max_length=255, blank=True)),
                ('position', models.CharField(choices=[('dean', 'Декан'), ('Head of Department', 'Завідувач кафедри'), ('teacher', 'Викладач')], max_length=255)),
                ('department', models.ForeignKey(to='reporting.Department')),
            ],
            options={
                'verbose_name': 'Teacher',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publicplan',
            name='responsive',
            field=models.ForeignKey(to='reporting.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pass',
            name='student',
            field=models.ForeignKey(to='reporting.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(to='reporting.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='culturalWork',
            field=models.ForeignKey(null=True, to='reporting.Student', related_name='cultural'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(null=True, blank=True, to='reporting.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='reporting.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='deputyHeadman',
            field=models.ForeignKey(null=True, to='reporting.Student', related_name='deputy'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='editorialBoard',
            field=models.ManyToManyField(null=True, to='reporting.Student', related_name='editorial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='healthWork',
            field=models.ForeignKey(null=True, to='reporting.Student', related_name='health'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(null=True, to='reporting.Student', related_name='leader'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='organizer',
            field=models.ForeignKey(null=True, to='reporting.Student', related_name='organiser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='otherTasks',
            field=models.ManyToManyField(null=True, to='reporting.Student', related_name='other'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='headOfDepartment',
            field=models.ForeignKey(null=True, to='reporting.Teacher', related_name='head'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='group',
            field=models.ForeignKey(to='reporting.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='reporting.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='additional',
            name='student',
            field=models.ForeignKey(to='reporting.Student'),
            preserve_default=True,
        ),
    ]
